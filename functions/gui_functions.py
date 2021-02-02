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
from PySide6.QtWidgets import QTreeWidgetItem, QTableWidgetItem, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QVBoxLayout, QGraphicsTextItem
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, Qt
from PySide6.QtGui import QColor, QPainter, QPen
from sqlalchemy import exc


# Internal modules
from ui.css import css_btn_pressed, css_btn_idle
from functions.sql_functions import n_samples, sql_column_keys, sql_to_dict, create_database, engine_connect, max_identifier, add_sql_data, delete_sql_data, db_query_sample_type, db_query_group, del_sql_entry
from functions.settings_functions import config_check_selected_db, config_write_selected_db, read_columns
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
    
    # Set selection to previous


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

    # Load columns
    load_column_names(self)


    # Change piechart
    self.ui.graphicsView.setScene(pie_chart(self))
    self.ui.graphicsView_2.setScene(pie_chart_2(self))

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

    # Load actual columns from db
    columns = sql_column_keys(database=selected_db)

    # Set table and row count
    self.ui.tableWidget_db_view.setRowCount(int(n_samples(selected_db))) # Row
    self.ui.tableWidget_db_view.setColumnCount(len(columns) - 5) # Column
    print(f"Rows were set to {int(n_samples(selected_db))}")

    # Update text for table
    self.ui.label_14.setText("Table view for database: \"" + selected_db + "\".") 

    # Get data from SQL database
    sql_data = sql_to_dict(database=selected_db)

    # Load pie charts
    self.ui.graphicsView.setScene(pie_chart(self))
    self.ui.graphicsView_2.setScene(pie_chart_2(self))
    
    # Load columns
    load_column_names(self)

    # Load data number
    self.ui.label_n_samples.setText(str(n_samples(self.ui.tree_select_database.currentItem().text(0))))

    # Write to  QTableWidget
    for i, data in enumerate(sql_data):
        for j, column in enumerate(columns):
            self.ui.tableWidget_db_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.__dict__[column])))


# 3.7 LOAD SETTINGS
def load_settings(self):
    # Database selection
    try:
        # Update pie_charts
        self.ui.graphicsView.setScene(pie_chart(self))
        self.ui.graphicsView_2.setScene(pie_chart_2(self))

        # Load column names
        load_column_names(self)
        # Get index
        index = config_check_selected_db()

        # Set selection
        self.ui.tree_select_database.setCurrentItem(self.ui.tree_select_database.topLevelItem(index)) # Selects multisite
        self.ui.tree_select_database_2.setCurrentItem(self.ui.tree_select_database_2.topLevelItem(index)) # Selects multisite

        # Update number of samples
        self.ui.label_n_samples.setText(str(n_samples(self.ui.tree_select_database.currentItem().text(0))))

        # Set database text
        self.ui.label_current_database.setText(self.ui.tree_select_database.currentItem().text(0))
        
        # Load pie_chart
        self.ui.graphicsView.setScene(pie_chart(self))
        self.ui.graphicsView_2.setScene(pie_chart_2(self))

        # Add CSS to item
        # Load data
        load_sql_data(self)



    except:
        pass

    # TODO
    # More settings

# Load column names
def load_column_names(self):
    # Load column names
    column_names = read_columns()
    
    # Make widget visible if hidden
    self.ui.tableWidget_db_view.horizontalHeader().setVisible(True)

    print(len(column_names))
    # Write column names to widget
    for i, column in enumerate(column_names):
        # Create widget
        self.ui.tableWidget_db_view.setHorizontalHeaderItem(i, QTableWidgetItem())

        # Set widget column text
        widgetColumn = self.ui.tableWidget_db_view.horizontalHeaderItem(i)
        widgetColumn.setText(QCoreApplication.translate("MainWindow", column, None))     
        
        print(f"Sat column name to: {column}")

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

    update(self)
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

    # Remove selections
    self.ui.lineEdit_add_participant_ID.clear()
    self.ui.lineEdit_add_visit.clear()
    self.ui.lineEdit_add_group.clear()

    # Update picharts



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

    # Clear table
    self.ui.tableWidget_db_view.clear()
    print("DB view was cleared")

    # Write new table
    load_column_names(self)

    # Update pie charts

    # Set text for table
    self.ui.label_14.setText("No database selected") 

    # Update db count and name
    self.ui.label_n_samples.setText("No selection")

    # Update pie_charts
    self.ui.graphicsView.setScene(pie_chart(self))
    self.ui.graphicsView_2.setScene(pie_chart_2(self))

    # Set database text
    self.ui.label_current_database.setText("No selection")








# Create pie charts
def pie_chart(self):
    print("\n\nPIE CHART 2")

    # Create scene and define settings
    self.scene = QGraphicsScene(self)
    colours = [QColor(97,158,97), QColor(235,142,64), QColor(197, 67, 62), QColor(83, 167, 185)] #  TODO update to prettier colours
    set_angle = 0 # Start angle

    # Get db name
    try:
        db_name = self.ui.tree_select_database.currentItem().text(0)
    except:
        # Create empty circle
        ellipse = QGraphicsEllipseItem(0,0,150,150) # Create an ciruclar ellispeitem
        ellipse.setBrush(QColor(235,142,64)) # Set color
        location = ellipse.boundingRect()


        # Set text
        text = QGraphicsTextItem("No database\nselected")
        text.setPos(location.center().x() - 25, location.center().y() - 15)

        # add stuff
        self.scene.addItem(ellipse)
        self.scene.addItem(text)        
        
        # Return
        return self.scene    
        
    # get data
    data = db_query_sample_type(self, db_name)
    words = ["Citrate", "EDTA", "Serum", "EV-EDTA"]

    # If empty - Add text to middle saying no selection
    if not data:
        # Create empty circle
        ellipse = QGraphicsEllipseItem(0,0,150,150) # Create an ciruclar ellispeitem
        ellipse.setBrush(QColor(235,142,64)) # Set color
        location = ellipse.boundingRect()


        # Set text
        text = QGraphicsTextItem("No data")
        text.setPos(location.center().x() - 24, location.center().y() - 15)

        # add stuff
        self.scene.addItem(ellipse)
        self.scene.addItem(text)        
        
        # Return
        return self.scene
    # Create pie chart
    for i, section in enumerate(data):
            # Create part of circle
            angle = round(float(section*5760)/sum(data))
            print(f"From angle is: {angle / 16}")
            print(f"To angle is: {set_angle / 16}")

            ellipse = QGraphicsEllipseItem(0,0,150,150) # Create an ciruclar ellispeitem
            ellipse.setStartAngle(set_angle) # from angle
            ellipse.setSpanAngle(angle) # to angle

            # Set text
            text = words[i]
            location = ellipse.boundingRect()
            text = QGraphicsTextItem(text)
            text.setPos(location.center().x() + 12, location.center().y() - 20)
            text.setRotation((angle / 16) / 2)
            
            print(f"Rotation is set to: {(angle / 16) - (set_angle / 16)}")
            
            ellipse.setBrush(colours[i]) # Set color

            # Change angle
            set_angle += angle

            # Edit with CSS
            # Add item
            self.scene.addItem(ellipse)
            self.scene.addItem(text)

    # Return scene
    return self.scene


def pie_chart_2(self):
    print("\n\nPIE CHART 2")
    # Create scene and define settings
    self.scene = QGraphicsScene(self)
    colours = [QColor(97,158,97), QColor(235,142,64), QColor(197, 67, 62), QColor(83, 167, 185)] #  TODO update to prettier colours
    set_angle = 0 # Start angle

    # Get db name
    try:
        db_name = self.ui.tree_select_database.currentItem().text(0)
    except:
        # Create empty circle
        ellipse = QGraphicsEllipseItem(0,0,150,150) # Create an ciruclar ellispeitem
        ellipse.setBrush(QColor(235,142,64)) # Set color
        location = ellipse.boundingRect()


        # Set text
        text = QGraphicsTextItem("No database\nselected")
        text.setPos(location.center().x() - 25, location.center().y() - 15)

        # add stuff
        self.scene.addItem(ellipse)
        self.scene.addItem(text)        
        
        # Return
        return self.scene    
    # get data
    data = db_query_group(self, db_name)
    words = ["Obese", "Control", "Other"]

    # If empty - Add text to middle saying no selection
    if not data:
        # Create empty circle
        ellipse = QGraphicsEllipseItem(0,0,150,150) # Create an ciruclar ellispeitem
        ellipse.setBrush(QColor(235,142,64)) # Set color
        location = ellipse.boundingRect()


        # Set text
        text = QGraphicsTextItem("No data")
        text.setPos(location.center().x() - 25, location.center().y() - 15)

        # add stuff
        self.scene.addItem(ellipse)
        self.scene.addItem(text)        
        
        # Return
        return self.scene
    # Create pie chart
    for i, section in enumerate(data):
            # Create part of circle
            angle = round(float(section*5760)/sum(data))
            ellipse = QGraphicsEllipseItem(0,0,150,150) # Create an ciruclar ellispeitem
            ellipse.setStartAngle(set_angle) # from angle
            ellipse.setSpanAngle(angle) # to angle
            print(f"From angle is: {angle / 16}")
            print(f"To angle is: {set_angle / 16}")

            # Set text
            text = words[i]
            location = ellipse.boundingRect()
            text = QGraphicsTextItem(text)
            text.setPos(location.center().x() + 12, location.center().y() - 20)
            text.setRotation((angle / 16) / 2)

            print(f"Rotation is set to: {(angle / 16) / 2}")
            ellipse.setBrush(colours[i]) # Set color

            # Change angle
            set_angle += angle

            # Edit with CSS
            # Add item
            self.scene.addItem(ellipse)
            self.scene.addItem(text)

    # Return scene
    return self.scene

def delete_entry_table(self):
    identifier = self.ui.tableWidget_db_view.item(self.ui.tableWidget_db_view.currentRow(), 1).text()
    db_name = self.ui.tree_select_database.currentItem().text(0)
    session = engine_connect(db_name)
    del_sql_entry(self, session=session, identifier=identifier)
    update(self)


def delete_entry(self):
    # Extract data
    # Get current db
    db_name = self.ui.tree_select_database.currentItem().text(0)

    # Extract selection
    identifier = int(self.ui.lineEdit_delete_identifier.text())

    # Create DB session
    session = engine_connect(db_name)

    # Write error checking function
    # TODO 
    
    # Write data to class
    # Citrate
    del_sql_entry(self, session=session, identifier=identifier)


    # Update view
    update(self)

    # Remove selections
    self.ui.lineEdit_delete_identifier.clear()




############################################################
################# Updated functions #######################
# Combined update function
def update(self):
    # If database selection is valid
    try:
        ### Get needed variables ###
        # Get selected DB
        database = self.ui.tree_select_database.currentItem().text(0)
        print("database was selected")

        # Get database column names
        columns = sql_column_keys(database=database)
        print("Colums keys was selected")

        # Get n of columns
        column_n = len(columns)

        # Get SQL_data into a dictionairy
        sql_data = sql_to_dict(database=database)
        print("database dict was selected")

        ### Write column names ###
        load_column_names_update(self, column_n)
        print("Column name was updated")

        ### Load data into table ###
        load_sql_data(self)
        print("Data in table was written")

        ### Update table header ###
        self.ui.label_14.setText("Table view for database: \"" + database + "\".") 
        print("Table heading name was updated")

        ### Update current database selection text ###
        self.ui.label_current_database.setText(database)
        print("Database text was selected")

        ### Update number of samples in database ###
        self.ui.label_n_samples.setText(str(n_samples(database)))
        print("Database n was selected")

        # Load pie charts
        self.ui.graphicsView.setScene(pie_chart(self))
        self.ui.graphicsView_2.setScene(pie_chart_2(self))

        # DEBUG - Print test
        print("Database was selected and update is completed")
    # If no database is selected
    except:
        # Set text for table
        self.ui.label_14.setText("No database selected") 

        # Update db count and name
        self.ui.label_n_samples.setText("No selection")

        # Update pie_charts
        self.ui.graphicsView.setScene(pie_chart(self))
        self.ui.graphicsView_2.setScene(pie_chart_2(self))

        # Set database text
        self.ui.label_current_database.setText("No selection")

        # Clear table
        self.ui.tableWidget_db_view.clear()
        print("clearing table")
        load_column_names_update(self, 0)


def load_settings_update(self):
    # Database selection
    try:
        # Update database list
        update_db_list(self)

        # Get index
        index = config_check_selected_db()

        print(f" Index is: {index}")
        # Set selection
        self.ui.tree_select_database.setCurrentItem(self.ui.tree_select_database.topLevelItem(index)) # Selects multisite
        self.ui.tree_select_database_2.setCurrentItem(self.ui.tree_select_database_2.topLevelItem(index)) # Selects multisite

        # Update everything
        print(f"Initial load function is running update")
        update(self)


    except:
        update(self)


# New update function for sql data
def load_sql_data_update(self, columns, sql_data):
    print(f"Writing table for {columns} with the following data: {sql_data}")

    # Write to  QTableWidget
    for i, data in enumerate(sql_data):
        for j, column in enumerate(columns):
            self.ui.tableWidget_db_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.__dict__[column])))
    print("Finished wrting data")

# New update function for setting column names
def load_column_names_update(self, column_n):
    # Set table visible if not allready
    self.ui.tableWidget_db_view.horizontalHeader().setVisible(True)

    if column_n == 0:
        self.ui.tableWidget_db_view.setColumnCount(1)
        self.ui.tableWidget_db_view.setRowCount(0)
        print("Rows were set to 0")

        self.ui.tableWidget_db_view.setHorizontalHeaderItem(0, QTableWidgetItem())
        widgetColumn = self.ui.tableWidget_db_view.horizontalHeaderItem(0)
        widgetColumn.setText(QCoreApplication.translate("MainWindow", "No data", None))     
    else:
        # Load column names
        column_names = read_columns()

        # Set column count
        self.ui.tableWidget_db_view.setColumnCount(column_n - 5)

        # Write column names to widget
        for i, column in enumerate(column_names):
            # Create widget
            print(column)
            self.ui.tableWidget_db_view.setHorizontalHeaderItem(i, QTableWidgetItem())

            # Set widget column text
            widgetColumn = self.ui.tableWidget_db_view.horizontalHeaderItem(i)
            widgetColumn.setText(QCoreApplication.translate("MainWindow", column, None))     

def delete_db_update(self):
    # Get currently selected db in view
    db_name = self.ui.tree_select_database.currentItem().text(0)
    print("db name is extracted")

    # Delete file
    os.remove("databases/" + db_name + ".db")

    # Clear table
    update_db_list(self)

    # update data table
    update(self)


# TODO
# Piechart text angle equal to angle start - angle end of ellipse. Maybe I can turn them around