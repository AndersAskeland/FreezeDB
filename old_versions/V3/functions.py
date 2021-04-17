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
from modules.helpers import get_path, get_engine, get_session, resource_path, debug_print, get_database_path
from modules.constants import CONFIG_DIR, STYLE_DARK, STYLE_LIGHT
from modules.configuration import ConfigMain, Config, ConfigTemplate
from modules.database import Database, CurrentDatabase

''' Local resources '''

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


# ------------------------------------------------------------- #
# 6 - Update functions                                          #
# ------------------------------------------------------------- #


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

