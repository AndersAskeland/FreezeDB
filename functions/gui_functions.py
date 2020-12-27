##################################################################################
##                                                                              ##
## Title: GUI functions                                                         ##
##                                                                              ##
## What: All functions related to the GUI and PySide6.                          ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External modules
import os
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QTreeWidgetItem, QTableWidgetItem
from PySide6.QtCore import QCoreApplication, QPropertyAnimation

# Internal modules
from ui.css import css_btn_pressed, css_btn_idle
from functions.sql_functions import n_samples, sql_column_keys, sql_to_dict
from classes.sql_classes import Blood

##################################################################
## 2 - SETTINGS AND CONSTANTS                                   ##
##################################################################



##################################################################
## 3 - FUNCTIONS                                                ##
##################################################################

# 3.1 UPDATE DATABASE LIST - Updates treewidget list on home page with all databases found in databases folder
def update_db_list(self):
    # Define manual itterator
    i = 0    

    for file in os.scandir("./databases"):
        if file.name.endswith(".db"):
            # Create item
            QTreeWidgetItem(self.ui.tree_select_database)

            # Set item name
            item = self.ui.tree_select_database.topLevelItem(i)
            item.setText(0, QCoreApplication.translate("MainWindow", file.name[:-3], None))
            
            # Itterate
            i += 1
        else:
            continue


# 3.2 ANIMATE TOGGLE MENU - Open and close the toggle menu. Connected to button
def toggle_menu(self):
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


# 3.3 CHANGE PAGES - Functions for changing page. Connected to buttons in qt_classes.py.
def change_page(self, previous_page=None, page=None):
    # Resets button state
    if previous_page is not None:
        reset_button(self, previous_page)
    
    # Goes to new page
    if page == "home":
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.label_status.setText("Home")
        self.ui.btn_home.setStyleSheet(css_btn_pressed)
    elif page == "add":
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.label_status.setText("Add or remove data")
        self.ui.btn_add.setStyleSheet(css_btn_pressed)
    elif page == "view":
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.label_status.setText("View data")
        self.ui.btn_view.setStyleSheet(css_btn_pressed)


# 3.4 RESET BUTTON - Resets button of previous page
def reset_button(self, page):
    if page == 0:
        self.ui.btn_home.setStyleSheet(css_btn_idle)
    if page == 1:
        self.ui.btn_add.setStyleSheet(css_btn_idle)
    if page == 2:
        self.ui.btn_view.setStyleSheet(css_btn_idle)


# 3.5 CHANGE DATABASE - Changes the database and updates values on home page
def change_database(self):
    # Get selection
    current_db_name = self.ui.tree_select_database.currentItem().text(0)

    # Set text
    self.ui.label_current_database.setText(current_db_name)

    # Set sample n 
    self.ui.label_n_samples.setText(str(n_samples(current_db_name, Blood)))

    ## TODO 
    # CREATION DATE
        # I need to define new variables in the SQL file. 
        # Dont delete files, just hide it using a hide column.
        # Do min value on datetime

    ## TODO
    # LAST EDITED
        # Do max value on datetime to find this


# 3.6 LOAD SQL DATA - Loads the data in the currenrly selected db and table and displays it in tablewidget
def load_sql_data(self):
    # Selected item
    selected_db = self.ui.tree_select_database.currentItem().text(0)

    # Load column names
    columns = sql_column_keys(database=selected_db, table=Blood)

    # Set table and row count
    self.ui.tableWidget_db_view.setRowCount(int(n_samples(database=selected_db, table=Blood))) # Row
    self.ui.tableWidget_db_view.setColumnCount(len(columns)) # Column
    
    # Write column names to widget
    for i, column in enumerate(columns):
        # Create widget
        self.ui.tableWidget_db_view.setHorizontalHeaderItem(i, QTableWidgetItem())

        # Set widget column text
        widgetColumn = self.ui.tableWidget_db_view.horizontalHeaderItem(i)
        widgetColumn.setText(QCoreApplication.translate("MainWindow", column, None));       
    
    # Get data from SQL database
    sql_data = sql_to_dict(database=selected_db, table=Blood)
    
    # Write to  QTableWidget
    for i, data in enumerate(sql_data):
        for j, column in enumerate(columns):
            self.ui.tableWidget_db_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.__dict__[column])))