# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_firstTimeStart.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_FirstStart(object):
    def setupUi(self, Dialog_FirstStart):
        if not Dialog_FirstStart.objectName():
            Dialog_FirstStart.setObjectName(u"Dialog_FirstStart")
        Dialog_FirstStart.resize(830, 428)
        self.verticalLayout = QVBoxLayout(Dialog_FirstStart)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(Dialog_FirstStart)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(120, 0))
        self.frame_2.setMaximumSize(QSize(120, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"graphics/logo.png"))

        self.verticalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(Dialog_FirstStart)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.verticalLayout_3 = QVBoxLayout(self.page_welcome)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.page_welcome)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 666, 360))
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 10, 668, 135))
        self.label_5.setTextFormat(Qt.RichText)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_welcome)
        self.page_licence = QWidget()
        self.page_licence.setObjectName(u"page_licence")
        self.verticalLayout_4 = QVBoxLayout(self.page_licence)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.page_licence)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.RichText)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.page_licence)
        self.page_folder = QWidget()
        self.page_folder.setObjectName(u"page_folder")
        self.horizontalLayout_4 = QHBoxLayout(self.page_folder)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_folder)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame = QFrame(Dialog_FirstStart)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(654, 11, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_FirstStart)

        QMetaObject.connectSlotsByName(Dialog_FirstStart)
    # setupUi

    def retranslateUi(self, Dialog_FirstStart):
        Dialog_FirstStart.setWindowTitle(QCoreApplication.translate("Dialog_FirstStart", u"Dialog", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_FirstStart", u"* Welcome", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_FirstStart", u"* Licence", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_FirstStart", u"* Data folder", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_FirstStart", u"<html><head/><body><p><span style=\" font-size:36pt;\">FreezeDB - First time setup</span></p><p><span style=\" font-size:14pt;\">Welcome to FreezeDB. FreezeDB is a simple application that can manage data <br/>related to clinical samples.</span></p><p><span style=\" font-size:14pt;\">As this is the first time you open this application on the currenct computer, you'll need to<br/>accept the licence terms and select the default storage location.</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_FirstStart", u"<html><head/><body><p><span style=\" font-size:36pt;\">Licence</span></p><p><span style=\" font-size:14pt;\">TODO</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog_FirstStart", u"Back", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_FirstStart", u"Next", None))
    # retranslateUi

