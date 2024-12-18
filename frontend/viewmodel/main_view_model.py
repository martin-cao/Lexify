from PySide6.QtWidgets import QWidget, QStackedWidget, QMainWindow
from view.login import Ui_Form as Ui_Login
from view.signup import Ui_Form as Ui_Signup
from view.MainWindow import Ui_MainWindow
from viewmodel.auth_view_model import LoginViewModel, SignUpViewModel
from database.database import DatabaseConnection


class MainViewModel:
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        # 获取 stackedWidget 用来切换视图
        self.stacked_widget = main_window.ui.stackedWidget

        # 设置登录和注册视图
        self.login_view = QWidget()
        self.signup_view = QWidget()

        # 设置对应的 UI
        self.login_ui = Ui_Login()
        self.login_ui.setupUi(self.login_view)

        self.signup_ui = Ui_Signup()
        self.signup_ui.setupUi(self.signup_view)

        # 初始化登录和注册的 ViewModel
        self.login_view_model = LoginViewModel(self.login_view, main_window)
        self.signup_view_model = SignUpViewModel(self.signup_view, main_window)

        # 将登录视图和注册视图添加到 stackedWidget 中
        self.stacked_widget.addWidget(self.login_view)
        self.stacked_widget.addWidget(self.signup_view)

        # 设置默认显示登录视图
        self.stacked_widget.setCurrentWidget(self.login_view)

        # 连接按钮：切换到注册界面
        self.login_view_model.button_signup.clicked.connect(self.show_signup_view)

    def show_signup_view(self):
        """切换到注册页面"""
        self.stacked_widget.setCurrentWidget(self.signup_view)

    def show_login_view(self):
        """切换到登录页面"""
        self.stacked_widget.setCurrentWidget(self.login_view)