# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 622)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_login_username = QLineEdit(Form)
        self.lineEdit_login_username.setObjectName(u"lineEdit_login_username")
        self.lineEdit_login_username.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_login_username)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_login_pwd = QLineEdit(Form)
        self.lineEdit_login_pwd.setObjectName(u"lineEdit_login_pwd")
        self.lineEdit_login_pwd.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_login_pwd.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_login_pwd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_login_login = QPushButton(Form)
        self.pushButton_login_login.setObjectName(u"pushButton_login_login")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login_login.setSizePolicy(sizePolicy)
        self.pushButton_login_login.setMinimumSize(QSize(80, 0))
        self.pushButton_login_login.setMaximumSize(QSize(160, 16777215))
        self.pushButton_login_login.setAutoFillBackground(False)
        self.pushButton_login_login.setStyleSheet(u"alignment=Qt.AlignCenter")
        self.pushButton_login_login.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_login_login, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(80, -1, 80, -1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.pushButton_login_signup = QPushButton(Form)
        self.pushButton_login_signup.setObjectName(u"pushButton_login_signup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_login_signup.sizePolicy().hasHeightForWidth())
        self.pushButton_login_signup.setSizePolicy(sizePolicy2)
        self.pushButton_login_signup.setMinimumSize(QSize(80, 0))
        self.pushButton_login_signup.setMaximumSize(QSize(80, 16777215))
        self.pushButton_login_signup.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_login_signup)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(80, -1, 80, -1)
        self.checkBox_login_devmode = QCheckBox(Form)
        self.checkBox_login_devmode.setObjectName(u"checkBox_login_devmode")

        self.horizontalLayout_4.addWidget(self.checkBox_login_devmode)

        self.lineEdit_login_server_url = QLineEdit(Form)
        self.lineEdit_login_server_url.setObjectName(u"lineEdit_login_server_url")
        self.lineEdit_login_server_url.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_login_server_url.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout_4.addWidget(self.lineEdit_login_server_url)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Welcome to Lexify</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.pushButton_login_login.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u65b0\u7528\u6237\uff1f", None))
        self.pushButton_login_signup.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.checkBox_login_devmode.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u670d\u52a1\u5668", None))
    # retranslateUi

