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


# ------------------------------------------------------------- #
# 3 - General functions                                         #
# ------------------------------------------------------------- #
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
    engine = create_engine("sqlite:///" + path, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


''' Initiate database engine '''
def get_engine(path):
    engine = create_engine("sqlite:///" + path, echo=True)
    return engine

''' Print messages '''
def print_message(function, message): 
    def esc(code):
        return f'\033[{code}m'
    # TODO - add type. Error, function, ect.
    print(esc('31;1;4') + '\t\t[' + function.upper() + ']\n' + esc(0) + message + '\n')