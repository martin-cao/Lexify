# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"/* \u5168\u5c40\u57fa\u7840\u8bbe\u7f6e */\n"
"\n"
"QMainWindow {\n"
"    background-image: url(:/pics/assets/background.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"}\n"
"\n"
"QWidget {\n"
"    color: #212121;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"}\n"
"\n"
"/* \u63d0\u793a\u6587\u672c\u548c\u4e0d\u53ef\u7528\u72b6\u6001 */\n"
"QWidget:disabled {\n"
"    color: #9E9E9E;\n"
"}\n"
"\n"
"/* \u6309\u94ae - \u6241\u5e73\u3001\u5706\u89d2\u3001\u5f3a\u8c03\u4e3b\u8272\u3001\u60ac\u6d6e\u53d8\u8272 */\n"
"QPushButton {\n"
"    background: rgba(98, 0, 238, 0.7); /* \u8bbe\u7f6e\u4e3a 70% \u4e0d\u900f\u660e */\n"
"    color: #FFFFFF;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"    border-radius: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(55, 0, 179, 0.7); /* \u52a0\u6df1\u4e3b\u8272\uff0c\u4fdd\u6301 70% \u4e0d\u900f\u660e */\n"
"}\n"
"QPushButton:pressed {\n"
"    background: r"
                        "gba(49, 27, 146, 0.7); /* \u66f4\u6df1\u4e00\u5c42\uff0c\u4fdd\u6301 70% \u4e0d\u900f\u660e */\n"
"}\n"
"QPushButton:disabled {\n"
"    background: rgba(189, 189, 189, 0.7); /* \u7981\u7528\u72b6\u6001\uff0c\u4fdd\u6301 70% \u4e0d\u900f\u660e */\n"
"    color: rgba(224, 224, 224, 0.7);\n"
"}\n"
"\n"
"/* \u6b21\u7ea7\u5f3a\u8c03\u8272\u6309\u94ae\uff08\u4e0d\u900f\u660e\u5ea6\u8bbe\u7f6e\u540c\u6837\u9002\u7528\uff09 */\n"
"QPushButton.secondary {\n"
"    background: rgba(3, 218, 198, 0.7);\n"
"    color: #000000;\n"
"}\n"
"QPushButton.secondary:hover {\n"
"    background: rgba(1, 179, 165, 0.7);\n"
"}\n"
"QPushButton.secondary:pressed {\n"
"    background: rgba(1, 140, 132, 0.7);\n"
"}\n"
"\n"
"/* \u6b21\u7ea7\u5f3a\u8c03\u8272\u6309\u94ae\uff08\u53ef\u81ea\u884c\u4f7f\u7528\uff0c\u6bd4\u5982\u5728\u7279\u5b9a\u529f\u80fd\u6309\u94ae\u4e0a\uff09 */\n"
"QPushButton.secondary {\n"
"    background: #03DAC6;\n"
"    color: #000000;\n"
"}\n"
"QPushButton.secondary:hover {\n"
"    background: #01B3A5;\n"
"}\n"
"QPus"
                        "hButton.secondary:pressed {\n"
"    background: #018C84;\n"
"}\n"
"\n"
"/* \u8f93\u5165\u6846\u3001\u4e0b\u62c9\u6846 - \u7b80\u6d01\u5e95\u7ebf */\n"
"QLineEdit, QComboBox {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 2px solid #9E9E9E;\n"
"    padding: 4px;\n"
"    selection-background-color: #6200EE;\n"
"    selection-color: #FFFFFF;\n"
"    color: #FFFFFF;\n"
"}\n"
"QLineEdit:focus, QComboBox:focus {\n"
"    border-bottom: 2px solid #6200EE;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u5217\u8868\u7684\u5f39\u51fa\u83dc\u5355 */\n"
"\n"
"\n"
"/* \u5de5\u5177\u680f\u548c\u83dc\u5355\u680f */\n"
"QToolBar {\n"
"    background: #F5F5F5;\n"
"    border: none;\n"
"    spacing: 8px;\n"
"}\n"
"QMenuBar {\n"
"    background: #F5F5F5;\n"
"    border-bottom: 1px solid #E0E0E0;\n"
"}\n"
"QMenuBar::item {\n"
"    padding: 8px 12px;\n"
"    background: transparent;\n"
"}\n"
"QMenuBar::item:selected {\n"
"    background: #E0E0E0;\n"
"    color: #000000;\n"
"}\n"
"QMenu {\n"
"    background: #FFFFFF;"
                        "\n"
"    border: 1px solid #E0E0E0;\n"
"}\n"
"QMenu::item {\n"
"    padding: 8px 16px;\n"
"}\n"
"QMenu::item:selected {\n"
"    background: #6200EE;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\uff08Tab\uff09\u63a7\u4ef6 */\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"}\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    padding: 8px 16px;\n"
"    margin: 0 4px;\n"
"    border-bottom: 2px solid transparent;\n"
"    color: #FFFFFF;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border-bottom: 2px solid #6200EE;\n"
"    font-weight: 500;\n"
"    color: #6200EE;\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background: rgba(224, 224, 224, 0.3);\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761 - \u6241\u5e73\u3001\u7ec6\u6761\u6837\u5f0f */\n"
"QScrollBar:horizontal {\n"
"    background: #F5F5F5;\n"
"    height: 8px;\n"
"    margin: 0 16px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #9E9E9E;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background:"
                        " #F5F5F5;\n"
"    width: 8px;\n"
"    margin: 16px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #9E9E9E;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u53bb\u6389 QScrollBar \u7684\u4e0a\u4e0b\u63a7\u5236\u6309\u94ae */\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"    height: 0px; /* \u5782\u76f4\u6eda\u52a8\u6761\u4e0a\u4e0b\u6309\u94ae\u7684\u9ad8\u5ea6\u8bbe\u4e3a 0 */\n"
"    width: 0px;  /* \u6c34\u5e73\u6eda\u52a8\u6761\u5de6\u53f3\u6309\u94ae\u7684\u5bbd\u5ea6\u8bbe\u4e3a 0 */\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u9632\u6b62\u4e0a\u4e0b\u63a7\u5236\u6309\u94ae\u7559\u4e0b\u7a7a\u9699 */\n"
"QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal, QScrollBar::add-line:horizontal {\n"
"    margin: 0;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u6587\u672c */\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u63d0\u793a\u6846\uff08ToolTip\uff09 */\n"
"QToolT"
                        "ip {\n"
"    background: #212121;\n"
"    color: #FFFFFF;\n"
"    padding: 4px 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u5217\u8868\u548c\u6811\u89c6\u56fe */\n"
"QListView, QTreeView {\n"
"    border: none;\n"
"    selection-background-color: #E0E0E0;\n"
"}\n"
"QListView::item:hover, QTreeView::item:hover {\n"
"    background: #E0E0E0;\n"
"}\n"
"QListView::item:selected, QTreeView::item:selected {\n"
"    background: #6200EE;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u8fdb\u5ea6\u6761 */\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 4px;\n"
"    background: #F5F5F5;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: #6200EE;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.gridLayout_2 = QGridLayout(self.login)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_login = QGridLayout()
        self.gridLayout_login.setObjectName(u"gridLayout_login")

        self.gridLayout_2.addLayout(self.gridLayout_login, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.login)
        self.signup = QWidget()
        self.signup.setObjectName(u"signup")
        self.gridLayout_3 = QGridLayout(self.signup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_signup = QGridLayout()
        self.gridLayout_signup.setObjectName(u"gridLayout_signup")

        self.gridLayout_3.addLayout(self.gridLayout_signup, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.signup)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.gridLayout_4 = QGridLayout(self.main)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_main = QGridLayout()
        self.gridLayout_main.setObjectName(u"gridLayout_main")

        self.gridLayout_4.addLayout(self.gridLayout_main, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.main)
        self.memorize = QWidget()
        self.memorize.setObjectName(u"memorize")
        self.gridLayout_5 = QGridLayout(self.memorize)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_memorize = QGridLayout()
        self.gridLayout_memorize.setObjectName(u"gridLayout_memorize")

        self.gridLayout_5.addLayout(self.gridLayout_memorize, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.memorize)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

