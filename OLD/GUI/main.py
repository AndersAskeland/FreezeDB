##################################################################################
## Title: FreezeDB                                                              ##
##                                                                              ##
## Author: Anders Askeland                                                      ##
## Frameworks used: Qt Designer, SQLAlchemy 2.0, and PySide6                    ##
## Version: 0.0.1                                                               ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External modules
from operator import ne
import sys, os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QSizePolicy, QLabel, QTableWidgetItem
from PySide6.QtCore import QFile, QSize, QPropertyAnimation, QSize, Qt, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *

# Internal modules
from ui_mainwindow import Ui_MainWindow # UI file
from functions import nSamples, sql_table_names, loadSQL
from classes import Blood
from popup_createDB import Ui_Form_create_database 


##################################################################
## 2 - MAIN WINDOW                                              ##
##################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load generated python class fomr UI file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        ######################
        ## 2.1 - Settings   ##
        #################33###

        # Set window title
        self.setWindowTitle('FreezeDB')

        # Set window size
        startSize = QSize(1100, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        # Go to home page
        self.ui.stackedWidget.setCurrentIndex(0)


        ##########################
        ## 2.2 - Load settings  ##
        ##########################
        # Currently this is static. Should be made dynamic (JSON files) at some point of time.
        
        # Populate tree widget
        treeWidget(self)

        # Set db index
        self.ui.tree_select_database.setCurrentItem(self.ui.tree_select_database.topLevelItem(1)) # Selects multisite

        # Number of samples
        self.ui.label_n_samples.setText(str(nSamples(self.ui.tree_select_database.currentItem().text(0), Blood)))

        # Set database text
        self.ui.label_current_database.setText(self.ui.tree_select_database.currentItem().text(0))

        # Populate table
        loadData(self)
        
        ##########################
        ## 2.3 - Connections    ##
        ##########################

        # Connect buttons
        self.ui.btn_toggle_menu.clicked.connect(lambda: toggleMenu(self)) # Toggle
        self.ui.btn_home.clicked.connect(lambda: homePage(self)) # Home
        self.ui.btn_add.clicked.connect(lambda: addPage(self)) # Add
        self.ui.btn_view.clicked.connect(lambda: viewData(self)) # View data


        self.ui.tree_select_database.itemClicked.connect(lambda: databaseChange(self))

        # Slots

########################################################################
## 4 - Popups
########################################################################

class MyPopup(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.popup = Ui_Form_create_database()
        self.popup.setupUi(self)

        ######################
        ## 2.1 - Settings   ##
        #################33###

        # Set window title
        self.setWindowTitle('Popup test')

        # Set window size
        startSize = QSize(400, 200)
        self.resize(startSize)
        self.setMinimumSize(startSize)


def popup():
    popup = MyPopup()
    popup.show()
########################################################################
## 3 - Functions
########################################################################

# Populate tree widget on home page
def treeWidget(self):
    # Name
    i = 0

    for file in os.scandir("./databases"):
        if file.name.endswith(".db"):
            QTreeWidgetItem(self.ui.tree_select_database)
            item = self.ui.tree_select_database.topLevelItem(i)
            item.setText(0, QCoreApplication.translate("MainWindow", file.name[:-3], None))
            i += 1
        else:
            continue


def databaseChange(self):
    # Get selection
    current_db_name = self.ui.tree_select_database.currentItem().text(0)

    # Set text
    self.ui.label_current_database.setText(self.ui.tree_select_database.currentItem().text(0))

    # Set sample n 
    self.ui.label_n_samples.setText(str(nSamples(self.ui.tree_select_database.currentItem().text(0), Blood)))

    # Creation date
        ## TO DO 
        # I need to define new variables in the SQL file. 
        # Dont delete files, just hide it using a hide column.
        # Do min value on datetime

    # Last edited
        ## TO DO
        # Do max value on datetime


# Toggle menu
def toggleMenu(self):
    # Get current width
    current_width = self.ui.frame_menu_bottom.width()

    # Define width to be used
    extended_width = 200 if current_width == 65 else 65

    # Animation
    self.animation = QPropertyAnimation(self.ui.frame_menu_bottom, b"minimumWidth")
    self.animation.setDuration(300)
    self.animation.setStartValue(current_width)
    self.animation.setEndValue(extended_width)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start() 

def viewData(self):
    self.ui.stackedWidget.setCurrentIndex(2)

    # Change status bar
    self.ui.label_status.setText("View data")
    
    # Reset button
    # self.ui.current.setStyleSheet(btn_standard_css)

    # Pressed button
    # self.ui.btn_home.setStyleSheet(btn_pressed_css)



def loadData(self):
    # Load column names
    columns = sql_table_names(self.ui.tree_select_database.currentItem().text(0), Blood)

    # Set table and row count
    self.ui.tableWidget_db_view.setRowCount(int(nSamples(self.ui.tree_select_database.currentItem().text(0), Blood)))
    self.ui.tableWidget_db_view.setColumnCount(len(columns))
    
    print(self.ui.tableWidget_db_view.columnCount())
    print(self.ui.tableWidget_db_view.rowCount())

    # Write column names
    for i, column in enumerate(columns):
        # Create widget
        self.ui.tableWidget_db_view.setHorizontalHeaderItem(i, QTableWidgetItem())

        # Set widget column text
        widgetColumn = self.ui.tableWidget_db_view.horizontalHeaderItem(i)
        widgetColumn.setText(QCoreApplication.translate("MainWindow", column, None));       
    
    # Get data from SQL database
    sql_data = loadSQL(self.ui.tree_select_database.currentItem().text(0), Blood)
    
    # Put inside QTableWidget
    for i, data in enumerate(sql_data):
        for j, column in enumerate(columns):
            print(f"Row: {i}. {column}: {data.__dict__[column]}")
            self.ui.tableWidget_db_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.__dict__[column])))



def homePage(self):

    # Get current index
    # current = currentIndex(self)
    # print(current)
    # Change page
    self.ui.stackedWidget.setCurrentIndex(0)

    # Change status bar
    self.ui.label_status.setText("Home")
    
    # Reset button
    # self.ui.current.setStyleSheet(btn_standard_css)

    # Pressed button
    # self.ui.btn_home.setStyleSheet(btn_pressed_css)



def addPage(self): 
    # Get current index
    #current = currentIndex(self)
    # print(current)

    # Change page
    self.ui.stackedWidget.setCurrentIndex(1)

    # Change status bar
    self.ui.label_status.setText("Add or remove data")

    # Reset buttons
    # current.setStyleSheet(btn_standard_css)

    # Pressed button
    # self.ui.btn_add.setStyleSheet(btn_pressed_css)


def currentIndex(self):
    index = self.ui.stackedWidget.currentIndex()

    # Check location
    if index == 0:
        return("btn_home")
    elif index == 1:
        return("btn_add")
    elif index == 2:
        return("btn_view")
    else:
        pass






########################################################################
## 4 - Design elements
########################################################################
btn_standard_css = (u"QPushButton {\n"
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


btn_pressed_css = (u"QPushButton {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"	text-align: left;\n"
"   background-color: rgb(85, 170, 255)"
"}\n"
"")

########################################################################
## 5 - App event
########################################################################

# Start app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()


    sys.exit(app.exec_())       
