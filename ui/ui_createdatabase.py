# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_createdatabase.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_CreateDatabase(object):
    def setupUi(self, CreateDatabase):
        if not CreateDatabase.objectName():
            CreateDatabase.setObjectName(u"CreateDatabase")
        CreateDatabase.resize(841, 309)
        self.verticalLayout = QVBoxLayout(CreateDatabase)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CreateDatabase)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(CreateDatabase)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #222831")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(42,49,61);\n"
"border-radius: 20px;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 0, -1, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(70, 0))
        self.pushButton_2.setMaximumSize(QSize(70, 16777215))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	font-size: 15px;\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(70, 0))
        self.pushButton.setMaximumSize(QSize(70, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	font-size: 15px;\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(CreateDatabase)

        QMetaObject.connectSlotsByName(CreateDatabase)
    # setupUi

    def retranslateUi(self, CreateDatabase):
        CreateDatabase.setWindowTitle(QCoreApplication.translate("CreateDatabase", u"Form", None))
        self.label.setText(QCoreApplication.translate("CreateDatabase", u"Create new database", None))
        self.pushButton_2.setText(QCoreApplication.translate("CreateDatabase", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("CreateDatabase", u"Submit", None))
    # retranslateUi

