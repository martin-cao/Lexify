from PySide6.QtWidgets import QWidget, QStackedWidget, QMainWindow, QGridLayout, QGraphicsBlurEffect

from view.login import Ui_Form as Ui_Login
from view.signup import Ui_Form as Ui_Signup
from view.main import Ui_Form as Ui_main

from viewmodel.auth_view_model import LoginViewModel, SignUpViewModel

from database.database import DatabaseConnection


class MainViewModel:
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        # 获取 stackedWidget 用来切换视图
        self.stackedWidget = main_window.findChild(QStackedWidget, "stackedWidget")

        # 获取预定义的页面
        self.gridLayout_login = self.main_window.findChild(QGridLayout, "gridLayout_login")
        self.gridLayout_signup = self.main_window.findChild(QGridLayout, "gridLayout_signup")
        self.gridLayout_main = self.main_window.findChild(QGridLayout, "gridLayout_main")

        # 设置登录和注册视图
        self.login_view = QWidget()
        self.signup_view = QWidget()
        self.main_view = QWidget()

        # 设置对应的 UI
        self.login_ui = Ui_Login()
        self.login_ui.setupUi(self.login_view)

        self.signup_ui = Ui_Signup()
        self.signup_ui.setupUi(self.signup_view)

        self.main_ui = Ui_main()
        self.main_ui.setupUi(self.main_view)

        # 初始化登录和注册的 ViewModel
        self.login_view_model = LoginViewModel(self.login_view, main_window)
        self.signup_view_model = SignUpViewModel(self.signup_view, main_window)

        # 将视图添加到预定义的页面中
        self.gridLayout_login.addWidget(self.login_view)
        self.gridLayout_signup.addWidget(self.signup_view)
        self.gridLayout_main.addWidget(self.main_view)

        # 设置默认显示登录视图
        self.stackedWidget.setCurrentIndex(0)

        # 连接按钮：切换到注册界面
        # self.login_view_model.button_signup.clicked.connect(self.show_signup_view)

        # 动态为按钮添加高斯模糊效果
        self.add_blur_effect_to_buttons()

    def show_signup_view(self):
        """切换到注册页面"""
        self.stackedWidget.setCurrentWidget(self.signup_view)

    def show_login_view(self):
        """切换到登录页面"""
        self.stackedWidget.setCurrentWidget(self.login_view)

    def add_blur_effect_to_buttons(self):
        """为所有按钮添加高斯模糊效果"""
        buttons = [
            self.login_ui.pushButton_login_login,
            self.login_ui.pushButton_login_signup,
            self.signup_ui.pushButton_signup_signup,
            self.signup_ui.pushButton_signup_cancel
        ]

        for button in buttons:
            if button:  # 确保按钮存在
                blur_effect = QGraphicsBlurEffect()
                blur_effect.setBlurRadius(10)  # 设置模糊半径
                button.setGraphicsEffect(blur_effect)