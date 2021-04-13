# ----------------------------------------------------------------------------- #
# Title: Functions/slots                                                        #
#                                                                               #
# What: All functions used in program.                                          #
#                                                                               #
# ----------------------------------------------------------------------------- #

# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
''' External modules '''
import os, sys
from glob import glob
from datetime import date
from configparser import ConfigParser
from PySide2 import QtCore
from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtCore import QPropertyAnimation, QCoreApplication
from PySide2.QtGui import QColor, QPalette
from sqlalchemy.ext.declarative import declarative_base

''' Local modules '''
from modules.classes import Db, Database, Base, Settings, Metadata
from modules.helpers import get_path, get_engine, get_session, resource_path, print_message, get_database_path
from modules.constants import CONFIG_DIR, STYLE_DARK, STYLE_LIGHT
from modules.configuration import ConfigMain, Config, ConfigTemplate
from modules.database import Database2

''' Local resources '''

# ------------------------------------------------------------- #
# 2 - SETTING, CONSTANTS, AND HELPER FUNCTIONS                  #
# ------------------------------------------------------------- #



# ------------------------------------------------------------- #
# 3 - UI functions                                              #
# ------------------------------------------------------------- #
# --------------------------- #
# 3.1 - Change theme          #
# --------------------------- # 
''' Connected to custom theme change widget - changes the theme from dark to light. '''
def ui_change_theme(self): # UPDATED
    ### Debug/print ###
    print("[UI] - Changing theme.")
    
    ### Classes ###
    palette = QPalette()
    config = ConfigMain()
    
    ### Variables ###
    dark_theme_dir = resource_path(STYLE_DARK)
    light_theme_dir = resource_path(STYLE_LIGHT) 
    button_state = self.ui.animate_toggle.isChecked()

    ### Error handling ###

    ### Logic ###
    if button_state:
        # Dark theme
        theme = "dark"
        self.setStyleSheet(open(dark_theme_dir, "r").read()) # Dark
        
        palette.setColor(QPalette.Window, QColor(27, 29, 35))
        self.setPalette(palette)
    else:
        # Light theme
        self.setStyleSheet(open(light_theme_dir, "r").read()) # Dark
        theme = "light"

        # TODO - Palette

    # Save to config
    config.change_theme(theme)

# --------------------------- #
# 3.2 - Load theme          #
# --------------------------- # 
''' Loads theme from settings file. '''
def ui_load_theme(self): # UPDATED
    ### Debug/print ###
    print("[UI] - Loading theme.")
    
    ### Class instances ###
    palette = QPalette()
    config = ConfigMain()
    
    ### Constants ###
    dark_theme_dir = resource_path(STYLE_DARK)
    light_theme_dir = resource_path(STYLE_LIGHT) 
    theme = config.selected_theme

    ### Logic ###
    if theme == "dark":
        # Dark theme
        self.setStyleSheet(open(dark_theme_dir, "r").read()) # Dark
        self.ui.animate_toggle.setChecked(True)

        palette.setColor(QPalette.Window, QColor(27, 29, 35))
        self.setPalette(palette)

    else:
        # Light theme
        self.setStyleSheet(open(light_theme_dir, "r").read()) # Dark)

        # TODO - Palatte


# --------------------------- #
# 3.3 - Sidebar toggle        #
# --------------------------- # 
''' Animation and logic for the sidebar toggle menu. '''
def ui_menu_toggle(self): # UPDATED
    ### Debug/print ###
    print(f"[UI] Sidebar toggle menu activated.")

    ### Class instances ###

    ### Constants ###
    current_width = self.ui.sidebar_left.width()

    ### Logic ###
    # Define animation
    self.animation = QPropertyAnimation(self.ui.sidebar_left, b"minimumWidth")
    self.animation.setDuration(300)
    self.animation.setStartValue(current_width)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

    # Set needed width
    if current_width != 200:
        self.animation.setEndValue(200)
    else:
        self.animation.setEndValue(65)

    # Run
    self.animation.start()


# --------------------------- #
# 3.4 - Change page           #
# --------------------------- # 
''' Changes the page when button is pressed. Also manages css states for the buttons. '''
def ui_change_page(self, previous_page=None, page=None): # TODO - create custom button class for page buttons
    ### Debug/print ###
    print(f"[UI] Changing page to '{page}'")

    ### Class instances ###

    ### Variables ###

    ### Logic ###
    # Change page
    if page == "home" and previous_page != 0:
        self.ui.pageWidget.setCurrentIndex(0)
        self.ui.txt_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Home</span></p></body></html>", None))
        self.ui.btn_home__btn_large.setStyleSheet("background-color: rgb(85, 170, 255)")
    elif page == "add" and previous_page != 1:
        self.ui.pageWidget.setCurrentIndex(1)
        self.ui.txt_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Add or remove data</span></p></body></html>", None))
        self.ui.btn_add__btn_large.setStyleSheet("background-color: rgb(85, 170, 255)")
    elif page == "view" and previous_page != 2:
        self.ui.pageWidget.setCurrentIndex(2)
        self.ui.txt_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">View data</span></p></body></html>", None))
        self.ui.btn_data__btn_large.setStyleSheet("background-color: rgb(85, 170, 255)")
    else:
        return 0

    # Resets previous button
    if previous_page == 0:
        self.ui.btn_home__btn_large.setStyleSheet("background-color: rgb(27, 29, 35)")
    elif previous_page == 1:
        self.ui.btn_add__btn_large.setStyleSheet("background-color: rgb(27, 29, 35)")
    elif previous_page == 2:
        self.ui.btn_data__btn_large.setStyleSheet("background-color: rgb(27, 29, 35)")

# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #









# ------------------------------------------------------------- #
# 4 - Configuration functions                                   #
# ------------------------------------------------------------- #
# --------------------------- #
# 4.1 - Set default config.   # # TODO: It might be better to use config within the specific functions - Less mess.
# --------------------------- # 
''' Checks if config exits - if not - creates new config. '''
def config_check(): # UPDATED
    ### Debug/print ###
    print("[CONFIG] - Check if config is created.")

    ### Class instances ###

    ### Constants ###

    ### Logic ###
    ConfigMain()

# --------------------------- #
# 4.2 - Add database          #
# --------------------------- # 
''' Add database to config file. '''
def config_add_database(database_name): # UPDATED
    ### Print/debug ###
    print("[CONFIG] - Adding database to config file.")

    ### Class instances ###
    config = ConfigMain()

    ### Error handling ###
   
    ### Logic ###
    config.create_database(database_name)


# --------------------------- #
# 4.3 - Delete database       #
# --------------------------- # 
''' Deletes database from config file. '''
def config_delete_database(index, database): # TODO: Check if name is correct.
    ### Print/debug ###
    print("\t[CONFIG]\n Deleting database from config file.")

    ### Class instances ###
    config = ConfigMain()

    ### Constants ###
    config_database_name = config.selected_database

    ### Error handling ###
    if str(index) != str(config_database_name):
        print("[ERROR] - Database names are not matching.")
        return 0

    ### Logic ###
    config.delete_database(index=index)
    config.update_database_list()


# --------------------------- #
# 4.3 - Update database       #
# --------------------------- # 
''' Updates databases in config file. '''
def config_update_database_list(): # UPDATED - TODO: I might not need this. Run it within functions 
    ### Print/debug ###
    print("\t[CONFIG]\n Updating database list inside config file.")

    ### Class instances ###
    config = ConfigMain()
    
    ### Constants ###

    ### Error handling ###

    ### Logic ###
    config.update_database_list()
    

# --------------------------- #
# 4.4 - Set current db        #
# --------------------------- # 
''' Writes currently selected db to config file '''
def config_db_selection(item_index): # UPDATED
    ### Print/debug ###
    print("[CONFIG] Setting selected db to config")

    ### Classes ###
    config = ConfigMain()

    ### Variables ###

    ### Error handling ###

    ### Logic ###
    config.set_database(item_index)


# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #





# ------------------------------------------------------------- #
# 5 - Database functions                                        #
# ------------------------------------------------------------- #
# --------------------------- #
# 5.1 - Creates new db        #
# --------------------------- # 
def database_create(self):
    ### Print/debug ###
    print_message(function="database", message="Creating new database.")

    ### Classes ###
    config_main = ConfigMain()
    config_template = ConfigTemplate()
    database = Database2()

    ### Variables ###
    database_name = self.ui.input_createDatabase.text()
    data_dir = config_main.data_dir
    database_path = get_database_path(data_dir=data_dir, database_name=database_name)
    selected_template = config_template.template_name
    
    ### Error handling ###
    if os.path.exists(database_path):
        print_message(function="error", message="Database allready exist.")
        return 0
    elif database_name == "":
        print_message(function="error", message="Database must have a name.")
        return 0

    ### Logic ###
    self.ui.input_createDatabase.clear() 

    # Create database
    table = database.create_database(database_name=database_name, selected_template=selected_template, database_path=database_path)


    # Write to config
    config_add_database(database_name=database_name)

    update_dbList(self)

    # Update current selection
    update_selected_db(self)


''' Creates a new database. Only run when a new database is first created '''
def db_create(self):
    ### Debug/print ###
    print_message(function="database", message="Creating new database.")

    # Extract input & clear
    db_name = self.ui.input_createDatabase.text()
    self.ui.input_createDatabase.clear()
    
    # Get data
    db_dir = Settings().item_dir
    path = get_path(db_name, db_dir)

    # Error handling
    if os.path.exists(path):
        print("        [ERROR] - Database already exist.")
        return 0
    elif db_name == "":
        print("        [ERROR] - Database must have a name.")
        return 0

    # Create database
    engine = get_engine(path)

    # Write data to db
    Base.metadata.create_all(engine)

    # Write metadata 
    metadata = Metadata(freezedb=True, layout_name="Default")
    session = get_session(path)
    session.add(metadata)
    session.commit()    

    # Write to config
    config_add_database(database_name=db_name)

    # Update db list
    update_dbList(self)

    # Update current selection
    update_selected_db(self)

    # Message
    print(f"        [SUCCESS] - Database created!")



# --------------------------- #
# 5.2 - Delete database       #
# --------------------------- # 
''' Deletes the selected database '''
def db_delete(self):
    # Debug/print
    print(f"[Database] Deleting database")
    
    # Get index and name
    index = self.ui.tree_databaseViewHome.currentIndex().row()
    db_name = self.ui.tree_databaseViewAdd.currentItem().text(0)

    # Delete db
    db.delete_db()
    print("        [STATUS] - Database physically deleted")

    # Delete from config
    config_delete_database(database=db_name, index=index)
    print("        [STATUS] - Database removed from config")
    
    # Update config
    config_update_database_list()
    print("        [STATUS] - Config file updated database list.")
    
    # Update db list
    update_dbList(self)

    # Update to default settings
    update_selected_db(self)
    
    # Message
    print("        [SUCCESS] - Database deleted")


# --------------------------- #
# 5.3 - Reads db from dir     #
# --------------------------- # 
def db_check(self):
    # Print/debug
    print(f"[Database] Reading databases from data dir")

    # Read settings
    config = Settings()

    # Create lists
    config_db = []
    dir_db = []

    # Get db lists
    for db in config.section_database_names: # Config
        config_db.append(db[1])
    
    for f in glob(config.item_dir + "*.db"): # Dir
        base_name = os.path.basename(f)
        dir_db.append(os.path.splitext(base_name)[0])
    
    # Checks
    for item in dir_db: # Dir files in config
        if item in config_db:
            print(f"        [STATUS] - Config entry: {item} found. Doing nothing.")
        else:
            # Write to config
            config_add_database(database_name=item)

            # Update db list
            #  update_dbList(self)

            # Print/debug
            print(f"        [STATUS] - Config entry: {item} missing. Writing to config")
            
    for index, item in enumerate(config_db): # Config files not in dir!
        if item not in dir_db:
            # Remove from config
            config_delete_database(database=item, index=index)
            config_update_database_list()
            # update_dbList(self)
            
            # Print/debug
            print(f"        [STATUS] - Dir file: {item} missing. Removing from config.")
        else:
            # Print/debug
            print(f"        [STATUS] - Dir file {item} found. Doing nothing.")


# --------------------------- #
# 5.4 - Sets active database  #
# --------------------------- # 
''' Select and create active database '''
def db_active(self):
    # Debug/print
    print(f"[Database] Setting active DB")

    # Get current window
    page_index = self.ui.pageWidget.currentIndex()

    # Get selected item
    if page_index == 0:   
        # Get current selection
        ui_item = self.ui.tree_databaseViewHome.currentItem()
        db_name = ui_item.text(0)
        item_index = self.ui.tree_databaseViewHome.indexOfTopLevelItem(ui_item)

        # Update all other page locations
        self.ui.tree_databaseViewAdd.setCurrentItem(self.ui.tree_databaseViewAdd.topLevelItem(item_index))
    
    elif page_index == 1:   
        # Get current selection
        ui_item = self.ui.tree_databaseViewAdd.currentItem()
        db_name = ui_item.text(0)
        item_index = self.ui.tree_databaseViewAdd.indexOfTopLevelItem(ui_item)
        
        # Update all other page locations
        self.ui.tree_databaseViewHome.setCurrentItem(self.ui.tree_databaseViewHome.topLevelItem(item_index))
    
    # Initilize global db class
    global db
    db = Db(database=db_name)

    # Update current selection to config
    config_db_selection(item_index)
    
    # Update view
    db.update_view(self)

    # Message
    print(f"        [SUCCESS] - Database '{db_name}' activated")

# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #







# ------------------------------------------------------------- #
# 6 - Update functions                                          #
# ------------------------------------------------------------- #
# --------------------------- #
# 6.1 - Updates db tree list  #
# --------------------------- # 
''' Updates the lists showing avaliable databases. Reads the config file. '''
def update_dbList(self):
    # Debug/print
    print(f"[Update] Updating database list")

    # Clear previous tree view
    self.ui.tree_databaseViewHome.clear()
    self.ui.tree_databaseViewAdd.clear()

    # Read settings
    config = Settings()
    db_names = config.section_database_names
    db_creation_date = config.section_database_creation_date

    # Set name
    for item in db_names:
        # Create item
        QTreeWidgetItem(self.ui.tree_databaseViewHome)
        QTreeWidgetItem(self.ui.tree_databaseViewAdd) 

        # Set item
        item_home = self.ui.tree_databaseViewHome.topLevelItem(int(item[0]))
        item_add = self.ui.tree_databaseViewAdd.topLevelItem(int(item[0]))
        item_home.setText(0, QCoreApplication.translate("MainWindow", item[1], None)) 
        item_add.setText(0, QCoreApplication.translate("MainWindow", item[1], None))
    
    # Set creation date
    for item in db_creation_date:
        item_home = self.ui.tree_databaseViewHome.topLevelItem(int(item[0]))
        item_add = self.ui.tree_databaseViewAdd.topLevelItem(int(item[0]))
        item_home.setText(1, QCoreApplication.translate("MainWindow", item[1], None)) 
        item_add.setText(1, QCoreApplication.translate("MainWindow", item[1], None)) 

    # Message
    print("        [SUCCESS] - Database list updated.")


# --------------------------- #
# 6.2 - Updates current db    #
# --------------------------- # 
''' Updates the view to represent the currently selected db - Reads config file. '''
def update_selected_db(self):
    # Debug/print
    print(f"[Update] Setting currently selected DB")

    # Read config
    config = Settings()
    db_index = config.item_current_db
    

    # Check if db is not selected
    if db_index == "none":
        # Progress message
        print("        [STATUS] - Currently no selection - Setting no selection")
        
        # Set output text to no selection
        self.ui.output_databaseTable__text_xl2.setText("No database selected")
        self.ui.output_dbSelection__text_lg__font_bold_2.setText("No selection")
        self.ui.output_dbSelection__text_lg__font_bold.setText("No selection")
    # If there is selection
    else:
        # Progress message
        print("        [STATUS] - Setting db selection")

        try:
            # Get Qitem
            q_tree_widget_item = self.ui.tree_databaseViewHome.topLevelItem(int(db_index))

            # Set selection
            self.ui.tree_databaseViewHome.setCurrentItem(q_tree_widget_item)
            self.ui.tree_databaseViewAdd.setCurrentItem(q_tree_widget_item)

            # Get DB name and update view
            db_name = q_tree_widget_item.text(0)
            db = Db(database=db_name)
            db.update_view(self)
        except:
            return

    # Message
    print("        [SUCCESS] - Currently selected db is set")


# --------------------------- #
# 6.3 - Change theme          #
# --------------------------- # 
''' Changes the theme '''
def update_theme(self):
    # Debug/print
    print("[Update] - Changing theme.")

    # Read settings & create palette
    config = Settings()
    palette = QPalette()

    # Constant paths
    dark_path = resource_path(STYLE_DARK)
    light_path = resource_path(STYLE_LIGHT)

    # Set theme
    if config.item_theme == "dark":
        # Stylesheet
        self.setStyleSheet(open(dark_path, "r").read()) # Dark
        self.ui.animate_toggle.setChecked(True)

        # Palette 
        palette.setColor(QPalette.Window, QColor(27, 29, 35))
        self.setPalette(palette)

    elif config.item_theme == "light":
        # Style sheet
        self.setStyleSheet(open(light_path, "r").read()) # light

        # Palette
    
    # Message
    print(f"        [SUCCESS] - Changed theme to {config.item_theme}")
       

# ---------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------- #
