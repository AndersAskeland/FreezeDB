# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_create_db.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_create_db_page_(object):
    def setupUi(self, create_db_page_):
        if not create_db_page_.objectName():
            create_db_page_.setObjectName(u"create_db_page_")
        create_db_page_.resize(683, 390)
        self.verticalLayout_2 = QVBoxLayout(create_db_page_)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_freezedb = QLabel(create_db_page_)
        self.txt_freezedb.setObjectName(u"txt_freezedb")
        self.txt_freezedb.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.txt_freezedb)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(create_db_page_)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_4 = QLineEdit(create_db_page_)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QSize(0, 0))
        self.lineEdit_4.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lineEdit_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame = QFrame(create_db_page_)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.card_tabWidget = QTabWidget(self.frame)
        self.card_tabWidget.setObjectName(u"card_tabWidget")
        self.card_tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    background: rgb(42,49,61);\n"
"	color: rgb(204, 204, 204);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(42,49,61);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
""
                        "QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tab_3_card = QWidget()
        self.tab_3_card.setObjectName(u"tab_3_card")
        self.layoutWidget = QWidget(self.tab_3_card)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 571, 92))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6__text_base = QLabel(self.layoutWidget)
        self.label_6__text_base.setObjectName(u"label_6__text_base")

        self.gridLayout.addWidget(self.label_6__text_base, 0, 0, 1, 1)

        self.label_7__text_base = QLabel(self.layoutWidget)
        self.label_7__text_base.setObjectName(u"label_7__text_base")

        self.gridLayout.addWidget(self.label_7__text_base, 0, 1, 1, 1)

        self.label_8__text_base = QLabel(self.layoutWidget)
        self.label_8__text_base.setObjectName(u"label_8__text_base")

        self.gridLayout.addWidget(self.label_8__text_base, 0, 2, 1, 1)

        self.label_9__text_base = QLabel(self.layoutWidget)
        self.label_9__text_base.setObjectName(u"label_9__text_base")

        self.gridLayout.addWidget(self.label_9__text_base, 0, 3, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 3, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 2, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 2, 3, 1, 1)

        self.card_tabWidget.addTab(self.tab_3_card, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget1 = QWidget(self.tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 601, 185))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_7 = QCheckBox(self.layoutWidget1)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_2.addWidget(self.checkBox_7, 4, 0, 1, 1)

        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 0, 5, 1, 1)

        self.checkBox_5 = QCheckBox(self.layoutWidget1)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_2.addWidget(self.checkBox_5, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.comboBox_4 = QComboBox(self.layoutWidget1)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_2.addWidget(self.comboBox_4, 3, 5, 1, 1)

        self.checkBox_8 = QCheckBox(self.layoutWidget1)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_2.addWidget(self.checkBox_8, 1, 3, 1, 1)

        self.comboBox_5 = QComboBox(self.layoutWidget1)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_2.addWidget(self.comboBox_5, 4, 5, 1, 1)

        self.checkBox_9 = QCheckBox(self.layoutWidget1)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_2.addWidget(self.checkBox_9, 3, 3, 1, 1)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 4, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 4, 2, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 0))
        self.pushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.pushButton, 1, 4, 1, 1)

        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 3, 1, 1, 1)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 0, 4, 1, 1)

        self.pushButton_3 = QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 0))
        self.pushButton_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_3, 4, 4, 1, 1)

        self.checkBox_11 = QCheckBox(self.layoutWidget1)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_2.addWidget(self.checkBox_11, 4, 6, 1, 1)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 6, 1, 1)

        self.checkBox_6 = QCheckBox(self.layoutWidget1)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_2.addWidget(self.checkBox_6, 3, 0, 1, 1)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 0, 3, 1, 1)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 3, 2, 1, 1)

        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1)

        self.checkBox_4 = QCheckBox(self.layoutWidget1)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_2.addWidget(self.checkBox_4, 3, 6, 1, 1)

        self.checkBox_10 = QCheckBox(self.layoutWidget1)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_2.addWidget(self.checkBox_10, 4, 3, 1, 1)

        self.checkBox_3 = QCheckBox(self.layoutWidget1)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 1, 6, 1, 1)

        self.comboBox_6 = QComboBox(self.layoutWidget1)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_2.addWidget(self.comboBox_6, 2, 5, 1, 1)

        self.comboBox_7 = QComboBox(self.layoutWidget1)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_2.addWidget(self.comboBox_7, 1, 5, 1, 1)

        self.pushButton_2 = QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 0))
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 4, 1, 1)

        self.checkBox_12 = QCheckBox(self.layoutWidget1)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_2.addWidget(self.checkBox_12, 2, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 2, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 2, 1, 1, 1)

        self.checkBox_13 = QCheckBox(self.layoutWidget1)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout_2.addWidget(self.checkBox_13, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 0))
        self.pushButton_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 4, 1, 1)

        self.checkBox_14 = QCheckBox(self.layoutWidget1)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout_2.addWidget(self.checkBox_14, 2, 6, 1, 1)

        self.card_tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.card_tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.card_tabWidget)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(create_db_page_)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(create_db_page_)
        self.buttonBox.accepted.connect(create_db_page_.accept)
        self.buttonBox.rejected.connect(create_db_page_.reject)

        self.card_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(create_db_page_)
    # setupUi

    def retranslateUi(self, create_db_page_):
        create_db_page_.setWindowTitle(QCoreApplication.translate("create_db_page_", u"Dialog", None))
        self.txt_freezedb.setText(QCoreApplication.translate("create_db_page_", u"<html><head/><body><p><span style=\" font-size:24pt;\">Create new database layout</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("create_db_page_", u"Database layout name:", None))
#if QT_CONFIG(tooltip)
        self.card_tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_6__text_base.setText(QCoreApplication.translate("create_db_page_", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">What?</span></p></body></html>", None))
        self.label_7__text_base.setText(QCoreApplication.translate("create_db_page_", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Name</span></p></body></html>", None))
        self.label_8__text_base.setText(QCoreApplication.translate("create_db_page_", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Data type</span></p></body></html>", None))
        self.label_9__text_base.setText(QCoreApplication.translate("create_db_page_", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Nullable</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("create_db_page_", u"Identifer", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("create_db_page_", u"integer", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("create_db_page_", u"bool", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("create_db_page_", u"date", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("create_db_page_", u"string", None))

        self.checkBox.setText("")
        self.label_4.setText(QCoreApplication.translate("create_db_page_", u"ID", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("create_db_page_", u"integer", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("create_db_page_", u"bool", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("create_db_page_", u"string", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("create_db_page_", u"date", None))

        self.checkBox_2.setText("")
        self.card_tabWidget.setTabText(self.card_tabWidget.indexOf(self.tab_3_card), QCoreApplication.translate("create_db_page_", u"Required", None))
        self.checkBox_7.setText("")
        self.label_12.setText(QCoreApplication.translate("create_db_page_", u"Data type", None))
        self.checkBox_5.setText("")
        self.comboBox_4.setItemText(0, QCoreApplication.translate("create_db_page_", u"integer", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("create_db_page_", u"date", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("create_db_page_", u"bool", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("create_db_page_", u"string", None))

        self.checkBox_8.setText("")
        self.comboBox_5.setItemText(0, QCoreApplication.translate("create_db_page_", u"integer", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("create_db_page_", u"date", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("create_db_page_", u"bool", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("create_db_page_", u"string", None))

        self.checkBox_9.setText("")
        self.label_15.setText(QCoreApplication.translate("create_db_page_", u"Enable", None))
        self.label_18.setText(QCoreApplication.translate("create_db_page_", u"Time", None))
        self.pushButton.setText(QCoreApplication.translate("create_db_page_", u"Set", None))
        self.label_14.setText(QCoreApplication.translate("create_db_page_", u"Type", None))
        self.label_16.setText(QCoreApplication.translate("create_db_page_", u"Groups", None))
        self.pushButton_3.setText(QCoreApplication.translate("create_db_page_", u"Set", None))
        self.checkBox_11.setText("")
        self.label_13.setText(QCoreApplication.translate("create_db_page_", u"Nullable", None))
        self.checkBox_6.setText("")
        self.label_17.setText(QCoreApplication.translate("create_db_page_", u"Set groups", None))
        self.label_10.setText(QCoreApplication.translate("create_db_page_", u"What?", None))
        self.label_11.setText(QCoreApplication.translate("create_db_page_", u"Name", None))
        self.checkBox_4.setText("")
        self.checkBox_10.setText("")
        self.checkBox_3.setText("")
        self.comboBox_6.setItemText(0, QCoreApplication.translate("create_db_page_", u"integer", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("create_db_page_", u"date", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("create_db_page_", u"bool", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("create_db_page_", u"string", None))

        self.comboBox_7.setItemText(0, QCoreApplication.translate("create_db_page_", u"integer", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("create_db_page_", u"date", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("create_db_page_", u"bool", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("create_db_page_", u"string", None))

        self.pushButton_2.setText(QCoreApplication.translate("create_db_page_", u"Set", None))
        self.checkBox_12.setText("")
        self.label_5.setText(QCoreApplication.translate("create_db_page_", u"Groups", None))
        self.label_19.setText(QCoreApplication.translate("create_db_page_", u"Groups", None))
        self.checkBox_13.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("create_db_page_", u"Set", None))
        self.checkBox_14.setText("")
        self.card_tabWidget.setTabText(self.card_tabWidget.indexOf(self.tab), QCoreApplication.translate("create_db_page_", u"Optional", None))
        self.card_tabWidget.setTabText(self.card_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("create_db_page_", u"Custom", None))
    # retranslateUi

