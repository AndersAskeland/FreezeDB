# ----------------------------------------------------------------------------- #
# Title: Main application                                                       #
#                                                                               #
# What: Main application for logic.                                             #
#                                                                               #
# ----------------------------------------------------------------------------- #

# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
# External modules
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QVBoxLayout, QDialog, QFileDialog
from PySide2.QtCore import QSize
from PySide2.QtGui import QColor, QPalette

# Internal modules
from modules.functions import ui_load_theme, ui_change_page, ui_change_theme, ui_menu_toggle
from modules.functions import config_check
from modules.functions import db_check, update_selected_db, database_create, db_active, update_dbList, db_delete
# from modules.configuration import ConfigTemplate
from modules.database import Database2

# import resources.user_interface.icons_rc
from modules.widgets import AnimatedToggle

# UI manual - ENABLED
from resources.user_interface.mainwindow import Ui_MainWindow
from resources.user_interface.dialog_create_db import Ui_create_db_page_

# Dialogs
from modules.dialogs import CreateDBTemplate

# UI loader - DISABLED
''' 
from PySide2.QtUiTools import QUiLoader, QtXml
import resources.user_interface.icons_rc
'''


# ------------------------------------------------------------- #
# 2 - Main application                                          #
# ------------------------------------------------------------- #
class MainWindow(QMainWindow):
    # ------------------------- #
    # 2.1 - Main window         #
    # ------------------------- # 
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize user interface
        self.init_ui()

        # Custom widgets
        self.custom_widgets()

        # Settings/prefrences
        self.load_settings()

        # Connections
        self.connections()


    # ------------------------- #
    # 2.2 - User interface      #
    # ------------------------- # 
    def init_ui(self):
        # Load UI (QUiLoader)
        ''' Disabled '''
        # self.ui = QUiLoader().load('resources/user_interface/ui_mainwindow.ui', self)

        # Load UI (ui_mainwindow.py file)
        ''' Enabled '''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window title
        self.setWindowTitle("FreezeDB")

        # Set default button pressed
        self.ui.btn_home__btn_large.setStyleSheet("background-color: rgb(85, 170, 255)")

        # Set window size
        window_size = QSize(1350, 800)
        self.resize(window_size)
        self.setMinimumSize(window_size)
    

    # ------------------------- #
    # 2.3 - Custom widgets      #
    # ------------------------- # 
    def custom_widgets(self):
        pass
        # Sidebar
        ''' TODO - Every sidebar button can be custom '''
    
    # ------------------------- #
    # 2.4 - Load settings       #
    # ------------------------- # 
    def load_settings(self):      
        # Crate default settings
        config_check()

        # Set theme
        ui_load_theme(self)

        # Check db are present
        db_check(self)

        # Update DB list
        update_dbList(self)

        # Update currently selected db
        update_selected_db(self)


    # ------------------------- #
    # 2.5 - Connections/signals #
    # ------------------------- # 
    def connections(self):
        # Menu toggle
        self.ui.btn_toggleMenu__btn_large.clicked.connect(lambda: ui_menu_toggle(self))
        
        # Pages
        self.ui.btn_home__btn_large.clicked.connect(lambda: ui_change_page(self, previous_page=self.ui.pageWidget.currentIndex(), page="home")) # Home
        self.ui.btn_add__btn_large.clicked.connect(lambda: ui_change_page(self, previous_page=self.ui.pageWidget.currentIndex(), page="add")) # Add
        self.ui.btn_data__btn_large.clicked.connect(lambda: ui_change_page(self, previous_page=self.ui.pageWidget.currentIndex(), page="view")) # View

        # Create db
        self.ui.btn_createDB__btn_med.clicked.connect(lambda:database_create(self))

        # Delete database
        self.ui.btn_deleteDatabase__btn_small.clicked.connect(lambda: db_delete(self))

        # Change database
        self.ui.tree_databaseViewHome.itemClicked.connect(lambda: db_active(self))
        self.ui.tree_databaseViewAdd.itemClicked.connect(lambda: db_active(self))

        # General buttons
        self.ui.btn_refreshDatabase__btn_small.clicked.connect(lambda: update_dbList(self)) # Update db list
        self.ui.animate_toggle.clicked.connect(lambda: ui_change_theme(self)) # Change theme

        # Dialogs
        self.ui.btn_pref__btn_small.clicked.connect(CreateDBTemplate)

        # Testing
        self.ui.btn_settings__btn_large.clicked.connect(lambda: db_check(self))
        # self.ui.btn_settings__btn_large.clicked.connect(lambda: ConfigTemplate().test())
        # self.ui.btn_settings__btn_large.clicked.connect(lambda: Database2().create_database("test", "test"))

# class InterfaceView(MainWindow):
#     pass

# ------------------------------------------------------------- #
# 3 - Application start                                         #
# ------------------------------------------------------------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)

    
    # Show ui (QUiLoader option)
    ''' DISABLED '''
    # window = MainWindow()
    # window.ui.show()

    # Show GUI window
    window = MainWindow()
    window.show()

    # App execute
    sys.exit(app.exec_())