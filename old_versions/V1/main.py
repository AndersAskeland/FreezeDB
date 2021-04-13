##################################################################################
##                                   Main file                                  ##
##################################################################################
## Program title: FreezeDB                                                      ##
##                                                                              ##
## Author: Anders Askeland                                                      ##
## Frameworks used: Qt Designer, SQLAlchemy 2.0, and PySide6                    ##
## Version: 0.0.2                                                               ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External modules
import sys
from PySide2.QtWidgets import QApplication
from configparser import ConfigParser

# Internal modules
from classes.qt_classes import MainWindow
from functions.settings_functions import config_exist

##################################################################
## 2 - SETTINGS AND CONSTANTS                                   ##
##################################################################
# Read configfile
# parser = ConfigParser()
# parser.read()


#  NOTE
# I don't need db create_all if I just run the function when I create DB's inside the create db app.

##################################################################
## 3 - RUN APP                                                  ##
##################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Check and create default settings if not allready present
    config_exist()

    # Show GUI window
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
