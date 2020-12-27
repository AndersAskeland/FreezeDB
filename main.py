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
from PySide6.QtWidgets import QApplication

# Internal modules
from classes.qt_classes import MainWindow


# Start app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()


    sys.exit(app.exec_())       
