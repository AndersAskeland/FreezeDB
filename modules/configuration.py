import os, sys, shutil
from datetime import date
from configparser import ConfigParser
from modules.helpers import resource_path, get_path, resource_path, get_session, get_engine
from modules.constants import CONFIG_DIR
from modules.dialogs import FirstTimeSetup
from sqlalchemy.sql.sqltypes import String, Date, Integer, Boolean

class Config:
    ''' Class attributes '''
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

    # Reset main config 
    def reset_config(self):
        # Find data dir from old file
        self.config.read(main_dir)
        dir_data = self.main_config.get("general", "dir")

        # Replace file with default
        shutil.copy2(default_dir, main_dir)

        # Write data dir back
        self.config.read(main_dir)
        self.config.set("general", "dir", dir_data)
        self.write_to_config(path=main_dir, config=self.config)


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
        
    ''' Functions '''
    # Set theme
    def change_theme(self, theme):
        # Change setting
        self.config.set("general", "theme", theme)

        # Write
        self.write_to_config(self.path, self.config)

    # Set currently selected database
    def set_database(self, database_index):
        self.config.set("general", "selected_db", str(database_index))

        self.write_to_config(self.path, self.config)
    
    # Create new database
    def create_database(self, database_name):
        # Variables
        index = len(self.config.items("database_names"))
        date_time  = date.today().strftime("%Y-%m-%d")  

        # Add database to end
        self.config.set("database_names", str(index), str(database_name))
        self.config.set("database_creation_date", str(index), str(date_time))

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



class ConfigTemplate(ConfigMain):
    ''' Class attributes '''

    ''' Instance attributes '''
    def __init__(self):
        # Classes
        self.config_main = ConfigMain()
        # Variables
        self.template_name = self.config_main.selected_template
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


