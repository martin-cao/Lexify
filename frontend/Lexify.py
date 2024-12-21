import sys
import time

from PySide6.QtCore import Qt, QDate, QFile
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPalette

from config import Config
from database.database import DatabaseConnection

from view.MainWindow import Ui_MainWindow
from viewmodel.main_view_model import MainViewModel

class MainWindow(QMainWindow):
    def __init__(self, db_session):
        super(MainWindow, self).__init__()

        # Initialize SQLAlchemy session
        self.session = db_session

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Lexify")

if __name__ == "__main__":

    app = QApplication([])

    # with open("style.qss", "r", encoding="utf-8") as f:
    #     qss = f.read()
    #
    # app.setStyleSheet(qss)

    # if sys.platform == "darwin": # macOS
    #     app.setStyle("macintosh")
    # elif sys.platform == "win32": # Windows
    #     app.setStyle("windowsvista")

    db_connection = DatabaseConnection()
    session = db_connection.get_session()

    window = MainWindow(session)

    main_window_view_model = MainViewModel(window)

    window.show()
    app.exec()