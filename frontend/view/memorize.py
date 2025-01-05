# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'memorize.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(932, 746)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_memorize_back = QPushButton(Form)
        self.pushButton_memorize_back.setObjectName(u"pushButton_memorize_back")
        self.pushButton_memorize_back.setMinimumSize(QSize(56, 36))
        self.pushButton_memorize_back.setMaximumSize(QSize(56, 36))

        self.horizontalLayout.addWidget(self.pushButton_memorize_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(72, -1, 72, -1)
        self.label_memorize_word = QLabel(Form)
        self.label_memorize_word.setObjectName(u"label_memorize_word")
        self.label_memorize_word.setMinimumSize(QSize(240, 56))
        self.label_memorize_word.setMaximumSize(QSize(16777215, 56))
        self.label_memorize_word.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_memorize_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_memorize_word)

        self.label_memorize_pronunciation = QLabel(Form)
        self.label_memorize_pronunciation.setObjectName(u"label_memorize_pronunciation")
        self.label_memorize_pronunciation.setMinimumSize(QSize(240, 36))
        self.label_memorize_pronunciation.setMaximumSize(QSize(16777215, 36))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label_memorize_pronunciation.setFont(font)
        self.label_memorize_pronunciation.setTextFormat(Qt.TextFormat.AutoText)
        self.label_memorize_pronunciation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_memorize_pronunciation)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 154, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(48, -1, 48, -1)
        self.pushButton_memorize_option_1 = QPushButton(Form)
        self.pushButton_memorize_option_1.setObjectName(u"pushButton_memorize_option_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_memorize_option_1.sizePolicy().hasHeightForWidth())
        self.pushButton_memorize_option_1.setSizePolicy(sizePolicy)
        self.pushButton_memorize_option_1.setMinimumSize(QSize(240, 48))
        self.pushButton_memorize_option_1.setMaximumSize(QSize(16777215, 48))

        self.verticalLayout.addWidget(self.pushButton_memorize_option_1)

        self.pushButton_memorize_option_2 = QPushButton(Form)
        self.pushButton_memorize_option_2.setObjectName(u"pushButton_memorize_option_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_memorize_option_2.sizePolicy().hasHeightForWidth())
        self.pushButton_memorize_option_2.setSizePolicy(sizePolicy1)
        self.pushButton_memorize_option_2.setMinimumSize(QSize(240, 48))
        self.pushButton_memorize_option_2.setMaximumSize(QSize(16777215, 48))

        self.verticalLayout.addWidget(self.pushButton_memorize_option_2)

        self.pushButton_memorize_option_4 = QPushButton(Form)
        self.pushButton_memorize_option_4.setObjectName(u"pushButton_memorize_option_4")
        sizePolicy.setHeightForWidth(self.pushButton_memorize_option_4.sizePolicy().hasHeightForWidth())
        self.pushButton_memorize_option_4.setSizePolicy(sizePolicy)
        self.pushButton_memorize_option_4.setMinimumSize(QSize(240, 48))
        self.pushButton_memorize_option_4.setMaximumSize(QSize(16777215, 48))

        self.verticalLayout.addWidget(self.pushButton_memorize_option_4)

        self.pushButton_memorize_option_3 = QPushButton(Form)
        self.pushButton_memorize_option_3.setObjectName(u"pushButton_memorize_option_3")
        sizePolicy.setHeightForWidth(self.pushButton_memorize_option_3.sizePolicy().hasHeightForWidth())
        self.pushButton_memorize_option_3.setSizePolicy(sizePolicy)
        self.pushButton_memorize_option_3.setMinimumSize(QSize(240, 48))
        self.pushButton_memorize_option_3.setMaximumSize(QSize(16777215, 48))

        self.verticalLayout.addWidget(self.pushButton_memorize_option_3)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 154, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_memorize_forgot = QPushButton(Form)
        self.pushButton_memorize_forgot.setObjectName(u"pushButton_memorize_forgot")
        self.pushButton_memorize_forgot.setMinimumSize(QSize(120, 36))
        self.pushButton_memorize_forgot.setMaximumSize(QSize(120, 36))

        self.horizontalLayout_2.addWidget(self.pushButton_memorize_forgot)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_memorize_back.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_memorize_word.setText(QCoreApplication.translate("Form", u"# word", None))
        self.label_memorize_pronunciation.setText(QCoreApplication.translate("Form", u"pronunciation", None))
        self.pushButton_memorize_option_1.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_memorize_option_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_memorize_option_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_memorize_option_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_memorize_forgot.setText(QCoreApplication.translate("Form", u"\u770b\u7b54\u6848", None))
    # retranslateUi

