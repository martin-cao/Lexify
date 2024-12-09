# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_signup_username = QLineEdit(Form)
        self.lineEdit_signup_username.setObjectName(u"lineEdit_signup_username")
        self.lineEdit_signup_username.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_signup_username)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_signup_pwd = QLineEdit(Form)
        self.lineEdit_signup_pwd.setObjectName(u"lineEdit_signup_pwd")
        self.lineEdit_signup_pwd.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_signup_pwd.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_signup_pwd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(200, 16777215))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_signup_pwd_check = QLineEdit(Form)
        self.lineEdit_signup_pwd_check.setObjectName(u"lineEdit_signup_pwd_check")
        self.lineEdit_signup_pwd_check.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_signup_pwd_check.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_4.addWidget(self.lineEdit_signup_pwd_check)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_signup_signup = QPushButton(Form)
        self.pushButton_signup_signup.setObjectName(u"pushButton_signup_signup")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_signup_signup.sizePolicy().hasHeightForWidth())
        self.pushButton_signup_signup.setSizePolicy(sizePolicy)
        self.pushButton_signup_signup.setMinimumSize(QSize(80, 0))
        self.pushButton_signup_signup.setMaximumSize(QSize(160, 16777215))
        self.pushButton_signup_signup.setAutoFillBackground(False)
        self.pushButton_signup_signup.setStyleSheet(u"alignment=Qt.AlignCenter")
        self.pushButton_signup_signup.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_signup_signup, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.pushButton_signup_signup.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
    # retranslateUi

