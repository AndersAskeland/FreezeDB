# ----------------------------------------------------------------------------- #
# Title: Classes                                                                #
#                                                                               #
# What: All the different classes used for program.                             #
#                                                                               #
# ----------------------------------------------------------------------------- #

# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
''' External modules '''
import os, sys
from datetime import date
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, create_engine, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean, Date
from PySide2.QtCore import Qt, QSize, QPoint, QPointF, QRectF, QEasingCurve, QPropertyAnimation, QSequentialAnimationGroup, Slot, Property
from PySide2.QtWidgets import QCheckBox
from PySide2.QtGui import QColor, QBrush, QPaintEvent, QPen, QPainter
from configparser import ConfigParser

''' Local modules '''
from modules.constants import CONFIG_DIR
from modules.dialogs import FirstTimeSetup
from modules.helpers import resource_path, get_path, resource_path, get_session, get_engine

''' Local resources '''

# ------------------------------------------------------------- #
# 2 - SETTING, CONSTANTS, AND HELPER FUNCTIONS                  #
# ------------------------------------------------------------- #
Base = declarative_base()


# ------------------------------------------------------------- #
# 3 - Classes                                                   #
# ------------------------------------------------------------- #

# --------------------------- #
# 3.1 - Database deceleration #
# --------------------------- # 
''' Default database class. TODO: Dynamically create db class based on settings. Probably best to use a INI file per format. Also create function that can read db classes from folder '''
class Database(Base):
    __tablename__ = "database"

    # Read template

    # Add columns
    participant_id = Column(Integer, nullable=False)
    identifier = Column(Integer, nullable=False, primary_key=True, unique=True)
    group = Column(String, nullable=False)
    visit = Column(String, nullable=False)
    sample_type = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    freeze_cycles = Column(Integer, nullable=True)
    operator = Column(String, nullable=True)
    location = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    delete = Column(Boolean, nullable=False)


    # Print method
    def __repr__(self):
        return(f"Database(Participant ID={self.participant_id}, identifier={self.identifier}, visit={self.visit}, sample type={self.sample_type}, date={self.date}, delete={self.delete}, freeze thaw cycles={self.freeze_cycles}, operator={self.operator}, location{self.location}, notes={self.notes})")

''' Metadata - Info about version of freezedb created in and layout name. '''
class Metadata(Base):
    __tablename__ = "metadata"

    freezedb = Column(Boolean, nullable=False)
    layout_name = Column(String, nullable=False, primary_key=True)
    creation_date = Column(Date, nullable=True)


class Database_new:
    def __init__(self, database):
        self.name = str(database)
        self.path = get_path(self.name, Settings().item_dir)
        self.engine = get_engine(self.path)
        self.session = get_session(self.path)
        self.n = self.number_of_samples()

    # Calculate number of samples
    def number_of_samples(self):
        return self.session.query(Database).filter(Database.delete == False).count()
    
    # Delete database
    def delete_db(self):
        os.remove(self.path)

    # Update GUI view
    def update_view(self, interface):
        # Update selection
        interface.ui.output_dbSelection__text_lg__font_bold.setText(self.name) # Home
        interface.ui.output_databaseTable__text_xl2.setText('Table view for database: "' + self.name + '".') # Add/update

        # Update number of samples
        interface.ui.output_dbSelection__text_lg__font_bold_2.setText(str(self.n))
    
    def create_database(database_name, column_names, column_types, primary_key_flags, nullable_flags, layout_name):
        # Variables
        metadata = MetaData(bind=engine)
        path = get_path(database_name, Settings().item_dir)
        
        # Tables
        main_table = Table('samples', metadata,
             *(Column(column_name, column_type,
                      primary_key=primary_key_flag,
                      nullable=nullable_flag)
               for column_name,
                   column_type,
                   primary_key_flag,
                   nullable_flag in zip(columns_names,
                                        columns_types,
                                        primary_key_flags,
                                        nullable_flags)))
        
        meta_table = Table('metadata', metadata,
                Column('freezedb', Boolean, True),
                Column('layout_name', String, layout_name),
                Column('creation_date', Date, date.today().strftime("%Y-%m-%d")))

        main_table.create()
        meta_table.create()


# --------------------------- #
# 3.2 - Selected database     #
# --------------------------- # 
''' Data associated to the currently selected database '''
class Db:
    def __init__(self, database):
        self.name = str(database)
        self.path = get_path(self.name, Settings().item_dir)
        self.engine = get_engine(self.path)
        self.session = get_session(self.path)
        self.n = self.number_of_samples()

    # Calculate number of samples
    def number_of_samples(self):
        return self.session.query(Database).filter(Database.delete == False).count()
    
    # Delete database
    def delete_db(self):
        os.remove(self.path)

    # Update GUI view
    def update_view(self, interface):
        # Update selection
        interface.ui.output_dbSelection__text_lg__font_bold.setText(self.name) # Home
        interface.ui.output_databaseTable__text_xl2.setText('Table view for database: "' + self.name + '".') # Add/update

        # Update number of samples
        interface.ui.output_dbSelection__text_lg__font_bold_2.setText(str(self.n))


# --------------------------- #
# 3.3 - Settings              #
# --------------------------- #  
class DatabaseTemplate():
    def __init__(self):
        self.path = resource_path(CONFIG_DIR)
        self.config = self.read()
        self.config.read(self.path)
    def read(self):
        # Create config class
        self.config = ConfigParser()

        with open(self.path, "w") as f:
            self.config.write(f)
        
        # Open newly created config
        self.config.read(self.path)
        return self.config


# --------------------------- #
# 3.4 - Settings              #
# --------------------------- # 
class Settings:
    def __init__(self):
        self.path = resource_path(CONFIG_DIR + "config.ini")
        self.config = self.read()

        # Items
        self.item_current_db = self.config.get("general", "selected_db")
        self.item_theme = self.config.get("general", "theme")
        self.item_dir = self.config.get("general", "dir")
        self.item_theme = self.config.get("general", "current_template")

        # Section lists
        self.section_general = self.config.items("general")
        self.section_database_names = self.config.items("database_names")
        self.section_database_creation_date = self.config.items("database_creation_date")

    # Read settings
    def read(self):
        # Create config class
        self.config = ConfigParser()

        # Check if config exists
        if os.path.exists(self.path):
            self.config.read(self.path)
            return self.config
        else: # Create new config
            # Create config
            self.config['general'] = {
            'selected_db': 'none',
            'user': 'root',
            'theme': 'light',
            'file_location': '/',
            'current_template': 'default',
            'dir': FirstTimeSetup().data_folder()
            }

            self.config["column_names"] = {
            'column_1': 'Participant ID',
            'column_2': 'Identifier',
            'column_3': 'Group',
            'column_4': 'Visit',
            'column_5': 'Sample type',
            'column_6': 'Date'
            }

            # TODO: Check if databases are present in data folder

            self.config["database_names"] = {

            }
        
            self.config["database_creation_date"] = {

            }

            self.config["template_name"] = {
                '1': 'default'
            }

        # Write
        self.write()

        # Open newly created config
        self.config.read(self.path)
        return self.config


    def write(self):
        with open(self.path, "w") as f:
            self.config.write(f)

    def config_set(self, section, index, content):
        self.config.set(section, str(index), content)

    # Set selected them
    def theme(self, theme):
        if theme:
            self.config_set("general", "theme", "dark")
        else:
            self.config_set("general", "theme", "light")

        self.write()

    # Sets selected db
    def db_selection(self, db_name):
        # Set selection
        self.config_set("general", "selected_db", str(db_name))

        # Write
        self.write()

    # Adds db
    def db_create(self, db_name):
        # Get location and date
        index = len(self.config.items("database_names"))
        
        # Add db to end
        self.config_set("database_names", index, db_name)
        self.config_set("database_creation_date", index, date.today().strftime("%Y-%m-%d"))

        # Save settings
        self.write()


    # Deletes a specific item
    def db_delete(self, index):
        # Remove db
        self.config.remove_option("database_names", str(index))
        self.config.remove_option("database_creation_date", str(index))

        # Set selection to none
        self.config_set("general", "selected_db", "none")
        
        # Update section
        self.write()


    # Updates list
    def db_update(self):
        # Set variables
        n = len(self.config.items("database_names"))
        delete = False

        for i in range(0, n):
            index = self.config.items("database_names")[i][0]
            db_name = self.config.items("database_names")[i][1]
            db_creation_date = self.config.items("database_creation_date")[i][1]

            # Check if correct number
            if index == str(i):
                pass
            else:
                # Set new
                self.config_set("database_names", i, db_name)
                self.config_set("database_creation_date", i, db_creation_date)

                # Remove previous
                self.config.remove_option("database_names", str(index))
                self.config.remove_option("database_creation_date", str(index))

                if delete == False:
                    delete = True

        # Check if item was removed
        if delete:
            self.config.remove_option("database_names", str(n))
            self.config.remove_option("database_creation_date", str(n))

        # Write to DB
        self.write()
