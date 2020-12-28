# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1135, 985)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(650, 468))
        MainWindow.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(650, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy1)
        self.frame_main.setMinimumSize(QSize(0, 65))
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Sunken)
        self.frame_main.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(65, 55))
        self.frame_toggle.setMaximumSize(QSize(65, 55))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.frame_toggle)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy1.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy1)
        self.btn_toggle_menu.setMinimumSize(QSize(0, 55))
        self.btn_toggle_menu.setMaximumSize(QSize(65, 55))
        self.btn_toggle_menu.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/24x24/icons/24x24/cil-menu.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_toggle_menu.setIcon(icon)
        self.btn_toggle_menu.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_2.addWidget(self.frame_toggle)

        self.frame_info = QFrame(self.frame_top)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(QSize(0, 65))
        self.frame_info.setMaximumSize(QSize(16777215, 55))
        self.frame_info.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_info.setFrameShape(QFrame.NoFrame)
        self.frame_info.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.frame_info)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 4)
        self.label_status = QLabel(self.frame_info)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet(u"color: rgb(202, 204, 204);")

        self.verticalLayout.addWidget(self.label_status, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_info)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_bottom = QFrame(self.frame_center)
        self.frame_menu_bottom.setObjectName(u"frame_menu_bottom")
        sizePolicy1.setHeightForWidth(self.frame_menu_bottom.sizePolicy().hasHeightForWidth())
        self.frame_menu_bottom.setSizePolicy(sizePolicy1)
        self.frame_menu_bottom.setMinimumSize(QSize(65, 0))
        self.frame_menu_bottom.setMaximumSize(QSize(65, 16777215))
        self.frame_menu_bottom.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_menu_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_menu_bottom.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_5 = QVBoxLayout(self.frame_menu_bottom)
#ifndef Q_OS_MAC
        self.verticalLayout_5.setSpacing(-1)
#endif
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_menu_bottom)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(200, 65))
        self.btn_home.setMaximumSize(QSize(16777215, 65))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/24x24/icons/24x24/cil-home.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_add = QPushButton(self.frame_menu_bottom)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)
        self.btn_add.setMinimumSize(QSize(200, 65))
        self.btn_add.setMaximumSize(QSize(16777215, 65))
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/24x24/icons/24x24/cil-library-add.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_add.setIcon(icon2)
        self.btn_add.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_add)

        self.btn_view = QPushButton(self.frame_menu_bottom)
        self.btn_view.setObjectName(u"btn_view")
        sizePolicy2.setHeightForWidth(self.btn_view.sizePolicy().hasHeightForWidth())
        self.btn_view.setSizePolicy(sizePolicy2)
        self.btn_view.setMinimumSize(QSize(200, 65))
        self.btn_view.setMaximumSize(QSize(16777215, 65))
        self.btn_view.setStyleSheet(u"QPushButton {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/24x24/icons/24x24/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_view.setIcon(icon3)
        self.btn_view.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_view)

        self.btn_export = QPushButton(self.frame_menu_bottom)
        self.btn_export.setObjectName(u"btn_export")
        sizePolicy2.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy2)
        self.btn_export.setMinimumSize(QSize(200, 65))
        self.btn_export.setMaximumSize(QSize(16777215, 65))
        self.btn_export.setStyleSheet(u"QPushButton {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/24x24/icons/24x24/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_export.setIcon(icon4)
        self.btn_export.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_export)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.btn_settings = QPushButton(self.frame_menu_bottom)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy3)
        self.btn_settings.setMinimumSize(QSize(200, 65))
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/24x24/icons/24x24/cil-settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_settings.setIcon(icon5)
        self.btn_settings.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_settings)


        self.horizontalLayout_3.addWidget(self.frame_menu_bottom)

        self.frame_content_center = QFrame(self.frame_center)
        self.frame_content_center.setObjectName(u"frame_content_center")
        sizePolicy1.setHeightForWidth(self.frame_content_center.sizePolicy().hasHeightForWidth())
        self.frame_content_center.setSizePolicy(sizePolicy1)
        self.frame_content_center.setStyleSheet(u"")
        self.frame_content_center.setFrameShape(QFrame.NoFrame)
        self.frame_content_center.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content_center)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_center)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color: #222831")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_6 = QVBoxLayout(self.frame_content)
#ifndef Q_OS_MAC
        self.verticalLayout_6.setSpacing(-1)
#endif
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_7 = QVBoxLayout(self.page_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_home_logo = QFrame(self.page_home)
        self.frame_home_logo.setObjectName(u"frame_home_logo")
        self.frame_home_logo.setMinimumSize(QSize(0, 100))
        self.frame_home_logo.setFrameShape(QFrame.NoFrame)
        self.frame_home_logo.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame_home_logo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 12, 0)
        self.label_logo = QLabel(self.frame_home_logo)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(110, 16777215))
        self.label_logo.setPixmap(QPixmap(u":/other/logo.png"))

        self.horizontalLayout.addWidget(self.label_logo)

        self.frame_logo_text = QFrame(self.frame_home_logo)
        self.frame_logo_text.setObjectName(u"frame_logo_text")
        self.frame_logo_text.setFrameShape(QFrame.NoFrame)
        self.frame_logo_text.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_10 = QVBoxLayout(self.frame_logo_text)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_logo_text)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 40px;\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.label_title)

        self.label_subtitle = QLabel(self.frame_logo_text)
        self.label_subtitle.setObjectName(u"label_subtitle")
        self.label_subtitle.setMaximumSize(QSize(16777215, 16777215))
        self.label_subtitle.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 15px;\n"
"}\n"
"")
        self.label_subtitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.label_subtitle)


        self.horizontalLayout.addWidget(self.frame_logo_text)


        self.verticalLayout_7.addWidget(self.frame_home_logo)

        self.frame_home_content_2 = QFrame(self.page_home)
        self.frame_home_content_2.setObjectName(u"frame_home_content_2")
        self.frame_home_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_home_content_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_11 = QVBoxLayout(self.frame_home_content_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_home_content_2)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(0, 200))
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_home)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.label_4 = QLabel(self.frame_home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 30px;\n"
"	padding-left: 5px;\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label_4)

        self.frame_current_DB = QFrame(self.frame_home)
        self.frame_current_DB.setObjectName(u"frame_current_DB")
        self.frame_current_DB.setMinimumSize(QSize(0, 100))
        self.frame_current_DB.setMaximumSize(QSize(16777215, 600))
        self.frame_current_DB.setFrameShape(QFrame.StyledPanel)
        self.frame_current_DB.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_current_DB)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_current_DB)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(22, -1, 22, -1)
        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 40))
        self.label_19.setMaximumSize(QSize(16777215, 60))
        self.label_19.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 26px;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.label_19)

        self.label_current_database = QLabel(self.frame_9)
        self.label_current_database.setObjectName(u"label_current_database")
        self.label_current_database.setMinimumSize(QSize(0, 30))
        self.label_current_database.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setBold(True)
        self.label_current_database.setFont(font1)
        self.label_current_database.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 222, 224);\n"
"	font-size: 24px;\n"
"  font-weight: bold;\n"
"}\n"
"")
        self.label_current_database.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_13.addWidget(self.label_current_database)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(22, -1, 22, -1)
        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 40))
        self.label_21.setMaximumSize(QSize(16777215, 40))
        self.label_21.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 26px;\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.label_21)

        self.label_n_samples = QLabel(self.frame_7)
        self.label_n_samples.setObjectName(u"label_n_samples")
        self.label_n_samples.setMinimumSize(QSize(0, 30))
        self.label_n_samples.setMaximumSize(QSize(16777215, 30))
        self.label_n_samples.setFont(font1)
        self.label_n_samples.setStyleSheet(u"QLabel {\n"
"	color: rgb(221, 222, 224);\n"
"	font-size: 24px;\n"
"  font-weight: bold;\n"
"}\n"
"")
        self.label_n_samples.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.label_n_samples)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_8)


        self.gridLayout.addWidget(self.frame_7, 0, 1, 1, 1)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 26px;\n"
"}\n"
"")
        self.label_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_15.addWidget(self.label_8)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_7)


        self.gridLayout.addWidget(self.frame_10, 1, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 26px;\n"
"}\n"
"")
        self.label_9.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.label_9)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_9)


        self.gridLayout.addWidget(self.frame_8, 1, 1, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_current_DB)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(300, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(12, -1, -1, 12)
        self.frame_16 = QFrame(self.frame_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 26px;\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_15.addWidget(self.label_2)

        self.pushButton_6 = QPushButton(self.frame_16)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.pushButton_6)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 10px;\n"
"	font-size: 20px;\n"
"	color: rgb(201, 202, 204);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_5)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 35))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 26px;\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.label)

        self.tree_select_database = QTreeWidget(self.frame_5)
        self.tree_select_database.setObjectName(u"tree_select_database")
        self.tree_select_database.setMaximumSize(QSize(16777215, 100))
        self.tree_select_database.setStyleSheet(u"	color: rgb(201, 202, 204);\n"
"")
        self.tree_select_database.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tree_select_database.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tree_select_database.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tree_select_database.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tree_select_database.header().setCascadingSectionResizes(False)

        self.verticalLayout_8.addWidget(self.tree_select_database)


        self.horizontalLayout_7.addWidget(self.frame_5)


        self.verticalLayout_12.addWidget(self.frame_current_DB)


        self.verticalLayout_11.addWidget(self.frame_home)


        self.verticalLayout_7.addWidget(self.frame_home_content_2)

        self.stackedWidget.addWidget(self.page_home)
        self.page_add_delete = QWidget()
        self.page_add_delete.setObjectName(u"page_add_delete")
        self.verticalLayout_21 = QVBoxLayout(self.page_add_delete)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_upper = QFrame(self.page_add_delete)
        self.frame_upper.setObjectName(u"frame_upper")
        self.frame_upper.setMinimumSize(QSize(0, 300))
        self.frame_upper.setMaximumSize(QSize(16777215, 320))
        self.frame_upper.setFrameShape(QFrame.NoFrame)
        self.frame_upper.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_upper)
#ifndef Q_OS_MAC
        self.horizontalLayout_9.setSpacing(-1)
#endif
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_table = QFrame(self.frame_upper)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setMaximumSize(QSize(230, 16777215))
        self.frame_table.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_table.setFrameShape(QFrame.NoFrame)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_table)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(12, 0, 12, -1)
        self.frame_11 = QFrame(self.frame_table)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 120))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 6, 0, 6)
        self.frame_24 = QFrame(self.frame_11)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_24)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, -1, 0, -1)
        self.label_16 = QLabel(self.frame_24)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 30px;\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_24)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 15px;\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.label_17)


        self.horizontalLayout_12.addWidget(self.frame_24)


        self.verticalLayout_23.addWidget(self.frame_11)

        self.tree_select_database_2 = QTreeWidget(self.frame_table)
        self.tree_select_database_2.setObjectName(u"tree_select_database_2")
        self.tree_select_database_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tree_select_database_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_23.addWidget(self.tree_select_database_2)


        self.horizontalLayout_9.addWidget(self.frame_table)

        self.frame_add = QFrame(self.frame_upper)
        self.frame_add.setObjectName(u"frame_add")
        self.frame_add.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_add.setFrameShape(QFrame.NoFrame)
        self.frame_add.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_add)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 6, 0, 0)
        self.frame_add_title = QFrame(self.frame_add)
        self.frame_add_title.setObjectName(u"frame_add_title")
        self.frame_add_title.setMaximumSize(QSize(16777215, 100))
        self.frame_add_title.setFrameShape(QFrame.NoFrame)
        self.frame_add_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_add_title)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 20, 0)
        self.label_6 = QLabel(self.frame_add_title)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(85, 16777215))
        self.label_6.setStyleSheet(u"padding-left: 20px;")
        self.label_6.setPixmap(QPixmap(u":/other/add.png"))

        self.horizontalLayout_8.addWidget(self.label_6)

        self.frame_18 = QFrame(self.frame_add_title)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 30px;\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 15px;\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.label_11)


        self.horizontalLayout_8.addWidget(self.frame_18)

        self.pushButton_4 = QPushButton(self.frame_add_title)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy4)
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QSize(27, 24))

        self.horizontalLayout_8.addWidget(self.pushButton_4)


        self.verticalLayout_17.addWidget(self.frame_add_title)

        self.frame_add_content = QFrame(self.frame_add)
        self.frame_add_content.setObjectName(u"frame_add_content")
        self.frame_add_content.setFrameShape(QFrame.NoFrame)
        self.frame_add_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_add_content)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(12, 0, 12, 12)
        self.frame_12 = QFrame(self.frame_add_content)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_13)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"}")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_15)

        self.lineEdit_add_participant_ID = QLineEdit(self.frame_13)
        self.lineEdit_add_participant_ID.setObjectName(u"lineEdit_add_participant_ID")
        self.lineEdit_add_participant_ID.setMinimumSize(QSize(0, 30))
        self.lineEdit_add_participant_ID.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_28.addWidget(self.lineEdit_add_participant_ID)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_3)


        self.horizontalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_14)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"}")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_18)

        self.lineEdit_add_visit = QLineEdit(self.frame_14)
        self.lineEdit_add_visit.setObjectName(u"lineEdit_add_visit")
        self.lineEdit_add_visit.setMinimumSize(QSize(0, 30))
        self.lineEdit_add_visit.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_27.addWidget(self.lineEdit_add_visit)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_4)


        self.horizontalLayout_13.addWidget(self.frame_14)


        self.verticalLayout_25.addWidget(self.frame_12)

        self.label_status_add = QLabel(self.frame_add_content)
        self.label_status_add.setObjectName(u"label_status_add")
        self.label_status_add.setMinimumSize(QSize(0, 40))
        self.label_status_add.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"}")
        self.label_status_add.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_status_add)

        self.pushButton = QPushButton(self.frame_add_content)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 10px;\n"
"	font-size: 20px;\n"
"	color: rgb(201, 202, 204);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/24x24/cil-save.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon6)

        self.verticalLayout_25.addWidget(self.pushButton)


        self.verticalLayout_17.addWidget(self.frame_add_content)


        self.horizontalLayout_9.addWidget(self.frame_add)

        self.frame_remove = QFrame(self.frame_upper)
        self.frame_remove.setObjectName(u"frame_remove")
        self.frame_remove.setMinimumSize(QSize(300, 0))
        self.frame_remove.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_remove.setFrameShape(QFrame.NoFrame)
        self.frame_remove.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_remove)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 6, 0, 0)
        self.frame_remove_title = QFrame(self.frame_remove)
        self.frame_remove_title.setObjectName(u"frame_remove_title")
        self.frame_remove_title.setMinimumSize(QSize(0, 0))
        self.frame_remove_title.setMaximumSize(QSize(16777215, 100))
        self.frame_remove_title.setFrameShape(QFrame.NoFrame)
        self.frame_remove_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_remove_title)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 20, 0)
        self.label_7 = QLabel(self.frame_remove_title)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(85, 16777215))
        self.label_7.setStyleSheet(u"padding-left: 20px;\n"
"")
        self.label_7.setPixmap(QPixmap(u":/other/remove.png"))

        self.horizontalLayout_10.addWidget(self.label_7)

        self.frame_20 = QFrame(self.frame_remove_title)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_13 = QLabel(self.frame_20)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 30px;\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.label_13)

        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 15px;\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.label_12)


        self.horizontalLayout_10.addWidget(self.frame_20)

        self.pushButton_3 = QPushButton(self.frame_remove_title)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy5)
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.pushButton_3)


        self.verticalLayout_18.addWidget(self.frame_remove_title)

        self.frame_remove_content = QFrame(self.frame_remove)
        self.frame_remove_content.setObjectName(u"frame_remove_content")
        self.frame_remove_content.setFrameShape(QFrame.NoFrame)
        self.frame_remove_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_remove_content)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 0, 12, 12)
        self.frame_15 = QFrame(self.frame_remove_content)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_19)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_20 = QLabel(self.frame_19)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 20))
        self.label_20.setMaximumSize(QSize(16777215, 20))
        self.label_20.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"}")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_20)

        self.lineEdit_4 = QLineEdit(self.frame_19)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_30.addWidget(self.lineEdit_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_6)


        self.horizontalLayout_14.addWidget(self.frame_19)


        self.verticalLayout_26.addWidget(self.frame_15)

        self.pushButton_2 = QPushButton(self.frame_remove_content)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 10px;\n"
"	font-size: 20px;\n"
"	color: rgb(201, 202, 204);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/24x24/cil-trash.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon7)

        self.verticalLayout_26.addWidget(self.pushButton_2)


        self.verticalLayout_18.addWidget(self.frame_remove_content)


        self.horizontalLayout_9.addWidget(self.frame_remove)


        self.verticalLayout_21.addWidget(self.frame_upper)

        self.frame_table_2 = QFrame(self.page_add_delete)
        self.frame_table_2.setObjectName(u"frame_table_2")
        self.frame_table_2.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_table_2.setFrameShape(QFrame.StyledPanel)
        self.frame_table_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_table_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(12, -1, -1, -1)
        self.label_14 = QLabel(self.frame_table_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 50))
        self.label_14.setMaximumSize(QSize(16777215, 50))
        self.label_14.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 25px;\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.label_14)

        self.frame_22 = QFrame(self.frame_table_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, -1, -1)
        self.tableWidget_db_view = QTableWidget(self.frame_22)
        self.tableWidget_db_view.setObjectName(u"tableWidget_db_view")
        sizePolicy.setHeightForWidth(self.tableWidget_db_view.sizePolicy().hasHeightForWidth())
        self.tableWidget_db_view.setSizePolicy(sizePolicy)
        self.tableWidget_db_view.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_db_view.setFrameShadow(QFrame.Plain)
        self.tableWidget_db_view.horizontalHeader().setVisible(True)

        self.horizontalLayout_11.addWidget(self.tableWidget_db_view)

        self.btn_quick_edit = QFrame(self.frame_22)
        self.btn_quick_edit.setObjectName(u"btn_quick_edit")
        self.btn_quick_edit.setMinimumSize(QSize(40, 0))
        self.btn_quick_edit.setMaximumSize(QSize(40, 16777215))
        self.btn_quick_edit.setFrameShape(QFrame.StyledPanel)
        self.btn_quick_edit.setFrameShadow(QFrame.Plain)
        self.verticalLayout_29 = QVBoxLayout(self.btn_quick_edit)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.toolButton_delete = QToolButton(self.btn_quick_edit)
        self.toolButton_delete.setObjectName(u"toolButton_delete")
        self.toolButton_delete.setMinimumSize(QSize(40, 40))
        self.toolButton_delete.setMaximumSize(QSize(40, 40))
        self.toolButton_delete.setStyleSheet(u"QToolButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 10px;\n"
"	font-size: 12px;\n"
"	color: rgb(201, 202, 204);\n"
"\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QToolButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/24x24/icons/24x24/cil-trash.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_delete.setIcon(icon8)
        self.toolButton_delete.setIconSize(QSize(20, 20))
        self.toolButton_delete.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_29.addWidget(self.toolButton_delete)

        self.toolButton_2 = QToolButton(self.btn_quick_edit)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(40, 40))
        self.toolButton_2.setMaximumSize(QSize(40, 40))
        self.toolButton_2.setStyleSheet(u"QToolButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 10px;\n"
"	font-size: 12px;\n"
"	color: rgb(201, 202, 204);\n"
"\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QToolButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/20x20/icons/20x20/cil-description.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_2.setIcon(icon9)
        self.toolButton_2.setIconSize(QSize(20, 20))
        self.toolButton_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_29.addWidget(self.toolButton_2)


        self.horizontalLayout_11.addWidget(self.btn_quick_edit)


        self.verticalLayout_22.addWidget(self.frame_22)


        self.verticalLayout_21.addWidget(self.frame_table_2)

        self.stackedWidget.addWidget(self.page_add_delete)
        self.page_view = QWidget()
        self.page_view.setObjectName(u"page_view")
        self.verticalLayout_9 = QVBoxLayout(self.page_view)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame = QFrame(self.page_view)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);\n"
"background-color: #30475e;\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_9.addWidget(self.frame)

        self.frame_4 = QFrame(self.page_view)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_view)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_content)

        self.frame_status_bar = QFrame(self.frame_content_center)
        self.frame_status_bar.setObjectName(u"frame_status_bar")
        self.frame_status_bar.setMinimumSize(QSize(0, 25))
        self.frame_status_bar.setMaximumSize(QSize(16777215, 25))
        self.frame_status_bar.setStyleSheet(u"background-color: rgb(27, 29, 34)")
        self.frame_status_bar.setFrameShape(QFrame.NoFrame)
        self.frame_status_bar.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_status_bar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_status_bar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 14\n"
"px;\n"
"	padding-left: 2px;\n"
"	text-align: left;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame_status_bar)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 14px;\n"
"	padding-right: 10px;\n"
"	text-align: right;\n"
"}\n"
"")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_3.addWidget(self.frame_status_bar)


        self.horizontalLayout_3.addWidget(self.frame_content_center)


        self.verticalLayout_2.addWidget(self.frame_center)


        self.horizontalLayout_4.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1135, 24))
        self.menubar.setStyleSheet(u"QMenuBar {background-color: 0, 0, 0;}")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"    Home", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"    Add/delete", None))
        self.btn_view.setText(QCoreApplication.translate("MainWindow", u"    View data", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"    Export (CSV)", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"    Settings", None))
        self.label_logo.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"FreezeDB", None))
        self.label_subtitle.setText(QCoreApplication.translate("MainWindow", u"A simple GUI based database manager for keeping track \n"
"of clinical samples.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Current database", None))
        self.label_current_database.setText(QCoreApplication.translate("MainWindow", u"Placeholder: Database", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Number of samples", None))
        self.label_n_samples.setText(QCoreApplication.translate("MainWindow", u"Placeholder: n", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Quick Entry", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Quick Delete", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Create  database", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select database", None))
        ___qtreewidgetitem = self.tree_select_database.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Last entry", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Creation date", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Select database to add \n"
"and remove to/from.", None))
        ___qtreewidgetitem1 = self.tree_select_database_2.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Last edited", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Creation date", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Database", None));
        self.label_6.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Add database entries.", None))
        self.pushButton_4.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Participant ID", None))
        self.lineEdit_add_participant_ID.setText("")
        self.lineEdit_add_participant_ID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Participant", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Visit", None))
        self.lineEdit_add_visit.setText("")
        self.lineEdit_add_visit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Visit", None))
        self.label_status_add.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" Add", None))
        self.label_7.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Remove ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Remove database entries.", None))
        self.pushButton_3.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Identifer ID", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identifier ID", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" Remove", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Table view", None))
        self.toolButton_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Made by Anders Askeland", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Version: 0.0.1", None))
    # retranslateUi

