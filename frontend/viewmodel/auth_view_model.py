from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, QMainWindow, QStackedWidget
from hashlib import sha256

import controller.auth_controller as AuthController
from view.MainWindow import Ui_MainWindow
from view.login import Ui_Form as Ui_Login
from view.signup import Ui_Form as Ui_Signup


class LoginViewModel:
    def __init__(self, view: QWidget, main_window: QMainWindow):
        self.login_view = view
        self.main_window = main_window
        self.stackedWidget = main_window.findChild(QStackedWidget, "stackedWidget")

        self.lineEdit_username = view.findChild(QLineEdit, "lineEdit_login_username")
        self.lineEdit_password = view.findChild(QLineEdit, "lineEdit_login_pwd")
        self.button_login = view.findChild(QPushButton, "pushButton_login_login")
        self.button_signup = view.findChild(QPushButton, "pushButton_login_signup")

        # Connect buttons with slot functions
        self.button_login.clicked.connect(self.handle_login)
        self.button_signup.clicked.connect(self.handle_signup)

    def handle_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # Encode the inputed password
        password_sha256 = sha256(password.encode()).hexdigest()

        success, msg = AuthController.login(username, password_sha256)

        self.show_message(success, msg, "登陆")

        if success:
            self.stackedWidget.setCurrentIndex(2)

    def handle_signup(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_message(self, success, message, action):
        # 根据登录或注册的结果弹出提示框
        msg = QMessageBox(self.login_view)
        msg.setIcon(QMessageBox.Information if success else QMessageBox.Critical)
        msg.setText(f"{action} {'成功' if success else '失败'}")
        msg.setInformativeText(message)
        msg.setWindowTitle(f"{action} 结果")
        msg.setStandardButtons(QMessageBox.Ok)

        # 如果点击Done按钮，切换页面
        button = msg.exec()
        if button == QMessageBox.Ok:
            pass  # 这里不需要做额外的处理，页面已经在 handle_login 中切换


class SignUpViewModel:
    def __init__(self, view: QWidget, main_window: QMainWindow):
        self.sign_up_view = view
        self.main_window = main_window
        self.stackedWidget = main_window.findChild(QStackedWidget, "stackedWidget")

        self.lineEdit_username = view.findChild(QLineEdit, "lineEdit_signup_username")
        self.lineEdit_password = view.findChild(QLineEdit, "lineEdit_signup_pwd")
        self.lineEdit_password_check = view.findChild(QLineEdit, "lineEdit_signup_pwd_check")
        self.button_signup = view.findChild(QPushButton, "pushButton_signup_signup")
        self.button_cancel = view.findChild(QPushButton, "pushButton_signup_cancel")

        # Connect button with slot function
        self.button_signup.clicked.connect(self.handle_signup)
        self.button_cancel.clicked.connect(self.handle_cancel)

    def handle_signup(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        password_check = self.lineEdit_password_check.text()

        # Encode the inputed password
        password_sha256 = sha256(password.encode()).hexdigest()
        password_check_sha256 = sha256(password_check.encode()).hexdigest()

        if password_sha256 != password_check_sha256:
            # 弹出密码不一致的提示框
            msg = QMessageBox(self.sign_up_view)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("密码不一致")
            msg.setInformativeText("请确保两次输入的密码相同")
            msg.setWindowTitle("注册失败")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        success, msg = AuthController.register(username, password_sha256)

        self.show_message(success, msg, "注册")

        if success:
            self.stackedWidget.setCurrentIndex(2)

    def handle_cancel(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_message(self, success, message, action):
        # 根据注册结果弹出提示框
        msg = QMessageBox(self.sign_up_view)
        msg.setIcon(QMessageBox.Information if success else QMessageBox.Critical)
        msg.setText(f"{action} {'成功' if success else '失败'}")
        msg.setInformativeText(message)
        msg.setWindowTitle(f"{action} 结果")
        msg.setStandardButtons(QMessageBox.Ok)

        # 如果点击Done按钮，切换页面
        button = msg.exec()
        if button == QMessageBox.Ok:
            pass
