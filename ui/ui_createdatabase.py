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
        CreateDatabase.resize(400, 300)
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

        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(CreateDatabase)

        QMetaObject.connectSlotsByName(CreateDatabase)
    # setupUi

    def retranslateUi(self, CreateDatabase):
        CreateDatabase.setWindowTitle(QCoreApplication.translate("CreateDatabase", u"Form", None))
        self.label.setText(QCoreApplication.translate("CreateDatabase", u"Create new database", None))
    # retranslateUi
