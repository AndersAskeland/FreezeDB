# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_createDB.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form_create_database(object):
    def setupUi(self, Form_create_database):
        if not Form_create_database.objectName():
            Form_create_database.setObjectName(u"Form_create_database")
        Form_create_database.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form_create_database)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form_create_database)
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

        self.frame_2 = QFrame(Form_create_database)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #222831")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form_create_database)

        QMetaObject.connectSlotsByName(Form_create_database)
    # setupUi

    def retranslateUi(self, Form_create_database):
        Form_create_database.setWindowTitle(QCoreApplication.translate("Form_create_database", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form_create_database", u"Create new database", None))
    # retranslateUi

