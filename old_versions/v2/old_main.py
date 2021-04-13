##################################################################################
##                                   Main file                                  ##
##################################################################################
## Program title: FreezeDB                                                      ##
##                                                                              ##
## Author: Anders Askeland                                                      ##
## Frameworks used: Qt Designer, SQLAlchemy 2.0, and PySide2                    ##
## Version: 0.1                                                                 ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External modules
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

# Internal modules
from application import MainWindow

##################################################################
## 2 - SETTINGS AND CONSTANTS                                   ##
##################################################################
# Pyinstaller - Check if bundle or process
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    print('running in a PyInstaller bundle')
else:
    print('running in a normal Python process')

##################################################################
## 3 - RUN APP                                                  ##
##################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Check and create default settings if not allready present
    # config_exist()

    # Show GUI window
    window = MainWindow()
    window.show()

    # App execute
    sys.exit(app.exec_())
