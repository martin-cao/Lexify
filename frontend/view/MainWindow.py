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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

