# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QVBoxLayout, QWidget)
import assets_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 588)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_main = QWidget()
        self.tab_main.setObjectName(u"tab_main")
        self.gridLayout_3 = QGridLayout(self.tab_main)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(24)
        self.gridLayout.setContentsMargins(24, 24, 24, 24)
        self.label_main_date = QLabel(self.tab_main)
        self.label_main_date.setObjectName(u"label_main_date")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_main_date.sizePolicy().hasHeightForWidth())
        self.label_main_date.setSizePolicy(sizePolicy)
        self.label_main_date.setMinimumSize(QSize(304, 48))
        self.label_main_date.setMaximumSize(QSize(16777215, 48))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_main_date.setFont(font)
        self.label_main_date.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_main_date.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_main_date, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(48)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_main_learn = QPushButton(self.tab_main)
        self.pushButton_main_learn.setObjectName(u"pushButton_main_learn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_main_learn.sizePolicy().hasHeightForWidth())
        self.pushButton_main_learn.setSizePolicy(sizePolicy1)
        self.pushButton_main_learn.setMinimumSize(QSize(128, 48))
        self.pushButton_main_learn.setMaximumSize(QSize(16777215, 48))

        self.horizontalLayout.addWidget(self.pushButton_main_learn)

        self.pushButton_main_revise = QPushButton(self.tab_main)
        self.pushButton_main_revise.setObjectName(u"pushButton_main_revise")
        sizePolicy1.setHeightForWidth(self.pushButton_main_revise.sizePolicy().hasHeightForWidth())
        self.pushButton_main_revise.setSizePolicy(sizePolicy1)
        self.pushButton_main_revise.setMinimumSize(QSize(128, 48))
        self.pushButton_main_revise.setMaximumSize(QSize(16777215, 48))

        self.horizontalLayout.addWidget(self.pushButton_main_revise)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_main_sync = QPushButton(self.tab_main)
        self.pushButton_main_sync.setObjectName(u"pushButton_main_sync")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_main_sync.sizePolicy().hasHeightForWidth())
        self.pushButton_main_sync.setSizePolicy(sizePolicy2)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing))
        self.pushButton_main_sync.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_main_sync)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_main, "")
        self.tab_lexicons = QWidget()
        self.tab_lexicons.setObjectName(u"tab_lexicons")
        self.gridLayout_9 = QGridLayout(self.tab_lexicons)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(24)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.tab_lexicons)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(128, 0))
        self.label_9.setMaximumSize(QSize(128, 16777215))
        self.label_9.setTextFormat(Qt.TextFormat.MarkdownText)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.label_lexicon_username = QLabel(self.tab_lexicons)
        self.label_lexicon_username.setObjectName(u"label_lexicon_username")
        self.label_lexicon_username.setMinimumSize(QSize(128, 0))
        self.label_lexicon_username.setMaximumSize(QSize(128, 16777215))
        self.label_lexicon_username.setTextFormat(Qt.TextFormat.MarkdownText)

        self.horizontalLayout_9.addWidget(self.label_lexicon_username)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_lexicon_time_all = QLabel(self.tab_lexicons)
        self.label_lexicon_time_all.setObjectName(u"label_lexicon_time_all")
        sizePolicy.setHeightForWidth(self.label_lexicon_time_all.sizePolicy().hasHeightForWidth())
        self.label_lexicon_time_all.setSizePolicy(sizePolicy)
        self.label_lexicon_time_all.setMinimumSize(QSize(128, 36))
        self.label_lexicon_time_all.setMaximumSize(QSize(128, 36))
        self.label_lexicon_time_all.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_8.addWidget(self.label_lexicon_time_all, 3, 1, 1, 1)

        self.label_lexicon_count_all = QLabel(self.tab_lexicons)
        self.label_lexicon_count_all.setObjectName(u"label_lexicon_count_all")
        sizePolicy.setHeightForWidth(self.label_lexicon_count_all.sizePolicy().hasHeightForWidth())
        self.label_lexicon_count_all.setSizePolicy(sizePolicy)
        self.label_lexicon_count_all.setMinimumSize(QSize(128, 36))
        self.label_lexicon_count_all.setMaximumSize(QSize(128, 36))
        self.label_lexicon_count_all.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_8.addWidget(self.label_lexicon_count_all, 3, 0, 1, 1)

        self.label_20 = QLabel(self.tab_lexicons)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(128, 36))
        self.label_20.setMaximumSize(QSize(128, 36))
        self.label_20.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_8.addWidget(self.label_20, 2, 1, 1, 1)

        self.label_lexicon_time_today = QLabel(self.tab_lexicons)
        self.label_lexicon_time_today.setObjectName(u"label_lexicon_time_today")
        sizePolicy.setHeightForWidth(self.label_lexicon_time_today.sizePolicy().hasHeightForWidth())
        self.label_lexicon_time_today.setSizePolicy(sizePolicy)
        self.label_lexicon_time_today.setMinimumSize(QSize(128, 36))
        self.label_lexicon_time_today.setMaximumSize(QSize(128, 36))
        self.label_lexicon_time_today.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_8.addWidget(self.label_lexicon_time_today, 1, 1, 1, 1)

        self.label_lexicon_count_today = QLabel(self.tab_lexicons)
        self.label_lexicon_count_today.setObjectName(u"label_lexicon_count_today")
        sizePolicy.setHeightForWidth(self.label_lexicon_count_today.sizePolicy().hasHeightForWidth())
        self.label_lexicon_count_today.setSizePolicy(sizePolicy)
        self.label_lexicon_count_today.setMinimumSize(QSize(128, 36))
        self.label_lexicon_count_today.setMaximumSize(QSize(128, 36))
        self.label_lexicon_count_today.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_8.addWidget(self.label_lexicon_count_today, 1, 0, 1, 1)

        self.label_19 = QLabel(self.tab_lexicons)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(128, 36))
        self.label_19.setMaximumSize(QSize(128, 36))
        self.label_19.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_8.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_18 = QLabel(self.tab_lexicons)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(128, 36))
        self.label_18.setMaximumSize(QSize(128, 36))
        self.label_18.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_8.addWidget(self.label_18, 0, 1, 1, 1)

        self.label_10 = QLabel(self.tab_lexicons)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(128, 36))
        self.label_10.setMaximumSize(QSize(128, 36))
        self.label_10.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_8)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.progressBar = QProgressBar(self.tab_lexicons)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(256, 0))
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.tab_lexicons)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(40, 0))
        self.label_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label_lexicon_learned = QLabel(self.tab_lexicons)
        self.label_lexicon_learned.setObjectName(u"label_lexicon_learned")
        sizePolicy3.setHeightForWidth(self.label_lexicon_learned.sizePolicy().hasHeightForWidth())
        self.label_lexicon_learned.setSizePolicy(sizePolicy3)
        self.label_lexicon_learned.setMinimumSize(QSize(64, 0))
        self.label_lexicon_learned.setMaximumSize(QSize(64, 16777215))

        self.horizontalLayout_5.addWidget(self.label_lexicon_learned)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.tab_lexicons)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(40, 0))
        self.label_3.setMaximumSize(QSize(40, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_lexicon_all = QLabel(self.tab_lexicons)
        self.label_lexicon_all.setObjectName(u"label_lexicon_all")
        sizePolicy3.setHeightForWidth(self.label_lexicon_all.sizePolicy().hasHeightForWidth())
        self.label_lexicon_all.setSizePolicy(sizePolicy3)
        self.label_lexicon_all.setMinimumSize(QSize(64, 0))
        self.label_lexicon_all.setMaximumSize(QSize(64, 16777215))
        self.label_lexicon_all.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_lexicon_all)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.gridLayout_9.addLayout(self.verticalLayout_7, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.tab_lexicons)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(128, 36))
        self.label.setMaximumSize(QSize(16777215, 36))
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)

        self.verticalLayout.addWidget(self.label)

        self.comboBox_lib = QComboBox(self.tab_lexicons)
        self.comboBox_lib.setObjectName(u"comboBox_lib")
        self.comboBox_lib.setMinimumSize(QSize(256, 48))
        self.comboBox_lib.setMaximumSize(QSize(16777215, 48))

        self.verticalLayout.addWidget(self.comboBox_lib)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.tableView = QTableView(self.tab_lexicons)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setProperty(u"showDropIndicator", True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_6.addWidget(self.tableView)


        self.gridLayout_9.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.line = QFrame(self.tab_lexicons)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_lexicons, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.gridLayout_4 = QGridLayout(self.tab_settings)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea = QScrollArea(self.tab_settings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background: transparent;")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -149, 759, 676))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_settings_profile_pic = QLabel(self.scrollAreaWidgetContents)
        self.label_settings_profile_pic.setObjectName(u"label_settings_profile_pic")
        self.label_settings_profile_pic.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_settings_profile_pic.sizePolicy().hasHeightForWidth())
        self.label_settings_profile_pic.setSizePolicy(sizePolicy)
        self.label_settings_profile_pic.setMinimumSize(QSize(72, 72))
        self.label_settings_profile_pic.setMaximumSize(QSize(72, 72))
        font1 = QFont()
        font1.setPointSize(28)
        font1.setBold(False)
        font1.setKerning(True)
        self.label_settings_profile_pic.setFont(font1)
        self.label_settings_profile_pic.setStyleSheet(u"image: url(:/pics/assets/profile_pic.png)")
        self.label_settings_profile_pic.setTextFormat(Qt.TextFormat.AutoText)
        self.label_settings_profile_pic.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_settings_profile_pic)

        self.label_settings_username = QLabel(self.scrollAreaWidgetContents)
        self.label_settings_username.setObjectName(u"label_settings_username")
        sizePolicy.setHeightForWidth(self.label_settings_username.sizePolicy().hasHeightForWidth())
        self.label_settings_username.setSizePolicy(sizePolicy)
        self.label_settings_username.setMinimumSize(QSize(128, 36))
        self.label_settings_username.setMaximumSize(QSize(512, 36))
        font2 = QFont()
        font2.setPointSize(28)
        font2.setBold(False)
        self.label_settings_username.setFont(font2)
        self.label_settings_username.setTextFormat(Qt.TextFormat.PlainText)
        self.label_settings_username.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_settings_username)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 3, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(128, 36))
        self.label_11.setMaximumSize(QSize(128, 36))
        self.label_11.setTextFormat(Qt.TextFormat.MarkdownText)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.checkBox_settings_devmode = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_settings_devmode.setObjectName(u"checkBox_settings_devmode")

        self.gridLayout_6.addWidget(self.checkBox_settings_devmode, 0, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(128, 36))
        self.label_6.setMaximumSize(QSize(128, 36))
        self.label_6.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)
        self.label_15.setMinimumSize(QSize(128, 36))
        self.label_15.setMaximumSize(QSize(128, 36))
        self.label_15.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgb(102, 102, 102);")

        self.gridLayout_6.addWidget(self.label_16, 2, 1, 1, 1)

        self.lineEdit_settings_server_url = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_settings_server_url.setObjectName(u"lineEdit_settings_server_url")

        self.gridLayout_6.addWidget(self.lineEdit_settings_server_url, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_6)


        self.gridLayout_5.addLayout(self.verticalLayout_4, 4, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(128, 36))
        self.label_17.setMaximumSize(QSize(128, 36))
        self.label_17.setTextFormat(Qt.TextFormat.MarkdownText)

        self.horizontalLayout_8.addWidget(self.label_17)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_9.addWidget(self.label_22)


        self.gridLayout_5.addLayout(self.verticalLayout_9, 6, 0, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_4, 5, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(128, 36))
        self.label_4.setMaximumSize(QSize(128, 36))
        self.label_4.setTextFormat(Qt.TextFormat.MarkdownText)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(128, 36))
        self.label_14.setMaximumSize(QSize(128, 36))
        self.label_14.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_7.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setMinimumSize(QSize(128, 36))
        self.label_12.setMaximumSize(QSize(128, 36))
        self.label_12.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_7.addWidget(self.label_12, 1, 0, 1, 1)

        self.lineEdit_settings_pwd_new = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_settings_pwd_new.setObjectName(u"lineEdit_settings_pwd_new")
        self.lineEdit_settings_pwd_new.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout_7.addWidget(self.lineEdit_settings_pwd_new, 2, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(128, 36))
        self.label_5.setMaximumSize(QSize(128, 36))
        self.label_5.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_settings_pwd_new_check = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_settings_pwd_new_check.setObjectName(u"lineEdit_settings_pwd_new_check")
        self.lineEdit_settings_pwd_new_check.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout_7.addWidget(self.lineEdit_settings_pwd_new_check, 3, 1, 1, 1)

        self.lineEdit_settings_pwd_old = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_settings_pwd_old.setObjectName(u"lineEdit_settings_pwd_old")
        self.lineEdit_settings_pwd_old.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_7.addWidget(self.lineEdit_settings_pwd_old, 1, 1, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMinimumSize(QSize(128, 36))
        self.label_13.setMaximumSize(QSize(128, 36))
        self.label_13.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_7.addWidget(self.label_13, 2, 0, 1, 1)

        self.pushButton_settings_changePwd = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_settings_changePwd.setObjectName(u"pushButton_settings_changePwd")
        sizePolicy.setHeightForWidth(self.pushButton_settings_changePwd.sizePolicy().hasHeightForWidth())
        self.pushButton_settings_changePwd.setSizePolicy(sizePolicy)
        self.pushButton_settings_changePwd.setMinimumSize(QSize(256, 32))
        self.pushButton_settings_changePwd.setMaximumSize(QSize(256, 32))
        self.pushButton_settings_changePwd.setStyleSheet(u"QPushButton {\n"
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
"    background: rgba(49, 27, 146, 0.7); /* \u66f4\u6df1\u4e00\u5c42\uff0c\u4fdd\u6301 70% \u4e0d\u900f\u660e */\n"
"}\n"
"QPushButton:disabled {\n"
"    background: rgba(189, 189, 189, 0.7); /* \u7981\u7528\u72b6\u6001\uff0c\u4fdd\u6301 70% \u4e0d\u900f\u660e */\n"
"    color: rgba(224, 224, 224, 0.7);\n"
"}")

        self.gridLayout_7.addWidget(self.pushButton_settings_changePwd, 4, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_7)


        self.gridLayout_5.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_settings, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_main_date.setText(QCoreApplication.translate("Form", u"# Date", None))
        self.pushButton_main_learn.setText(QCoreApplication.translate("Form", u"\u65b0\u5b66", None))
        self.pushButton_main_revise.setText(QCoreApplication.translate("Form", u"\u590d\u4e60", None))
        self.pushButton_main_sync.setText(QCoreApplication.translate("Form", u"\u540c\u6b65", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), QCoreApplication.translate("Form", u"\u80cc\u8bcd", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"# \u6211\u7684\u6570\u636e", None))
        self.label_lexicon_username.setText(QCoreApplication.translate("Form", u"### username", None))
        self.label_lexicon_time_all.setText(QCoreApplication.translate("Form", u"## Time", None))
        self.label_lexicon_count_all.setText(QCoreApplication.translate("Form", u"## Count", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"### \u7d2f\u8ba1\u65f6\u957f", None))
        self.label_lexicon_time_today.setText(QCoreApplication.translate("Form", u"## Time", None))
        self.label_lexicon_count_today.setText(QCoreApplication.translate("Form", u"## Count", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"### \u7d2f\u8ba1\u5b66\u4e60", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"### \u4eca\u65e5\u603b\u65f6\u957f", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"### \u4eca\u65e5\u5b66\u4e60/\u590d\u4e60", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5df2\u5b66\u4e60", None))
        self.label_lexicon_learned.setText(QCoreApplication.translate("Form", u"Learned", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u603b\u8bcd\u6570", None))
        self.label_lexicon_all.setText(QCoreApplication.translate("Form", u"Total", None))
        self.label.setText(QCoreApplication.translate("Form", u"# \u6b63\u5728\u5b66\u4e60", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_lexicons), QCoreApplication.translate("Form", u"\u8bcd\u5e93", None))
        self.label_settings_profile_pic.setText("")
        self.label_settings_username.setText(QCoreApplication.translate("Form", u"Welcome Back, Username", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"# \u5176\u4ed6\u8bbe\u7f6e", None))
        self.checkBox_settings_devmode.setText(QCoreApplication.translate("Form", u"\u5f00\u542f\u5f00\u53d1\u8005\u6a21\u5f0f", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"### \u5f00\u53d1\u8005\u6a21\u5f0f", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"#### \u81ea\u5b9a\u4e49\u670d\u52a1\u5668", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u53ef\u4ee5\u79c1\u6709\u90e8\u7f72 Lexify \u670d\u52a1\u7aef", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"# \u5173\u4e8e", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Lexify \u662f\u4e00\u6b3e\u4e13\u6ce8\u4e8e\u8bcd\u6c47\u5b66\u4e60\u7684\u5e94\u7528\uff0c\u5e2e\u52a9\u7528\u6237\u8f7b\u677e\u8bb0\u5fc6\u5355\u8bcd\u5e76\u8ffd\u8e2a\u5b66\u4e60\u8fdb\u5ea6\u3002", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"# \u7528\u6237\u8bbe\u7f6e", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"#### \u786e\u8ba4\u65b0\u5bc6\u7801", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"#### \u65e7\u5bc6\u7801", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"### \u4fee\u6539\u5bc6\u7801", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"#### \u65b0\u5bc6\u7801", None))
        self.pushButton_settings_changePwd.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u5bc6\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
    # retranslateUi

