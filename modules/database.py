# ----------------------------------------------------------------------------- #
# Module: Database                                                              #
#                                                                               #
# What: Controls database access.                                               #
#                                                                               #
# ----------------------------------------------------------------------------- #
# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
''' External modules '''
import os
from glob import glob
from datetime import date
from sqlalchemy import Column, ForeignKey, UniqueConstraint, Table, create_engine, MetaData
from sqlalchemy.orm import relationship, sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String, Date, Integer, Boolean

''' Local functions '''
from modules.helpers import resource_path, get_path, resource_path, get_session, get_engine, get_database_path, debug_print

''' Local classes '''
from modules.configuration import ConfigMain, ConfigTemplate

''' Local resources '''

# ------------------------------------------------------------- #
# 2 - Settings, constants, helper functions                     #
# ------------------------------------------------------------- #
''' Resets database tables '''
def database_reset():
    Database().clear_tables()

# ------------------------------------------------------------- #
# 3 - Classes                                                   #
# ------------------------------------------------------------- #
# --------------------------- #
# 3.1 - Database              #
# --------------------------- # 
''' Default database class. '''
class Database:
    # ----------------- #
    #     Attributes    #
    # ----------------- #
    Base = declarative_base()
    

    # ----------------- #
    #     Functions     #
    # ----------------- # 
    ''' Create new database '''
    def create_database(self, database_name, selected_template, database_path):
        # Classes
        config_template = ConfigTemplate(selected_template)

        # Variables
        date_time = date.today().strftime("%Y-%m-%d")

        # Read template
        dict_samples = self.read_template(config_template)

        # Create class
        type("Samples", (self.Base,), dict_samples)
        
        # Create database
        engine = get_engine(database_path)
        self.Base.metadata.create_all(engine)

        # Clear tables
        self.clear_tables()

    ''' Read data from template file. '''
    def read_template(self, template):
        # Database variables
        required_fields = template.required_fields
        optional_fields = template.optional_fields

        # Create dictionary
        dict_samples = {'__tablename__': 'samples'}
        dict_metadata = 0

        for item in required_fields:
            dict_samples[item[1].split(";")[0]] = Column(eval(item[1].split(";")[1]), primary_key=item[1].split(";")[3], nullable=item[1].split(";")[2])
        for item in optional_fields:
            dict_samples[item[1].split(";")[0]] = Column(eval(item[1].split(";")[1]), primary_key=item[1].split(";")[3], nullable=item[1].split(";")[2])
        
        # Return
        return dict_samples

    ''' Clear/deletes tables in metadata instance '''
    def clear_tables(self):
        self.Base.metadata.clear()



# --------------------------- #
# 3.2 - Selected database     #
# --------------------------- # 
''' Currently selected database. '''
class CurrentDatabase(Database):
    ''' Class attributes  '''

    
    ''' Instance attributes '''
    def __init__(self, database, template):
        # Classes
        config_main = ConfigMain()
        self.Database = self.activate_database(template) # Database class

        # General variables
        self.name = str(database)
        self.path = get_database_path(data_dir=config_main.data_dir, database_name=self.name)
        self.engine = get_engine(path=self.path)
        self.session = get_session(path=self.path)
        self.samples_n = self.number_of_samples()
    
    ''' Functions '''
    # Create database class
    def activate_database(self, selected_template):
        # Read template
        config_template = ConfigTemplate(selected_template)

        # Read template
        dict_samples = self.read_template(template=config_template)

        # Get class
        return type("Samples", (self.Base,), dict_samples)

    # Calculate number of samples
    def number_of_samples(self):
        return self.session.query(self.Database).filter(self.Database.delete == False).count()
    
    # Delete database
    def delete_db(self):
        print(self.path)
        os.remove(self.path)

    # Update GUI view
    def update_view(self, interface):
        # Update selection
        interface.ui.output_db_selection.setText(self.name) # Home
        interface.ui.output_database_selection_2.setText('Table view for database: "' + self.name + '".') # Add/update

        # Update number of samples
        interface.ui.output_number_of_samples.setText(str(self.samples_n))

    def clear_tables(self):
        self.Base.metadata.clear()




# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------------------- #
# 4 - Functions                                                 #
# ------------------------------------------------------------- #
# --------------------------- #
# 4.1 - Sets active database  #
# --------------------------- # 
''' Select and create active database '''
def database_activate(self):
    # ------------- #
    #     Debug     #
    # ------------- #
    debug_print(level="top", name="database", message="Setting active database.", function="database_activate")

    # ------------- #
    #    Classes    #
    # ------------- #
    config = ConfigMain()

    # ------------- #
    #   Variables   #
    # ------------- #
    page_index = self.ui.pageWidget.currentIndex()

    # ------------- #
    #     Error     #
    # ------------- #

    # ------------- #
    #     Logic     #
    # ------------- #
    # Reset tables from previous selection
    database_reset()

    # Get selected item
    if page_index == 0:   
        # Get current selection
        ui_item = self.ui.tree_databaseViewHome.currentItem()
        database_name = ui_item.text(0)
        item_index = self.ui.tree_databaseViewHome.indexOfTopLevelItem(ui_item)

        # Update all other page locations
        self.ui.tree_databaseViewAdd.setCurrentItem(self.ui.tree_databaseViewAdd.topLevelItem(item_index))
    
    elif page_index == 1:   
        # Get current selection
        ui_item = self.ui.tree_databaseViewAdd.currentItem()
        database_name = ui_item.text(0)
        item_index = self.ui.tree_databaseViewAdd.indexOfTopLevelItem(ui_item)
        
        # Update all other page locations
        self.ui.tree_databaseViewHome.setCurrentItem(self.ui.tree_databaseViewHome.topLevelItem(item_index))
    
    # Get template of database
    template_name = config.read_template(item_index)

    # Create database class
    global ActiveDatabase
    ActiveDatabase = CurrentDatabase(database=database_name, template=template_name)
    debug_print(level="sub", message=f"Set selected database to: \"{database_name}\".")

    # Write selection to config
    config.set_database(database_index=item_index)

    # Update view
    ActiveDatabase.update_view(interface=self)
    debug_print(level="sub", message="Updated UI view.")


# --------------------------- #
# 5.2 - Creates new db        #
# --------------------------- # 
''' Create a new database and write the info to the configuration file. '''
def database_create(self):
    # ------------- #
    #     Debug     # 
    # ------------- #    
    debug_print(level="top", name="Database", message="Creating new database.", function=database_create.__name__)

    # ------------- #
    #    Classes    # 
    # ------------- #
    config = ConfigMain()
    database = Database()

    # ------------- #
    #   Variables   # 
    # ------------- #    
    database_name = self.ui.input_createDatabase.text()
    data_folder = config.data_dir
    template_name = config.selected_template
    database_path = get_database_path(data_dir=data_folder, database_name=database_name)
    
    # ------------- #
    #     Error     # 
    # ------------- #  
    if os.path.exists(database_path):
        debug_print(level="error", message="Database already exists.")
        return 0
    elif database_name == "":
        debug_print(level="error", message="Database must have a name.")
        return 0

    # ------------- #
    #     Logic     # 
    # ------------- #
    # Reset previous selection
    database_reset()

    # Clear selection
    self.ui.input_createDatabase.clear() 

    # Create database
    database.create_database(database_name=database_name, selected_template=template_name, database_path=database_path)
    debug_print(level="sub", message=f"Created database: \"{database_name}.db\".")

    # Write to configuration file
    debug_print(level="sub", message=f"Adding database \"{database_name}\" to config file.")
    config.create_database(database_name=database_name, template=template_name)

    # Update view
    debug_print(level="sub", message=f"Database list is updated.")
    config.ui_update_database_list(interface=self)



# --------------------------- #
# 5.3 - Reads db from dir     #
# --------------------------- # 
def database_dir(self):
    # ------------- #
    #     Debug     #
    # ------------- #
    debug_print(level="top", name="Database", message="Checking databases in data dir and adding to config.", function="database_dir")

    # ------------- #
    #    Classes    #
    # ------------- #
    config_main = ConfigMain()

    # ------------- #
    #   Variables   #
    # ------------- #
    databases_in_config = []
    databases_in_dir = []
    selected_template = config_main.selected_template

    # ------------- #
    #     Error     #
    # ------------- #

    # ------------- #
    #     Logic     #
    # ------------- #
    # List of databases
    for database_config in config_main.section_database_names:
        databases_in_config.append(database_config[1])

    for database_dir in glob(config_main.data_dir + "*.db"):
        base_name = os.path.basename(database_dir)
        databases_in_dir.append(os.path.splitext(base_name)[0])

    # Directory files also in config
    for database_dir in databases_in_dir: 
        if database_dir in databases_in_config:
            # Debug message
            debug_print(level="sub", message=f"Config entry: \"{database_dir}\" found. Doing nothing.")
        else: # TODO: Will cause error. Don't know what template this is.
            # Debug message
            debug_print(level="sub", message=f"Config entry: \"{database_dir}\" missing. Adding it to config.")
    
            # Write to config 
            config_main.create_database(database_name=database_dir, template=selected_template) 

    # Config files also in directory
    for index, database_config in enumerate(databases_in_config):
        if database_config in databases_in_dir:
            # Debug message
            debug_print(level="sub", message=f"Directory file: \"{database_config}\" found. Doing nothing.")
        else:
            # Debug message
            debug_print(level="sub", message=f"Directory file: \"{database_config}\" missing. Removed from config file.")

            # Remove from config
            config_main.delete_database(index=index)

            # Update database list
            config_main.update_database_list()

# --------------------------- #
# 5.4 - Delete database       #
# --------------------------- #
''' Deletes the selected database '''
def database_delete(self): 
    # ------------- #
    #     Debug     #
    # ------------- #
    debug_print(level="top", name="Database", message="Deleting database from folder and from config file.", function=database_delete.__name__)
    
    # ------------- #
    #    Classes    #
    # ------------- #
    config_main = ConfigMain()
    database_name = config_main.selected_database
    template = config_main.selected_template

    # ------------- #
    #   Variables   #
    # ------------- #
    database_index = self.ui.tree_databaseViewHome.currentIndex().row() 

    # ------------- #
    #     Logic     #
    # ------------- #
    # Remove database from folder
    ActiveDatabase.delete_db()

    # Remove database from config
    config_main.delete_database(index=database_index)
    config_main.update_database_list()

    # Update database list
    config_main.ui_update_database_list(interface=self)

    # Update selected database
    # update_selected_db(self)
