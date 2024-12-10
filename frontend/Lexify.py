import sys
import time

from PySide6.QtCore import Qt, QDate, QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtUiTools import QUiLoader
from requests import session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from view.MainWindow import Ui_MainWindow

from view.login import Ui_Form as Ui_loginView
from view.signup import Ui_Form as Ui_signupView

from database.database import session

# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
# Session = sessionmaker(bind=engine)
# session = Session()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize SQLAlchemy session
        self.session = session

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Lexify")

        self.loginView = QWidget()
        self.loginView_ui = Ui_loginView()
        self.loginView_ui.setupUi(self.loginView)

        self.ui.gridLayout_login.addWidget(self.loginView)
        self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":

    app = QApplication([])


    # if sys.platform == "darwin": # macOS
    #     app.setStyle("macintosh")
    # elif sys.platform == "win32": # Windows
    #     app.setStyle("windowsvista")

    # db_connection = DatabaseConnection()

    window = MainWindow()
    window.show()
    app.exec()