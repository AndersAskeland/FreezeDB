##################################################################################
##                                                                              ##
## Title: QT classes                                                            ##
##                                                                              ##
## What: All classes related to the GUI and PySide6.                            ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External modules
from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QWidget, QDialog
from PySide6.QtCore import QSize

# Internal modules
from functions.gui_functions import change_database, update_db_list, toggle_menu, change_page, load_sql_data, load_settings
from functions.sql_functions import n_samples
from classes.sql_classes import Blood

# UI files
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_createdatabase import Ui_CreateDatabase

##################################################################
## 2 - SETTING AND CONSTANTS                                    ##
##################################################################


##################################################################
## 3 - CLASSES                                                  ##
##################################################################

# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load generated python class fomr UI file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #########################
        ## 2.1 - Settings      ## 
        #########################

        # Set window title
        self.setWindowTitle("FreezeDB")

        # Set window size
        window_size = QSize(1100, 720)
        self.resize(window_size)
        self.setMinimumSize(window_size)

        # Set startpage
        change_page(self, page="home")

        ##########################
        ## 2.2 - Load settings  ##
        ##########################
        
        # Update database list (populate treewidget on home page)
        update_db_list(self)

        # Load setttings (config.ini)
        load_settings(self)

        ##########################
        ## 2.3 - Connections    ##
        ##########################

        # Menu toggle
        self.ui.btn_toggle_menu.clicked.connect(lambda: toggle_menu(self))

        # Pages
        self.ui.btn_home.clicked.connect(lambda: change_page(self, previous_page=self.ui.stackedWidget.currentIndex(), page="home")) # Home
        self.ui.btn_add.clicked.connect(lambda: change_page(self, previous_page=self.ui.stackedWidget.currentIndex(), page="add")) # Add
        self.ui.btn_view.clicked.connect(lambda: change_page(self, previous_page=self.ui.stackedWidget.currentIndex(), page="view")) # View

        # Change database
        self.ui.tree_select_database.itemClicked.connect(lambda: change_database(self, button=1))
        self.ui.tree_select_database_2.itemClicked.connect(lambda: change_database(self, button=2))

        # Popups
        self.ui.pushButton_6.clicked.connect(self.popup)
    
    
    def popup(self):
        self.popup_window = CreateDatabase()

        self.popup_window.show()




##################################################################
## 3 - DEFINE POPUP WINDOW                                      ##
##################################################################

class CreateDatabase(QWidget):
    def __init__(self):
        super(CreateDatabase, self).__init__()

        # Load generated python class fomr UI file
        self.ui = Ui_CreateDatabase()
        self.ui.setupUi(self)

        #########################
        ## 2.1 - Settings      ## 
        #########################

        # Set window title
        self.setWindowTitle("Create new database")

        # Set window size
        window_size = QSize(500, 300)
        self.resize(window_size)
        self.setMinimumSize(window_size)
    
