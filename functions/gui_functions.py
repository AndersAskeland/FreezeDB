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
from datetime import date
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QTreeWidgetItem, QTableWidgetItem
from PySide6.QtCore import QCoreApplication, QPropertyAnimation

# Internal modules
from ui.css import css_btn_pressed, css_btn_idle
from functions.sql_functions import n_samples, sql_column_keys, sql_to_dict, create_database, engine_connect, max_identifier, add_sql_data, delete_sql_data
from functions.settings_functions import config_check_selected_db, config_write_selected_db
from classes.sql_classes import Database

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

    # Clear item
    self.ui.tree_select_database.clear()
    self.ui.tree_select_database_2.clear()


    for file in os.scandir("databases"):
        print(file.name)
        if file.name.endswith(".db") or file.name == ".db":
            print(f"Creating input for {file} at id {i}")
            # Create item
            QTreeWidgetItem(self.ui.tree_select_database)
            QTreeWidgetItem(self.ui.tree_select_database_2)

            # Set item name
            item = self.ui.tree_select_database.topLevelItem(i)
            item.setText(0, QCoreApplication.translate("MainWindow", file.name[:-3], None))
            item2 = self.ui.tree_select_database_2.topLevelItem(i)
            item2.setText(0, QCoreApplication.translate("MainWindow", file.name[:-3], None))


            
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
def change_database(self, button): 
    # Find button pressed
    if button == 1:
        # Get item, name and index
        item = self.ui.tree_select_database.currentItem()
        db_name = item.text(0)
        index = self.ui.tree_select_database.indexOfTopLevelItem(item)

        # Update other table location
        self.ui.tree_select_database_2.setCurrentItem(self.ui.tree_select_database_2.topLevelItem(index))


    elif button == 2:
        # Get item, name and index
        item = self.ui.tree_select_database_2.currentItem()
        db_name = item.text(0)
        index = self.ui.tree_select_database_2.indexOfTopLevelItem(item)

        # Update other table location
        self.ui.tree_select_database.setCurrentItem(self.ui.tree_select_database.topLevelItem(index))

    # Set text
    self.ui.label_current_database.setText(db_name)

    # Set sample n 
    self.ui.label_n_samples.setText(str(n_samples(db_name)))

    # Load new data into table
    load_sql_data(self)

    # Write selection data to settings file
    config_write_selected_db(index)

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
    columns = sql_column_keys(database=selected_db)

    # Set table and row count
    self.ui.tableWidget_db_view.setRowCount(int(n_samples(selected_db))) # Row
    self.ui.tableWidget_db_view.setColumnCount(len(columns)) # Column
    
    # Update text for table
    self.ui.label_14.setText("Table view for database: \"" + selected_db + "\".")

    # Write column names to widget
    for i, column in enumerate(columns):
        # Create widget
        self.ui.tableWidget_db_view.setHorizontalHeaderItem(i, QTableWidgetItem())

        # Set widget column text
        widgetColumn = self.ui.tableWidget_db_view.horizontalHeaderItem(i)
        widgetColumn.setText(QCoreApplication.translate("MainWindow", column, None))     
        print(column)
    # Get data from SQL database
    sql_data = sql_to_dict(database=selected_db, table=Database)
    
    # Write to  QTableWidget
    for i, data in enumerate(sql_data):
        for j, column in enumerate(columns):
            self.ui.tableWidget_db_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.__dict__[column])))


# 3.7 LOAD SETTINGS
def load_settings(self):
    # Database selection
    try:
        # Get index
        index = config_check_selected_db()

        # Set selection
        self.ui.tree_select_database.setCurrentItem(self.ui.tree_select_database.topLevelItem(index)) # Selects multisite
        self.ui.tree_select_database_2.setCurrentItem(self.ui.tree_select_database_2.topLevelItem(index)) # Selects multisite

        # Update number of samples
        self.ui.label_n_samples.setText(str(n_samples(self.ui.tree_select_database.currentItem().text(0))))

        # Set database text
        self.ui.label_current_database.setText(self.ui.tree_select_database.currentItem().text(0))

        # Load data
        load_sql_data(self)

    except:
        pass

    # TODO
    # More settings

# Create new db and update list
def new_database_creation(self):
    # Get db name
    db_name = get_line_text(self)

    # Check if file exsist - Throw exception
    if os.path.exists("databases/" + db_name + ".db"):
        print("Database allready exsists. Doing nothing")
    elif db_name == "":
        print("Database must have a name")
    else:
    # Create db
        create_database(db_name)

        # update db list
        update_db_list(self)


    # Update db list
    # load_sql_data(self)


# Get lineEdit and reset field
def get_line_text(self):
    # Get text
    text = self.ui.lineEdit.text()

    # Reset field
    self.ui.lineEdit.clear()

    # Return
    return(text)


# Add to db
def add_to_db(self):
    # Get current db
    db_name = self.ui.tree_select_database.currentItem().text(0)

    # Create DB session
    session = engine_connect(db_name)

    # Write error checking function
    # TODO 

    # Write data to class
    # Citrate
    add_sql_data(self, session=session, sample_type="Citrate", n=20, identifier=1001)

    # EDTA
    add_sql_data(self, session=session, sample_type="EDTA", n=20, identifier=2001)

    # Serum
    add_sql_data(self, session=session, sample_type="Serum", n=10, identifier=3001)

    # EDTA_EV
    add_sql_data(self, session=session, sample_type="EV_EDTA", n=10, identifier=4001)

    # Add to db
    session.flush()
    session.commit()

    # Update view
    load_sql_data(self)


# Remove from db
def remove_from_db(self):
    # get current db
    db_name = self.ui.tree_select_database.currentItem().text(0)

    # Create DB session
    session = engine_connect(db_name)


    delete_sql_data()

def delete_db(self):
    # Get currently selected db in view
    db_name = self.ui.tree_select_database.currentItem().text(0)

    # Delete file
    os.remove("databases/" + db_name + ".db")

    # update data table
    update_db_list(self)

    # Update db count and name
    self.ui.label_n_samples.setText("No selection")

    # Set database text
    self.ui.label_current_database.setText("No selection")

