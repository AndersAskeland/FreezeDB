# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from modules.property import QSideBar
from modules.property import QCard
from modules.widgets import AnimatedToggle

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2048, 764)
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.gridLayout = QGridLayout(self.mainWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_left = QSideBar(self.mainWidget)
        self.sidebar_left.setObjectName(u"sidebar_left")
        self.sidebar_left.setMinimumSize(QSize(65, 0))
        self.sidebar_left.setMaximumSize(QSize(60, 16777215))
        self.sidebar_left.setFrameShape(QFrame.NoFrame)
        self.sidebar_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_left)
#ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_home__btn_large = QPushButton(self.sidebar_left)
        self.btn_home__btn_large.setObjectName(u"btn_home__btn_large")
        self.btn_home__btn_large.setMinimumSize(QSize(0, 50))
        icon = QIcon()
        icon.addFile(u":/white_icons/white_icons/home-white-18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home__btn_large.setIcon(icon)
        self.btn_home__btn_large.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_home__btn_large)

        self.btn_add__btn_large = QPushButton(self.sidebar_left)
        self.btn_add__btn_large.setObjectName(u"btn_add__btn_large")
        self.btn_add__btn_large.setMinimumSize(QSize(0, 50))
        self.btn_add__btn_large.setText(u"     Add")
        icon1 = QIcon()
        icon1.addFile(u":/white_icons/white_icons/library_add-white-48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add__btn_large.setIcon(icon1)
        self.btn_add__btn_large.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_add__btn_large)

        self.btn_data__btn_large = QPushButton(self.sidebar_left)
        self.btn_data__btn_large.setObjectName(u"btn_data__btn_large")
        self.btn_data__btn_large.setMinimumSize(QSize(0, 50))
        icon2 = QIcon()
        icon2.addFile(u":/white_icons/white_icons/leaderboard-white-18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_data__btn_large.setIcon(icon2)
        self.btn_data__btn_large.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_data__btn_large)

        self.btn_export__btn_large = QPushButton(self.sidebar_left)
        self.btn_export__btn_large.setObjectName(u"btn_export__btn_large")
        self.btn_export__btn_large.setMinimumSize(QSize(0, 50))
        icon3 = QIcon()
        icon3.addFile(u":/white_icons/white_icons/folder-white-18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export__btn_large.setIcon(icon3)
        self.btn_export__btn_large.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_export__btn_large)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_settings__btn_large = QPushButton(self.sidebar_left)
        self.btn_settings__btn_large.setObjectName(u"btn_settings__btn_large")
        self.btn_settings__btn_large.setMinimumSize(QSize(0, 50))
        icon4 = QIcon()
        icon4.addFile(u":/white_icons/white_icons/settings-white-18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings__btn_large.setIcon(icon4)
        self.btn_settings__btn_large.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_settings__btn_large)


        self.gridLayout.addWidget(self.sidebar_left, 1, 0, 1, 1)

        self.sidebar_corner = QSideBar(self.mainWidget)
        self.sidebar_corner.setObjectName(u"sidebar_corner")
        self.sidebar_corner.setMinimumSize(QSize(65, 0))
        self.sidebar_corner.setMaximumSize(QSize(60, 55))
        self.sidebar_corner.setFrameShape(QFrame.NoFrame)
        self.sidebar_corner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sidebar_corner)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggleMenu__btn_large = QPushButton(self.sidebar_corner)
        self.btn_toggleMenu__btn_large.setObjectName(u"btn_toggleMenu__btn_large")
        self.btn_toggleMenu__btn_large.setMinimumSize(QSize(55, 55))
        icon5 = QIcon()
        icon5.addFile(u":/white_icons/white_icons/menu-white-18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggleMenu__btn_large.setIcon(icon5)
        self.btn_toggleMenu__btn_large.setIconSize(QSize(32, 32))
        self.btn_toggleMenu__btn_large.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_toggleMenu__btn_large)


        self.gridLayout.addWidget(self.sidebar_corner, 0, 0, 1, 1)

        self.sidebar_top = QSideBar(self.mainWidget)
        self.sidebar_top.setObjectName(u"sidebar_top")
        self.sidebar_top.setMinimumSize(QSize(0, 55))
        self.sidebar_top.setMaximumSize(QSize(16777215, 55))
        self.sidebar_top.setFrameShape(QFrame.NoFrame)
        self.sidebar_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.sidebar_top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.txt_header = QLabel(self.sidebar_top)
        self.txt_header.setObjectName(u"txt_header")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_header.sizePolicy().hasHeightForWidth())
        self.txt_header.setSizePolicy(sizePolicy)
        self.txt_header.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_header)

        self.animate_toggle = AnimatedToggle(self.sidebar_top)
        self.animate_toggle.setObjectName(u"animate_toggle")

        self.horizontalLayout.addWidget(self.animate_toggle)


        self.gridLayout.addWidget(self.sidebar_top, 0, 2, 1, 1)

        self.content = QVBoxLayout()
        self.content.setSpacing(0)
        self.content.setObjectName(u"content")
        self.pages = QFrame(self.mainWidget)
        self.pages.setObjectName(u"pages")
        self.pages.setMaximumSize(QSize(16777215, 16777215))
        self.pages.setStyleSheet(u"")
        self.pages.setFrameShape(QFrame.NoFrame)
        self.pages.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.pages)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pageWidget = QStackedWidget(self.pages)
        self.pageWidget.setObjectName(u"pageWidget")
        self.pageWidget.setFrameShadow(QFrame.Plain)
        self.pageWidget.setLineWidth(1)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_3 = QVBoxLayout(self.page_home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_top = QFrame(self.page_home)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 180))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.figure_logo = QLabel(self.frame_top)
        self.figure_logo.setObjectName(u"figure_logo")
        self.figure_logo.setMinimumSize(QSize(120, 0))
        self.figure_logo.setMaximumSize(QSize(120, 16777215))
        self.figure_logo.setPixmap(QPixmap(u":/figures/figures/logo.png"))

        self.horizontalLayout_4.addWidget(self.figure_logo)

        self.layout_level_1__1 = QVBoxLayout()
        self.layout_level_1__1.setObjectName(u"layout_level_1__1")
        self.txt_freezedb = QLabel(self.frame_top)
        self.txt_freezedb.setObjectName(u"txt_freezedb")
        self.txt_freezedb.setMinimumSize(QSize(400, 0))
        self.txt_freezedb.setTextFormat(Qt.RichText)

        self.layout_level_1__1.addWidget(self.txt_freezedb)

        self.txt_subtitle__text_base = QLabel(self.frame_top)
        self.txt_subtitle__text_base.setObjectName(u"txt_subtitle__text_base")
        self.txt_subtitle__text_base.setMinimumSize(QSize(400, 0))
        self.txt_subtitle__text_base.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.layout_level_1__1.addWidget(self.txt_subtitle__text_base)


        self.horizontalLayout_4.addLayout(self.layout_level_1__1)


        self.verticalLayout_3.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.page_home)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.txt_dashboard__text_2xl = QLabel(self.frame_bottom)
        self.txt_dashboard__text_2xl.setObjectName(u"txt_dashboard__text_2xl")
        self.txt_dashboard__text_2xl.setMaximumSize(QSize(16777214, 30))

        self.verticalLayout_8.addWidget(self.txt_dashboard__text_2xl)

        self.layout_level_1__2 = QHBoxLayout()
        self.layout_level_1__2.setObjectName(u"layout_level_1__2")
        self.layout_level_2__1 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.layout_level_2__1.setSpacing(-1)
#endif
        self.layout_level_2__1.setObjectName(u"layout_level_2__1")
        self.layout_level_3__2 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.layout_level_3__2.setSpacing(-1)
#endif
        self.layout_level_3__2.setObjectName(u"layout_level_3__2")
        self.card_currentDatabase = QCard(self.frame_bottom)
        self.card_currentDatabase.setObjectName(u"card_currentDatabase")
        self.card_currentDatabase.setMinimumSize(QSize(300, 200))
        self.card_currentDatabase.setFrameShape(QFrame.NoFrame)
        self.card_currentDatabase.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.card_currentDatabase)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.txt_currentDatabase = QLabel(self.card_currentDatabase)
        self.txt_currentDatabase.setObjectName(u"txt_currentDatabase")

        self.verticalLayout_7.addWidget(self.txt_currentDatabase)

        self.output_dbSelection__text_lg__font_bold = QLabel(self.card_currentDatabase)
        self.output_dbSelection__text_lg__font_bold.setObjectName(u"output_dbSelection__text_lg__font_bold")

        self.verticalLayout_7.addWidget(self.output_dbSelection__text_lg__font_bold)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.layout_level_3__2.addWidget(self.card_currentDatabase)

        self.card_sampleDist = QCard(self.frame_bottom)
        self.card_sampleDist.setObjectName(u"card_sampleDist")
        self.card_sampleDist.setMinimumSize(QSize(300, 200))
        self.card_sampleDist.setFrameShape(QFrame.NoFrame)
        self.card_sampleDist.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.card_sampleDist)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_sample_dist__text_xl = QLabel(self.card_sampleDist)
        self.txt_sample_dist__text_xl.setObjectName(u"txt_sample_dist__text_xl")

        self.verticalLayout_10.addWidget(self.txt_sample_dist__text_xl)

        self.graphicsView = QGraphicsView(self.card_sampleDist)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_10.addWidget(self.graphicsView)


        self.layout_level_3__2.addWidget(self.card_sampleDist)


        self.layout_level_2__1.addLayout(self.layout_level_3__2)

        self.layout_level_3__1 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.layout_level_3__1.setSpacing(-1)
#endif
        self.layout_level_3__1.setObjectName(u"layout_level_3__1")
        self.card_nSamples = QCard(self.frame_bottom)
        self.card_nSamples.setObjectName(u"card_nSamples")
        self.card_nSamples.setMinimumSize(QSize(300, 200))
        self.card_nSamples.setFrameShape(QFrame.NoFrame)
        self.card_nSamples.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.card_nSamples)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.txt_nSamples = QLabel(self.card_nSamples)
        self.txt_nSamples.setObjectName(u"txt_nSamples")

        self.verticalLayout_9.addWidget(self.txt_nSamples)

        self.output_dbSelection__text_lg__font_bold_2 = QLabel(self.card_nSamples)
        self.output_dbSelection__text_lg__font_bold_2.setObjectName(u"output_dbSelection__text_lg__font_bold_2")

        self.verticalLayout_9.addWidget(self.output_dbSelection__text_lg__font_bold_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.layout_level_3__1.addWidget(self.card_nSamples)

        self.card_groupDist = QCard(self.frame_bottom)
        self.card_groupDist.setObjectName(u"card_groupDist")
        self.card_groupDist.setMinimumSize(QSize(300, 200))
        self.card_groupDist.setFrameShape(QFrame.NoFrame)
        self.card_groupDist.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.card_groupDist)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.txt_group_dist__text_xl = QLabel(self.card_groupDist)
        self.txt_group_dist__text_xl.setObjectName(u"txt_group_dist__text_xl")

        self.verticalLayout_11.addWidget(self.txt_group_dist__text_xl)

        self.graphicsView_2 = QGraphicsView(self.card_groupDist)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_11.addWidget(self.graphicsView_2)


        self.layout_level_3__1.addWidget(self.card_groupDist)


        self.layout_level_2__1.addLayout(self.layout_level_3__1)


        self.layout_level_1__2.addLayout(self.layout_level_2__1)

        self.card_database = QCard(self.frame_bottom)
        self.card_database.setObjectName(u"card_database")
        self.card_database.setMinimumSize(QSize(250, 0))
        self.card_database.setMaximumSize(QSize(300, 16777215))
        self.card_database.setFrameShape(QFrame.NoFrame)
        self.card_database.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.card_database)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.layout_level_2__2 = QVBoxLayout()
        self.layout_level_2__2.setObjectName(u"layout_level_2__2")
        self.layout_level_3_2 = QHBoxLayout()
        self.layout_level_3_2.setObjectName(u"layout_level_3_2")
        self.txt_create_db__text_xl = QLabel(self.card_database)
        self.txt_create_db__text_xl.setObjectName(u"txt_create_db__text_xl")
        self.txt_create_db__text_xl.setMinimumSize(QSize(185, 0))
        self.txt_create_db__text_xl.setMaximumSize(QSize(16777215, 40))

        self.layout_level_3_2.addWidget(self.txt_create_db__text_xl)

        self.btn_pref__btn_small = QPushButton(self.card_database)
        self.btn_pref__btn_small.setObjectName(u"btn_pref__btn_small")
        self.btn_pref__btn_small.setMaximumSize(QSize(16777215, 16777215))
        self.btn_pref__btn_small.setIcon(icon4)
        self.btn_pref__btn_small.setIconSize(QSize(24, 24))

        self.layout_level_3_2.addWidget(self.btn_pref__btn_small)


        self.layout_level_2__2.addLayout(self.layout_level_3_2)

        self.layout_level_3_3 = QVBoxLayout()
        self.layout_level_3_3.setObjectName(u"layout_level_3_3")
        self.layout_level_3_3.setContentsMargins(-1, -1, -1, 0)
        self.txt_db_name__text_base = QLabel(self.card_database)
        self.txt_db_name__text_base.setObjectName(u"txt_db_name__text_base")
        self.txt_db_name__text_base.setStyleSheet(u"\n"
"\n"
"    text-align: center;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.txt_db_name__text_base.setAlignment(Qt.AlignCenter)

        self.layout_level_3_3.addWidget(self.txt_db_name__text_base)

        self.input_createDatabase = QLineEdit(self.card_database)
        self.input_createDatabase.setObjectName(u"input_createDatabase")

        self.layout_level_3_3.addWidget(self.input_createDatabase)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_level_3_3.addItem(self.verticalSpacer_8)

        self.label = QLabel(self.card_database)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.layout_level_3_3.addWidget(self.label)

        self.comboBox = QComboBox(self.card_database)
        self.comboBox.setObjectName(u"comboBox")

        self.layout_level_3_3.addWidget(self.comboBox)

        self.verticalSpacer_4 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_level_3_3.addItem(self.verticalSpacer_4)

        self.btn_createDB__btn_med = QPushButton(self.card_database)
        self.btn_createDB__btn_med.setObjectName(u"btn_createDB__btn_med")

        self.layout_level_3_3.addWidget(self.btn_createDB__btn_med)


        self.layout_level_2__2.addLayout(self.layout_level_3_3)


        self.verticalLayout_14.addLayout(self.layout_level_2__2)

        self.layout_level_2__3 = QVBoxLayout()
        self.layout_level_2__3.setObjectName(u"layout_level_2__3")
        self.txt_select_db__text_xl = QLabel(self.card_database)
        self.txt_select_db__text_xl.setObjectName(u"txt_select_db__text_xl")

        self.layout_level_2__3.addWidget(self.txt_select_db__text_xl)

        self.layout_level_3__3 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.layout_level_3__3.setSpacing(-1)
#endif
        self.layout_level_3__3.setObjectName(u"layout_level_3__3")
        self.tree_databaseViewHome = QTreeWidget(self.card_database)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Name");
        self.tree_databaseViewHome.setHeaderItem(__qtreewidgetitem)
        self.tree_databaseViewHome.setObjectName(u"tree_databaseViewHome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tree_databaseViewHome.sizePolicy().hasHeightForWidth())
        self.tree_databaseViewHome.setSizePolicy(sizePolicy1)
        self.tree_databaseViewHome.setMaximumSize(QSize(16777215, 120))
        self.tree_databaseViewHome.setStyleSheet(u"    border-radius: 4px;\n"
"")
        self.tree_databaseViewHome.setFrameShape(QFrame.NoFrame)
        self.tree_databaseViewHome.header().setVisible(True)
        self.tree_databaseViewHome.header().setCascadingSectionResizes(False)
        self.tree_databaseViewHome.header().setDefaultSectionSize(60)
        self.tree_databaseViewHome.header().setHighlightSections(False)
        self.tree_databaseViewHome.header().setStretchLastSection(True)

        self.layout_level_3__3.addWidget(self.tree_databaseViewHome)

        self.layout_level_4__1 = QVBoxLayout()
        self.layout_level_4__1.setObjectName(u"layout_level_4__1")
        self.btn_refreshDatabase__btn_small = QPushButton(self.card_database)
        self.btn_refreshDatabase__btn_small.setObjectName(u"btn_refreshDatabase__btn_small")
        icon6 = QIcon()
        icon6.addFile(u":/white_icons/white_icons/refresh-white-18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refreshDatabase__btn_small.setIcon(icon6)
        self.btn_refreshDatabase__btn_small.setIconSize(QSize(24, 24))

        self.layout_level_4__1.addWidget(self.btn_refreshDatabase__btn_small)

        self.btn_deleteDatabase__btn_small = QPushButton(self.card_database)
        self.btn_deleteDatabase__btn_small.setObjectName(u"btn_deleteDatabase__btn_small")
        self.btn_deleteDatabase__btn_small.setIcon(icon4)
        self.btn_deleteDatabase__btn_small.setIconSize(QSize(24, 24))

        self.layout_level_4__1.addWidget(self.btn_deleteDatabase__btn_small)


        self.layout_level_3__3.addLayout(self.layout_level_4__1)


        self.layout_level_2__3.addLayout(self.layout_level_3__3)


        self.verticalLayout_14.addLayout(self.layout_level_2__3)


        self.layout_level_1__2.addWidget(self.card_database)


        self.verticalLayout_8.addLayout(self.layout_level_1__2)


        self.verticalLayout_3.addWidget(self.frame_bottom)

        self.pageWidget.addWidget(self.page_home)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        self.verticalLayout_5 = QVBoxLayout(self.page_add)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.layout_level_1__4 = QHBoxLayout()
        self.layout_level_1__4.setObjectName(u"layout_level_1__4")
        self.card_databaseView = QFrame(self.page_add)
        self.card_databaseView.setObjectName(u"card_databaseView")
        self.card_databaseView.setMaximumSize(QSize(250, 350))
        self.card_databaseView.setFrameShape(QFrame.StyledPanel)
        self.card_databaseView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.card_databaseView)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.txt_databases__text_xl2 = QLabel(self.card_databaseView)
        self.txt_databases__text_xl2.setObjectName(u"txt_databases__text_xl2")

        self.verticalLayout_6.addWidget(self.txt_databases__text_xl2)

        self.txt_databaseSubtitle__text_base = QLabel(self.card_databaseView)
        self.txt_databaseSubtitle__text_base.setObjectName(u"txt_databaseSubtitle__text_base")
        self.txt_databaseSubtitle__text_base.setMinimumSize(QSize(0, 50))
        self.txt_databaseSubtitle__text_base.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.txt_databaseSubtitle__text_base)

        self.tree_databaseViewAdd = QTreeWidget(self.card_databaseView)
        self.tree_databaseViewAdd.setObjectName(u"tree_databaseViewAdd")
        self.tree_databaseViewAdd.header().setDefaultSectionSize(65)

        self.verticalLayout_6.addWidget(self.tree_databaseViewAdd)


        self.layout_level_1__4.addWidget(self.card_databaseView)

        self.card_add = QFrame(self.page_add)
        self.card_add.setObjectName(u"card_add")
        self.card_add.setMinimumSize(QSize(350, 0))
        self.card_add.setMaximumSize(QSize(16777215, 350))
        self.card_add.setFrameShape(QFrame.StyledPanel)
        self.card_add.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.card_add)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.layout_level_2__5 = QHBoxLayout()
        self.layout_level_2__5.setObjectName(u"layout_level_2__5")
        self.layout_level_2__5.setContentsMargins(-1, -1, 12, -1)
        self.figure_add = QLabel(self.card_add)
        self.figure_add.setObjectName(u"figure_add")
        self.figure_add.setMinimumSize(QSize(70, 80))
        self.figure_add.setMaximumSize(QSize(70, 80))
        self.figure_add.setPixmap(QPixmap(u":/figures/figures/add.png"))

        self.layout_level_2__5.addWidget(self.figure_add)

        self.layout_level_3__4 = QVBoxLayout()
        self.layout_level_3__4.setObjectName(u"layout_level_3__4")
        self.txt_addData__text_xl2 = QLabel(self.card_add)
        self.txt_addData__text_xl2.setObjectName(u"txt_addData__text_xl2")
        self.txt_addData__text_xl2.setMaximumSize(QSize(16777215, 30))

        self.layout_level_3__4.addWidget(self.txt_addData__text_xl2)

        self.txt_addSubtitle__text_base = QLabel(self.card_add)
        self.txt_addSubtitle__text_base.setObjectName(u"txt_addSubtitle__text_base")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_addSubtitle__text_base.sizePolicy().hasHeightForWidth())
        self.txt_addSubtitle__text_base.setSizePolicy(sizePolicy2)
        self.txt_addSubtitle__text_base.setMaximumSize(QSize(16777215, 40))
        self.txt_addSubtitle__text_base.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.layout_level_3__4.addWidget(self.txt_addSubtitle__text_base)


        self.layout_level_2__5.addLayout(self.layout_level_3__4)

        self.btn_prefAdd__btn_small = QPushButton(self.card_add)
        self.btn_prefAdd__btn_small.setObjectName(u"btn_prefAdd__btn_small")
        icon7 = QIcon()
        icon7.addFile(u":/icons_white/graphics/white_icons/settings-white-18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prefAdd__btn_small.setIcon(icon7)
        self.btn_prefAdd__btn_small.setIconSize(QSize(24, 24))

        self.layout_level_2__5.addWidget(self.btn_prefAdd__btn_small)


        self.verticalLayout_16.addLayout(self.layout_level_2__5)

        self.layout_level_2__6 = QHBoxLayout()
        self.layout_level_2__6.setObjectName(u"layout_level_2__6")
        self.layout_level_3__6 = QVBoxLayout()
        self.layout_level_3__6.setObjectName(u"layout_level_3__6")
        self.txt_participantID__text_lg = QLabel(self.card_add)
        self.txt_participantID__text_lg.setObjectName(u"txt_participantID__text_lg")
        self.txt_participantID__text_lg.setAlignment(Qt.AlignCenter)

        self.layout_level_3__6.addWidget(self.txt_participantID__text_lg)

        self.input_participantID = QLineEdit(self.card_add)
        self.input_participantID.setObjectName(u"input_participantID")

        self.layout_level_3__6.addWidget(self.input_participantID)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_level_3__6.addItem(self.verticalSpacer_5)

        self.txt_date__text_lg = QLabel(self.card_add)
        self.txt_date__text_lg.setObjectName(u"txt_date__text_lg")
        self.txt_date__text_lg.setAlignment(Qt.AlignCenter)

        self.layout_level_3__6.addWidget(self.txt_date__text_lg)

        self.input_date = QLineEdit(self.card_add)
        self.input_date.setObjectName(u"input_date")

        self.layout_level_3__6.addWidget(self.input_date)


        self.layout_level_2__6.addLayout(self.layout_level_3__6)

        self.layout_level_3__5 = QVBoxLayout()
        self.layout_level_3__5.setObjectName(u"layout_level_3__5")
        self.txt_visit__text_lg = QLabel(self.card_add)
        self.txt_visit__text_lg.setObjectName(u"txt_visit__text_lg")
        self.txt_visit__text_lg.setAlignment(Qt.AlignCenter)

        self.layout_level_3__5.addWidget(self.txt_visit__text_lg)

        self.input_visit = QLineEdit(self.card_add)
        self.input_visit.setObjectName(u"input_visit")

        self.layout_level_3__5.addWidget(self.input_visit)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_level_3__5.addItem(self.verticalSpacer_6)

        self.txt_group__text_lg = QLabel(self.card_add)
        self.txt_group__text_lg.setObjectName(u"txt_group__text_lg")
        self.txt_group__text_lg.setAlignment(Qt.AlignCenter)

        self.layout_level_3__5.addWidget(self.txt_group__text_lg)

        self.input_group = QLineEdit(self.card_add)
        self.input_group.setObjectName(u"input_group")

        self.layout_level_3__5.addWidget(self.input_group)


        self.layout_level_2__6.addLayout(self.layout_level_3__5)


        self.verticalLayout_16.addLayout(self.layout_level_2__6)

        self.btn_add__btn_med = QPushButton(self.card_add)
        self.btn_add__btn_med.setObjectName(u"btn_add__btn_med")

        self.verticalLayout_16.addWidget(self.btn_add__btn_med)


        self.layout_level_1__4.addWidget(self.card_add)

        self.card_delete = QFrame(self.page_add)
        self.card_delete.setObjectName(u"card_delete")
        self.card_delete.setMinimumSize(QSize(350, 0))
        self.card_delete.setMaximumSize(QSize(16777215, 350))
        self.card_delete.setFrameShape(QFrame.StyledPanel)
        self.card_delete.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.card_delete)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, -1, 12)
        self.layout_level_1__5 = QHBoxLayout()
        self.layout_level_1__5.setObjectName(u"layout_level_1__5")
        self.layout_level_1__5.setContentsMargins(-1, -1, 12, -1)
        self.figure_remove = QLabel(self.card_delete)
        self.figure_remove.setObjectName(u"figure_remove")
        self.figure_remove.setMinimumSize(QSize(70, 80))
        self.figure_remove.setMaximumSize(QSize(70, 80))
        self.figure_remove.setPixmap(QPixmap(u":/figures/figures/remove.png"))

        self.layout_level_1__5.addWidget(self.figure_remove)

        self.layout_level_2__7 = QVBoxLayout()
        self.layout_level_2__7.setObjectName(u"layout_level_2__7")
        self.txt_removeData__text_xl2_2 = QLabel(self.card_delete)
        self.txt_removeData__text_xl2_2.setObjectName(u"txt_removeData__text_xl2_2")
        self.txt_removeData__text_xl2_2.setMaximumSize(QSize(16777215, 30))

        self.layout_level_2__7.addWidget(self.txt_removeData__text_xl2_2)

        self.txt_removeSubtitle__text_base = QLabel(self.card_delete)
        self.txt_removeSubtitle__text_base.setObjectName(u"txt_removeSubtitle__text_base")
        sizePolicy2.setHeightForWidth(self.txt_removeSubtitle__text_base.sizePolicy().hasHeightForWidth())
        self.txt_removeSubtitle__text_base.setSizePolicy(sizePolicy2)
        self.txt_removeSubtitle__text_base.setMaximumSize(QSize(16777215, 40))
        self.txt_removeSubtitle__text_base.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.layout_level_2__7.addWidget(self.txt_removeSubtitle__text_base)


        self.layout_level_1__5.addLayout(self.layout_level_2__7)

        self.btn_prefAdd__btn_small_2 = QPushButton(self.card_delete)
        self.btn_prefAdd__btn_small_2.setObjectName(u"btn_prefAdd__btn_small_2")
        self.btn_prefAdd__btn_small_2.setIcon(icon7)
        self.btn_prefAdd__btn_small_2.setIconSize(QSize(24, 24))

        self.layout_level_1__5.addWidget(self.btn_prefAdd__btn_small_2)


        self.verticalLayout_19.addLayout(self.layout_level_1__5)

        self.layout_level_1__6 = QVBoxLayout()
        self.layout_level_1__6.setObjectName(u"layout_level_1__6")
        self.txt_participantID__text_lg_2 = QLabel(self.card_delete)
        self.txt_participantID__text_lg_2.setObjectName(u"txt_participantID__text_lg_2")
        self.txt_participantID__text_lg_2.setAlignment(Qt.AlignCenter)

        self.layout_level_1__6.addWidget(self.txt_participantID__text_lg_2)

        self.input_identifier = QLineEdit(self.card_delete)
        self.input_identifier.setObjectName(u"input_identifier")

        self.layout_level_1__6.addWidget(self.input_identifier)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_level_1__6.addItem(self.verticalSpacer_7)


        self.verticalLayout_19.addLayout(self.layout_level_1__6)

        self.btn_remove__btn_med = QPushButton(self.card_delete)
        self.btn_remove__btn_med.setObjectName(u"btn_remove__btn_med")

        self.verticalLayout_19.addWidget(self.btn_remove__btn_med)


        self.layout_level_1__4.addWidget(self.card_delete)


        self.verticalLayout_5.addLayout(self.layout_level_1__4)

        self.card_databaseTable = QFrame(self.page_add)
        self.card_databaseTable.setObjectName(u"card_databaseTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.card_databaseTable.sizePolicy().hasHeightForWidth())
        self.card_databaseTable.setSizePolicy(sizePolicy3)
        self.card_databaseTable.setMinimumSize(QSize(0, 300))
        self.card_databaseTable.setFrameShape(QFrame.StyledPanel)
        self.card_databaseTable.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.card_databaseTable)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.output_databaseTable__text_xl2 = QLabel(self.card_databaseTable)
        self.output_databaseTable__text_xl2.setObjectName(u"output_databaseTable__text_xl2")

        self.verticalLayout_20.addWidget(self.output_databaseTable__text_xl2)

        self.layout_level_1__3 = QHBoxLayout()
        self.layout_level_1__3.setObjectName(u"layout_level_1__3")
        self.table_database = QTableWidget(self.card_databaseTable)
        if (self.table_database.columnCount() < 1):
            self.table_database.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_database.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.table_database.setObjectName(u"table_database")
        self.table_database.setMaximumSize(QSize(16777215, 16777215))

        self.layout_level_1__3.addWidget(self.table_database)

        self.layout_level_2__4 = QVBoxLayout()
        self.layout_level_2__4.setObjectName(u"layout_level_2__4")
        self.btn_deleteEntry__btn_small = QPushButton(self.card_databaseTable)
        self.btn_deleteEntry__btn_small.setObjectName(u"btn_deleteEntry__btn_small")
        icon8 = QIcon()
        icon8.addFile(u":/white_icons/white_icons/delete-white-18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_deleteEntry__btn_small.setIcon(icon8)
        self.btn_deleteEntry__btn_small.setIconSize(QSize(24, 24))

        self.layout_level_2__4.addWidget(self.btn_deleteEntry__btn_small)

        self.btn_refresh__btn_small_2 = QPushButton(self.card_databaseTable)
        self.btn_refresh__btn_small_2.setObjectName(u"btn_refresh__btn_small_2")
        self.btn_refresh__btn_small_2.setIcon(icon6)
        self.btn_refresh__btn_small_2.setIconSize(QSize(24, 24))

        self.layout_level_2__4.addWidget(self.btn_refresh__btn_small_2)


        self.layout_level_1__3.addLayout(self.layout_level_2__4)


        self.verticalLayout_20.addLayout(self.layout_level_1__3)


        self.verticalLayout_5.addWidget(self.card_databaseTable)

        self.pageWidget.addWidget(self.page_add)
        self.page_data = QWidget()
        self.page_data.setObjectName(u"page_data")
        self.pageWidget.addWidget(self.page_data)
        self.page_export = QWidget()
        self.page_export.setObjectName(u"page_export")
        self.pageWidget.addWidget(self.page_export)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.pageWidget.addWidget(self.page_settings)

        self.verticalLayout.addWidget(self.pageWidget)


        self.content.addWidget(self.pages)

        self.footer = QFrame(self.mainWidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 20))
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Raised)

        self.content.addWidget(self.footer)


        self.gridLayout.addLayout(self.content, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.mainWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2048, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home__btn_large.setText(QCoreApplication.translate("MainWindow", u"     Home", None))
        self.btn_data__btn_large.setText(QCoreApplication.translate("MainWindow", u"     View", None))
        self.btn_export__btn_large.setText(QCoreApplication.translate("MainWindow", u"     Export", None))
        self.btn_settings__btn_large.setText(QCoreApplication.translate("MainWindow", u"     Settings", None))
        self.btn_toggleMenu__btn_large.setText("")
        self.txt_header.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.animate_toggle.setText("")
        self.figure_logo.setText("")
        self.txt_freezedb.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt;\">FreezeDB</span></p></body></html>", None))
        self.txt_subtitle__text_base.setText(QCoreApplication.translate("MainWindow", u"A simple GUI based database manager for keeping track \n"
"of clinical samples.", None))
        self.txt_dashboard__text_2xl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt;\">Dashboard</span></p></body></html>", None))
        self.txt_currentDatabase.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Current database</span></p></body></html>", None))
        self.output_dbSelection__text_lg__font_bold.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">No selection</span></p></body></html>", None))
        self.txt_sample_dist__text_xl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Sample distribution</span></p></body></html>", None))
        self.txt_nSamples.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Number of entries</span></p></body></html>", None))
        self.output_dbSelection__text_lg__font_bold_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">No selection</span></p></body></html>", None))
        self.txt_group_dist__text_xl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Group distribution</span></p></body></html>", None))
        self.txt_create_db__text_xl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Create database</span></p></body></html>", None))
        self.btn_pref__btn_small.setText("")
        self.txt_db_name__text_base.setText(QCoreApplication.translate("MainWindow", u"Database name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Database layout", None))
        self.btn_createDB__btn_med.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.txt_select_db__text_xl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Avaliable databases</span></p></body></html>", None))
        ___qtreewidgetitem = self.tree_databaseViewHome.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Creation date", None));
        self.btn_refreshDatabase__btn_small.setText("")
        self.btn_deleteDatabase__btn_small.setText("")
        self.txt_databases__text_xl2.setText(QCoreApplication.translate("MainWindow", u"Databases", None))
        self.txt_databaseSubtitle__text_base.setText(QCoreApplication.translate("MainWindow", u"Select database to add \n"
"and remove to/from.", None))
        ___qtreewidgetitem1 = self.tree_databaseViewAdd.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Creation date", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.figure_add.setText("")
        self.txt_addData__text_xl2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.txt_addSubtitle__text_base.setText(QCoreApplication.translate("MainWindow", u"Add database entries.", None))
        self.btn_prefAdd__btn_small.setText("")
        self.txt_participantID__text_lg.setText(QCoreApplication.translate("MainWindow", u"Participant ID", None))
        self.txt_date__text_lg.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.txt_visit__text_lg.setText(QCoreApplication.translate("MainWindow", u"Visit", None))
        self.txt_group__text_lg.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.btn_add__btn_med.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.figure_remove.setText("")
        self.txt_removeData__text_xl2_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.txt_removeSubtitle__text_base.setText(QCoreApplication.translate("MainWindow", u"Remove database enteries.", None))
        self.btn_prefAdd__btn_small_2.setText("")
        self.txt_participantID__text_lg_2.setText(QCoreApplication.translate("MainWindow", u"Identifier", None))
        self.btn_remove__btn_med.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.output_databaseTable__text_xl2.setText(QCoreApplication.translate("MainWindow", u"No database selected", None))
        ___qtablewidgetitem = self.table_database.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        self.btn_deleteEntry__btn_small.setText("")
        self.btn_refresh__btn_small_2.setText("")
    # retranslateUi

