from datetime import datetime

from PySide6.QtWidgets import QWidget, QStackedWidget, QMainWindow, QGridLayout, QGraphicsBlurEffect, QComboBox, \
    QPushButton, QTableView, QLabel, QProgressBar, QLineEdit, QCheckBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

from view.login import Ui_Form as Ui_Login
from view.signup import Ui_Form as Ui_Signup
from view.main import Ui_Form as Ui_main
from view.memorize import Ui_Form as Ui_Memorize

from viewmodel.auth_view_model import LoginViewModel, SignUpViewModel
from viewmodel.memorize_view_model import MemorizeViewModel

from model.word import get_words_by_library
from model.user import hash_password

from viewmodel.message import show_popup_message

from controller.config_controller import load_config, save_config
from controller.sync_controller import sync_up_down
from controller.auth_controller import edit_user, logout

from util.lexicon import get_today_study_count, get_total_study_count, get_library_study_count, get_library_total_word_count

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

        self.button_exit = self.memorize_view.findChild(QPushButton, "pushButton_memorize_back")

        self.checkBox_login_devmode = self.login_view.findChild(QCheckBox, "checkBox_login_devmode")
        self.lineEdit_login_server_url = self.login_view.findChild(QLineEdit, "lineEdit_login_server_url")

        # 找到 comboBox_lib
        self.comboBox_lib = self.main_view.findChild(QComboBox, "comboBox_lib")
        # 加载所有库到下拉框
        self.load_libraries_to_combo()

        # 找到 pushButton_main_sync
        self.button_sync = self.main_view.findChild(QPushButton, "pushButton_main_sync")

        # 找到词库界面的元素
        self.table = self.main_view.findChild(QTableView, "tableView")
        self.label_lexicon_username = self.main_view.findChild(QLabel, "label_lexicon_username")
        self.label_lexicon_count_today = self.main_view.findChild(QLabel, "label_lexicon_count_today")
        self.label_lexicon_count_all = self.main_view.findChild(QLabel, "label_lexicon_count_all")
        self.label_lexicon_time_today = self.main_view.findChild(QLabel, "label_lexicon_time_today")
        self.label_lexicon_time_all = self.main_view.findChild(QLabel, "label_lexicon_time_all")
        self.progressBar = self.main_view.findChild(QProgressBar, "progressBar")
        self.label_lexicon_learned = self.main_view.findChild(QLabel, "label_lexicon_learned")
        self.label_lexicon_all = self.main_view.findChild(QLabel, "label_lexicon_all")

        # 找到设置界面的元素
        self.label_settings_username = self.main_view.findChild(QLabel, "label_settings_username")
        self.lineEdit_settings_pwd_old = self.main_view.findChild(QLineEdit, "lineEdit_settings_pwd_old")
        self.lineEdit_settings_pwd_new = self.main_view.findChild(QLineEdit, "lineEdit_settings_pwd_new")
        self.lineEdit_settings_pwd_new_check = self.main_view.findChild(QLineEdit, "lineEdit_settings_pwd_new_check")
        self.button_changePwd = self.main_view.findChild(QPushButton, "pushButton_settings_changePwd")
        self.checkBox_settings_devmode = self.main_view.findChild(QCheckBox, "checkBox_settings_devmode")
        self.lineEdit_settings_server_url = self.main_view.findChild(QLineEdit, "lineEdit_settings_server_url")
        self.button_logout = self.main_view.findChild(QPushButton, "pushButton_logout")

        # 将视图添加到预定义的页面中
        self.gridLayout_login.addWidget(self.login_view)
        self.gridLayout_signup.addWidget(self.signup_view)
        self.gridLayout_main.addWidget(self.main_view)
        self.gridLayout_memorize.addWidget(self.memorize_view)

        # 设置默认显示登录视图
        self.stackedWidget.setCurrentIndex(0)

        # Connect buttons with slot functions
        self.button_exit.clicked.connect(self.exit_memorize_view)

        self.main_ui.pushButton_main_learn.clicked.connect(self.show_learning_view)
        self.main_ui.pushButton_main_revise.clicked.connect(self.show_revise_view)
        self.main_ui.pushButton_main_sync.clicked.connect(self.on_sync_pressed)

        self.main_ui.pushButton_settings_changePwd.clicked.connect(self.change_password)
        self.main_ui.checkBox_settings_devmode.stateChanged.connect(self.toggle_dev_mode)
        self.lineEdit_settings_server_url.returnPressed.connect(self.update_server_url)

        self.button_logout.clicked.connect(self.do_logout)

        self.checkBox_login_devmode.stateChanged.connect(self.toggle_dev_mode)
        self.lineEdit_login_server_url.returnPressed.connect(self.update_server_url_during_login)



        # 动态为按钮添加高斯模糊效果
        self.add_blur_effect_to_buttons()

        # # 初始化词库界面
        # self.render_lexicon_ui()
        self.main_ui.tabWidget.currentChanged.connect(self.render_lexicon_ui)
        self.button_sync.clicked.connect(self.render_lexicon_ui)

        # 初始化设置界面
        self.load_settings()


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

    def exit_memorize_view(self):
        confirm = show_popup_message(
            message="确定退出吗？这会丢失本次背词进度",
            title="你确定吗",
            msg_type="question"
        )
        if confirm:
            self.stackedWidget.setCurrentIndex(2)
        else:
            pass

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
        self.render_lexicon_ui()
        print(f"[INFO] Updated config's lib_id to {lib_id}.")

    def on_sync_pressed(self):
        conf = load_config()
        uid = conf["uid"]
        pwd = conf["password"]
        sync_up_down(uid, pwd)

    def load_words_to_table(self, library_id):
        """加载指定词库的单词到 tableView."""
        words = get_words_by_library(library_id)

        # 按单词字段排序（A-Z）
        words.sort(key=lambda w: w.word.lower())  # 忽略大小写排序

        # 创建 QStandardItemModel，并设置列标签
        model = QStandardItemModel(len(words), 3)  # 行数=单词数，列数=3
        model.setHorizontalHeaderLabels(["单词", "发音", "释义"])

        # 填充数据
        for row, word in enumerate(words):
            model.setItem(row, 0, QStandardItem(word.word))
            model.setItem(row, 1, QStandardItem(word.pronunciation))
            model.setItem(row, 2, QStandardItem(word.definition))

        # 将 model 设置给 tableView
        self.table.setModel(model)

        # 自动调整列宽以适应内容
        self.table.resizeColumnsToContents()

    def render_progress_bar(self, user_id, library_id):
        if user_id == -1 or library_id == -1:
            self.progressBar.setValue(0)
            self.label_lexicon_learned.setText("learned")
            self.label_lexicon_all.setText("total")

        """渲染 progressBar 的进度"""
        learned_count = get_library_study_count(user_id, library_id)
        total_count = get_library_total_word_count(library_id)

        if total_count > 0:
            progress = (learned_count / total_count) * 100
        else:
            progress = 0

        self.progressBar.setValue(progress)
        self.label_lexicon_learned.setText(str(learned_count))
        self.label_lexicon_all.setText(str(total_count))

    def render_lexicon_ui(self):
        conf = load_config()
        if "uid" not in conf:
            print("[DEBUG] No uid stored.")
            self.label_lexicon_count_today.setText(f"## Count")
            self.label_lexicon_count_all.setText(f"## Count")
            self.label_lexicon_username.setText(f"### username")
            self.render_progress_bar(-1, -1)
            return

        lib_id = conf["lib_id"]
        uid = conf["uid"]
        username = conf["username"]
        self.load_words_to_table(lib_id)

        # 计算今日学习/复习词数
        today_count = get_today_study_count(uid, lib_id)
        self.label_lexicon_count_today.setText(f"## {today_count}")

        # 计算累计学习的词数
        total_count = get_total_study_count(uid)
        self.label_lexicon_count_all.setText(f"## {total_count}")

        # 渲染进度条
        self.render_progress_bar(uid, lib_id)

        self.label_lexicon_username.setText(f"### {username}")



    def change_password(self):
        """更改用户密码"""
        old_password = hash_password(self.lineEdit_settings_pwd_old.text())
        new_password = hash_password(self.lineEdit_settings_pwd_new.text())
        confirm_password = hash_password(self.lineEdit_settings_pwd_new_check.text())
        conf = load_config()
        username = conf["username"]

        if not old_password or not new_password or not confirm_password:
            show_popup_message("错误", "所有字段都必须填写", "error")
            return

        if new_password != confirm_password:
            show_popup_message("错误", "新密码和确认密码不一致", "error")
            return

        # 调用后端接口或本地服务来更改密码（示例中为假设）
        result, message = edit_user(username, old_password, new_password)
        if result:
            show_popup_message("成功", "密码修改成功")
            self.lineEdit_settings_pwd_old.clear()
            self.lineEdit_settings_pwd_new.clear()
            self.lineEdit_settings_pwd_new_check.clear()
        else:
            show_popup_message("错误", message)

    def toggle_dev_mode(self, state):
        conf = load_config()
        conf["devmode"] = bool(state)
        # self.lineEdit_settings_server_url.readOnly
        save_config(conf)
        self.lineEdit_settings_server_url.setReadOnly(not state)
        self.lineEdit_login_server_url.setReadOnly(not state)

    def update_server_url(self):
        url = self.lineEdit_settings_server_url.text()
        if not url:
            conf = load_config()
            conf["SERVER_URL"] = "http://127.0.0.1:5000/api"
            save_config(conf)
        else:
            conf = load_config()
            conf["SERVER_URL"] = url
            save_config(conf)

    def update_server_url_during_login(self):
        url = self.lineEdit_login_server_url.text()
        if not url:
            conf = load_config()
            conf["SERVER_URL"] = "http://127.0.0.1:5000/api"
            save_config(conf)
        else:
            conf = load_config()
            conf["SERVER_URL"] = url
            save_config(conf)

    def load_settings(self):
        conf = load_config()
        devmode = conf.get("devmode", False)
        server_url = conf.get("SERVER_URL", "http://127.0.0.1:5000")

        self.label_settings_username.setText(f"Welcome Back, {conf.get('username', 'username')}")


        # 设置 devmode 的状态
        self.checkBox_settings_devmode.setChecked(devmode)
        self.checkBox_login_devmode.setChecked(devmode)

        # 设置 server_url 的值
        if conf["SERVER_URL"] != "http://127.0.0.1:5000/api":
            self.lineEdit_settings_server_url.setText(server_url)
            self.lineEdit_login_server_url.setText(server_url)
        else:
            self.lineEdit_settings_server_url.clear()
            self.lineEdit_login_server_url.clear()

        # 如果 devmode 为 False，则设置为只读
        self.lineEdit_settings_server_url.setReadOnly(not devmode)
        self.lineEdit_login_server_url.setReadOnly(not devmode)

    def do_logout(self):
        logout()
        self.stackedWidget.setCurrentIndex(0)

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