import sys
import time

from PySide6.QtCore import Qt, QDate, QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


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