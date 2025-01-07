from datetime import datetime

from PySide6.QtWidgets import QWidget, QStackedWidget, QMainWindow, QGridLayout, QGraphicsBlurEffect, QComboBox
from sqlalchemy.sql.functions import current_date

from view.MainWindow import Ui_MainWindow
from view.login import Ui_Form as Ui_Login
from view.signup import Ui_Form as Ui_Signup
from view.main import Ui_Form as Ui_main
from view.memorize import Ui_Form as Ui_Memorize

from viewmodel.auth_view_model import LoginViewModel, SignUpViewModel
from viewmodel.memorize_view_model import MemorizeViewModel

from database.database import DatabaseConnection
from viewmodel.message import show_popup_message

from controller.config_controller import load_config, save_config

# 如果你已有 model.library, 用它来获取所有库
# 假设 get_all_libraries() 返回 [Library(id=1, name="四级"), Library(id=2, name="六级"), ...]
try:
    from model.library import get_all_libraries
except ImportError:
    # 如果你没有这个函数就写一个空的示例
    def get_all_libraries():
        return []


class MainViewModel:
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        # 获取 stackedWidget 用来切换视图
        self.stackedWidget = main_window.findChild(QStackedWidget, "stackedWidget")

        # 获取预定义的页面
        self.gridLayout_login = self.main_window.findChild(QGridLayout, "gridLayout_login")
        self.gridLayout_signup = self.main_window.findChild(QGridLayout, "gridLayout_signup")
        self.gridLayout_main = self.main_window.findChild(QGridLayout, "gridLayout_main")
        self.gridLayout_memorize = self.main_window.findChild(QGridLayout, "gridLayout_memorize")

        # 设置登录和注册视图
        self.login_view = QWidget()
        self.signup_view = QWidget()
        self.main_view = QWidget()
        self.memorize_view = QWidget()

        # 设置对应的 UI
        self.login_ui = Ui_Login()
        self.login_ui.setupUi(self.login_view)

        self.signup_ui = Ui_Signup()
        self.signup_ui.setupUi(self.signup_view)

        self.main_ui = Ui_main()
        self.main_ui.setupUi(self.main_view)

        self.memorize_ui = Ui_Memorize()
        self.memorize_ui.setupUi(self.memorize_view)

        # 初始化登录和注册的 ViewModel
        self.login_view_model = LoginViewModel(self.login_view, main_window)
        self.signup_view_model = SignUpViewModel(self.signup_view, main_window)

        # 初始化主页日期标签
        self.init_date_label()

        # 找到 comboBox_lib
        self.comboBox_lib = self.main_view.findChild(QComboBox, "comboBox_lib")
        # 加载所有库到下拉框
        self.load_libraries_to_combo()

        # 将视图添加到预定义的页面中
        self.gridLayout_login.addWidget(self.login_view)
        self.gridLayout_signup.addWidget(self.signup_view)
        self.gridLayout_main.addWidget(self.main_view)
        self.gridLayout_memorize.addWidget(self.memorize_view)

        # 设置默认显示登录视图
        self.stackedWidget.setCurrentIndex(0)

        # Connect buttons with slot functions
        self.main_ui.pushButton_main_learn.clicked.connect(self.show_learning_view)
        self.main_ui.pushButton_main_revise.clicked.connect(self.show_revise_view)

        # 动态为按钮添加高斯模糊效果
        self.add_blur_effect_to_buttons()

    def show_signup_view(self):
        """切换到注册页面"""
        self.stackedWidget.setCurrentWidget(self.signup_view)

    def show_login_view(self):
        """切换到登录页面"""
        self.stackedWidget.setCurrentWidget(self.login_view)

    # region Main view
    def init_date_label(self):
        current_date = datetime.now().strftime("%-d %B %Y")
        self.main_ui.label_main_date.setText(f"# {current_date}")

    def show_learning_view(self):
        self.stackedWidget.setCurrentIndex(3)
        print(f"[DEBUG] Learning Mode: Newly learn")
        self.memorize_view_model = MemorizeViewModel(view=self.memorize_view, main_window=self.main_window, is_review=False)
        self.memorize_view_model.learn_pressed()

    def show_revise_view(self):
        self.stackedWidget.setCurrentIndex(3)
        print(f"[DEBUG] Learning Mode: Revise")
        self.memorize_view_model = MemorizeViewModel(view=self.memorize_view, main_window=self.main_window, is_review=True)
        self.memorize_view_model.review_pressed()

    def load_libraries_to_combo(self):
        """从数据库中加载所有库，并显示在 comboBox_lib 里."""
        libraries = get_all_libraries()  # 例: [Library(id=1, name="四级"), Library(id=2, name="六级"), ...]
        self.comboBox_lib.clear()
        for lib in libraries:
            # 添加到下拉框, 显示文本=lib.name, 隐藏数据=lib.id
            self.comboBox_lib.addItem(lib.name, lib.id)

        # 如果已经在 config.json 里存了 lib_id，就设置为选中项
        conf = load_config()
        if "lib_id" in conf:
            saved_lib_id = conf["lib_id"]
            # 在下拉框里找到和 saved_lib_id 相同的 index
            index_to_set = -1
            for i in range(self.comboBox_lib.count()):
                if self.comboBox_lib.itemData(i) == saved_lib_id:
                    index_to_set = i
                    break
            if index_to_set >= 0:
                self.comboBox_lib.setCurrentIndex(index_to_set)
        else:
            self.comboBox_lib.setCurrentIndex(0)

        # 监听下拉框切换
        self.comboBox_lib.currentIndexChanged.connect(self.on_library_changed)

    def on_library_changed(self, index):
        """当用户切换了 comboBox_lib 时，把新的 library_id 写到 config.json."""
        if index < 0:
            return
        lib_id = self.comboBox_lib.itemData(index)
        conf = load_config()
        conf["lib_id"] = lib_id
        save_config(conf)
        print(f"[INFO] Updated config's lib_id to {lib_id}.")

    def add_blur_effect_to_buttons(self):
        """为所有按钮添加高斯模糊效果"""
        buttons = [
            self.login_ui.pushButton_login_login,
            self.login_ui.pushButton_login_signup,
            self.signup_ui.pushButton_signup_signup,
            self.signup_ui.pushButton_signup_cancel,

            self.main_ui.pushButton_main_sync,
            self.main_ui.pushButton_main_learn,
            self.main_ui.pushButton_main_revise,
            self.main_ui.pushButton_settings_changePwd,

            self.memorize_ui.pushButton_memorize_back,
            self.memorize_ui.pushButton_memorize_option_1,
            self.memorize_ui.pushButton_memorize_option_2,
            self.memorize_ui.pushButton_memorize_option_3,
            self.memorize_ui.pushButton_memorize_option_4,
            self.memorize_ui.pushButton_memorize_forgot
        ]

        for button in buttons:
            if button:  # 确保按钮存在
                blur_effect = QGraphicsBlurEffect()
                blur_effect.setBlurRadius(20)  # 设置模糊半径
                button.setGraphicsEffect(blur_effect)