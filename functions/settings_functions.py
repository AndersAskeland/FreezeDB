##################################################################################
##                                                                              ##
## Title: Settings functions                                                         ##
##                                                                              ##
## What: All functions related to the sqlalchemy.                               ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External
from configparser import ConfigParser
import os.path

##################################################################
## 2 - SETTINGS AND CONSTANTS                                   ##
##################################################################


##################################################################
## 3 - Functions                                                ##
##################################################################

# Checks if settings exsist
def config_exist():
    # Check if existing
    if os.path.exists("config.ini"):
        print("Settings file allready defined.")
        pass
    else:
        print("Setting default settings file.")

        # Connect to configparser
        config = ConfigParser()

        # Create config
        config['settings'] = {
            'selected_db': 'none',
            'user': 'root'
        }

        config["column_names"] = {
            'column_1': 'Participant ID',
            'column_2': 'Identifier',
            'column_3': 'Group',
            'column_4': 'Visit',
            'column_5': 'Sample type',
            'column_6': 'Date'
        }
        # Write to config
        with open('config.ini', 'w') as f:
            config.write(f)


# Check if settings.sections() exists
def config_section_exists(section):
    # Create connection
    parser = ConfigParser()
    parser.read('config.ini')

    # Check if section exsists
    if section in parser.sections():
        return True
    else:
        return False


# Reads for selected db
def config_check_selected_db():
    # Connection
    parser = ConfigParser()
    parser.read('config.ini')
    
    # Return
    return(int(parser.get('settings', 'selected_db')))



# Write selected db
def config_write_selected_db(index):
    # Connection
    parser = ConfigParser()
    parser.read('config.ini')

    # Set selected db
    with open('config.ini', 'w') as f:
        parser.set("settings", "selected_db", f"{index}")
        parser.write(f)
        print(f"Changed settings file to {index}")


# Read column names
def read_columns():
    # Connection
    parser = ConfigParser()
    parser.read('config.ini')

    # Extract column names
    columns = [option for option in parser['column_names']]
    
    # Extract data
    data = []
    for column in columns:
        data.append(parser.get('column_names', column))

    print("Read column function is done")
    return data