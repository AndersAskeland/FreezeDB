# ----------------------------------------------------------------------------- #
# Title: Helper functions                                                       #
#                                                                               #
# What: Functions used in multiple modules. Defined here to avoid circular      #
#       imports.                                                                #
# ----------------------------------------------------------------------------- #
# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
''' External packages '''
import os, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


''' Local modules '''

''' Local resources '''

# ------------------------------------------------------------- #
# 2 - SETTING, CONSTANTS, AND HELPER FUNCTIONS                  #
# ------------------------------------------------------------- #
class PrintColor:
    """ Set terminal print colors. Used for debug messages. """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ------------------------------------------------------------- #
# 3 - General functions                                         #
# ------------------------------------------------------------- #
""" """
def load_defaults(self):
    ConfigMain().ui_update_database_list(self)

""" Don't really know what this do) """
def get_base_path():
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        return sys._MEIPASS
    except Exception:
        return os.path.abspath(".")

""" Absolute path (works for dev and for PyInstaller) """
def resource_path(relative_path):
    base_path = get_base_path()

    return os.path.join(base_path, relative_path)


''' Absolute path to database file '''
def get_path(db_name, item_dir):
    base_path = get_base_path()

    return os.path.join(base_path, (item_dir + db_name + ".db"))

''' Absolute path to database file '''
def get_database_path(data_dir, database_name):
    base_path = get_base_path()
    return os.path.join(base_path, (data_dir + database_name + ".db"))

''' Retturn a active database session '''
def get_session(path):
    engine = create_engine("sqlite:///" + path, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()

''' Initiate database engine '''
def get_engine(path):
    engine = create_engine("sqlite:///" + path, echo=False)
    return engine

''' Print messages '''
def debug_print(level=0, name="", message="", complete=0, function=0): 
    # Get name
    name = "[" + name.upper() + "]"
    
    # Print
    if level == "top":
        print(PrintColor.HEADER + name + PrintColor.ENDC + " - " + message + " Function: " + PrintColor.OKCYAN + str(function) + PrintColor.ENDC)
    elif level == "sub":
        print(PrintColor.OKGREEN + "   > " + message + PrintColor.ENDC)
    elif level == "error":
        print(PrintColor.FAIL + "   Error: " + PrintColor.ENDC + message)

    # Newline if complete
    if complete == 1:
        pass
