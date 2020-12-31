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
from PySide6.QtWidgets import QMainWindow, QWidget, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QVBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor


# Internal modules
from functions.gui_functions import change_database, update_db_list, toggle_menu, change_page, load_settings, new_database_creation, add_to_db, delete_db, update, load_settings_update, delete_db_update, delete_entry, delete_entry_table
from functions.sql_functions import sql_column_keys, db_query_sample_type
from functions.settings_functions import read_columns

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
        # update_db_list(self)

        # Load setttings (config.ini)
        load_settings_update(self)
        
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
        
        # Create new database
        self.ui.pushButton_5.clicked.connect(lambda: new_database_creation(self))

        # Add stuff to db
        self.ui.pushButton_add.clicked.connect(lambda: add_to_db(self))
    
        # Delete db
        self.ui.pushButton_7.clicked.connect(lambda: delete_db_update(self))
        read_columns()

        # Update test
        self.ui.toolButton_update.clicked.connect(lambda: update(self))

        # Delete button identifier
        self.ui.pushButton_2.clicked.connect(lambda: delete_entry(self))
        
        self.ui.toolButton_delete.clicked.connect(lambda: delete_entry_table(self))



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
        window_size = QSize(600, 340)
        self.resize(window_size)
        self.setMinimumSize(window_size)
    
