# -----------------------------------------------------------------------------
# Module: Configuration     
#
# What: Property classifications as done in qtDesigner.   
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules
import os, sys, shutil
from datetime import date
from configparser import ConfigParser
from modules.helpers import resource_path, get_path, resource_path, get_session, get_engine
from modules.constants import CONFIG_DIR
from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtCore import QSize, QPropertyAnimation, QEasingCurve, QCoreApplication
from sqlalchemy.sql.sqltypes import String, Date, Integer, Boolean

# Local functions 

# Local classes 
from modules.dialogs import FirstTimeSetup

# Local resources


# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class Config:
    ''' Default config behaviours '''
    
    base_dir = resource_path(CONFIG_DIR)
    main_dir = resource_path(CONFIG_DIR + "config.ini")
    default_dir = resource_path(CONFIG_DIR + "config_default.ini")
    config = ConfigParser()


    ''' Functions '''
    # Read config 
    def read_config(self, path):
        # If config exists
        if os.path.exists(path):
            self.config.read(path)
            return self.config

        # If creating new
        else: 
            config = self.set_default()
            return self.config
    
    # Sets default config 
    def set_default(self):
        # Copy
        shutil.copy2(self.default_dir, self.main_dir)

        # Get data dir
        data_dir =  FirstTimeSetup().data_folder() 

        # Show first time setup dialog
        self.config.read(self.main_dir)
        self.config.set("general", "dir", str(data_dir))
        
        # Write to db
        self.write_to_config(path=self.main_dir, config=self.config)
        
        # Return
        return self.config

    # Reset main config to template config file
    def reset_config(self):
        # Find data dir from old file
        self.config.read(self.main_dir)
        dir_data = self.main_config.get("general", "dir")

        # Replace file with default
        shutil.copy2(self.default_dir, self.main_dir)

        # Write data dir back
        self.config.read(self.main_dir)
        self.config.set("general", "dir", dir_data)
        self.write_to_config(path=self.main_dir, config=self.config)


    # Write to config
    def write_to_config(self, path, config):
        with open(path, "w") as pref:
            config.write(pref)



# Configuration class for main config
class ConfigMain(Config):
    ''' Instance attributes '''
    def __init__(self):
        # Read
        self.path = self.main_dir
        self.config = self.read_config(path=self.path)

        # Items
        self.selected_database = self.config.get("general", "selected_db")
        self.selected_theme = self.config.get("general", "theme")
        self.selected_template = self.config.get("general", "current_template")
        self.data_dir = self.config.get("general", "dir")

        # Sections
        self.section_database_names = self.config.items("database_names")
        self.section_database_creation_dates = self.config.items("database_creation_date")
        
    ''' Functions '''
    # Set theme
    def change_theme(self, theme):
        # Change setting
        self.config.set("general", "theme", theme)

        # Write
        self.write_to_config(self.path, self.config)
    
    # Get template of database
    def read_template(self, index):
        return self.config.get("database_template", str(index))
    
    # Set currently selected database
    def set_database(self, database_index):
        self.config.set("general", "selected_db", str(database_index))

        self.write_to_config(self.path, self.config)
    
    # Create new database
    def create_database(self, database_name, template):
        # Variables
        index = len(self.config.items("database_names"))
        date_time  = date.today().strftime("%Y-%m-%d")  

        # Add database to end
        self.config.set("database_names", str(index), str(database_name))
        self.config.set("database_creation_date", str(index), str(date_time))
        self.config.set("database_template", str(index), str(template))
        
        # Write
        self.write_to_config(self.path, self.config)

    # Remove database
    def delete_database(self, index):
        # Remove option
        self.config.remove_option("database_names", str(index))
        self.config.remove_option("database_creation_date", str(index))

        # Reset selected_db option
        self.config.set("general", "selected_db", "none")

        # Write
        self.write_to_config(self.path, self.config)

    # Update database list
    def update_database_list(self):
        # Variables
        databases_n = len(self.config.items("database_names"))
        removed_database = False

        # Logic
        for i in range(databases_n):
            # Variables
            database_index = self.config.items("database_names")[i][0]
            database_name = self.config.items("database_names")[i][1]
            database_creation_date = self.config.items("database_creation_date")[i][1]

            # Check
            if database_index == str(i): # Deleted item
                pass
            else:
                # Set new
                self.config.set("database_names", str(i), str(database_name))
                self.config.set("database_creation_date", str(i), str(database_creation_date))

                # Remove previous
                self.config.remove_option("database_names", (str(database_index)))
                self.config.remove_option("database_creation_date", str(database_index))

                # Check if removed from list
                if removed_database == False:
                    removed_database = True

        # Check if item was removed
        if removed_database:
            self.config.remove_option("database_names", str(databases_n))
            self.config.remove_option("database_creation_date", str(databases_n))

        # Write
        self.write_to_config(self.path, self.config)

    
    # ----------------- #
    #      UI view      #
    # ----------------- #
    ''' Updates the lists showing avaliable databases (Reading from config file). ''' 
    def ui_update_database_list(self, interface):
        # Clear previous tree view
        interface.ui.tree_databaseViewHome.clear()
        interface.ui.tree_databaseViewAdd.clear()

        # Get variables
        database_names = self.section_database_names
        database_creation_dates = self.section_database_creation_dates

        # for item in 
        for database in database_names:
            # Create QTreeWidget item
            QTreeWidgetItem(interface.ui.tree_databaseViewHome)
            QTreeWidgetItem(interface.ui.tree_databaseViewAdd)

            # Set QTreeWidget attributes
            item_home = interface.ui.tree_databaseViewHome.topLevelItem(int(database[0]))
            item_add = interface.ui.tree_databaseViewAdd.topLevelItem(int(database[0]))

            item_home.setText(0, QCoreApplication.translate("MainWindow", database[1], None)) 
            item_add.setText(0, QCoreApplication.translate("MainWindow", database[1], None))

        for date in database_creation_dates:
            item_home = interface.ui.tree_databaseViewHome.topLevelItem(int(date[0]))
            item_add = interface.ui.tree_databaseViewAdd.topLevelItem(int(date[0]))
            item_home.setText(1, QCoreApplication.translate("MainWindow", date[1], None)) 
            item_add.setText(1, QCoreApplication.translate("MainWindow", date[1], None)) 
    
    
    ''' Updates the lists showing avaliable databases (Reading from config file). ''' 
    def ui_database_selection(self, interface):
        # Check if db is not selected
        if self.selected_database == "none":            
            # Set output text to no selection
            self.ui.output_databaseTable__text_xl2.setText("No database selected")
            self.ui.output_dbSelection__text_lg__font_bold_2.setText("No selection")
            self.ui.output_dbSelection__text_lg__font_bold.setText("No selection")
        else:
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


class ConfigTemplate(ConfigMain):
    ''' Class attributes '''

    ''' Instance attributes '''
    def __init__(self, template):
        # Classes
        self.config_main = ConfigMain()

        # Variables
        self.template_name = template
        self.path = self.base_dir + self.template_name + ".ini"
        self.config = self.read_config(path=self.path)

        # Items # TODO: Append the two lists?
        self.required_fields = self.config.items("required_columns")
        self.optional_fields = self.config.items("optional_columns")

  
        # Lists
        self.list_section = [item[0] for item in self.required_fields]
        self.column_names = [(item[1].split(";")[0]) for item in self.required_fields]
        self.column_types = [eval((item[1].split(";")[1])) for item in self.required_fields]
        self.nullable_flags = [eval((item[1].split(";")[2])) for item in self.required_fields]
        self.primary_keys = [eval((item[1].split(";")[3])) for item in self.required_fields]
        

    ''' Functions '''
    def test(self):
        print(self.list_section)
        print(self.column_names)
        print(self.column_types)
        print(self.nullable_flags)
        print(self.primary_keys)


