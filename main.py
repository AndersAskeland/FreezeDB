# ----------------------------------------------------------------------------- #
# Module: User interface                                                        #
#                                                                               #
# What: User interface logic and definitions.                                   #
#                                                                               #
# ----------------------------------------------------------------------------- #
# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
''' External modules '''
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
from PySide2.QtCore import QSize, QPropertyAnimation, QEasingCurve, QCoreApplication
from PySide2.QtGui import QPalette, QColor

''' Local functions '''
from modules.database import database_activate, database_create, database_delete, database_dir
from modules.constants import CONFIG_DIR, STYLE_DARK, STYLE_LIGHT
from modules.helpers import load_defaults, debug_print, resource_path

''' Local classes '''
from modules.widgets import AnimatedToggle
from modules.database import Database
from modules.dialogs import CreateDBTemplate
from modules.configuration import ConfigMain

''' Local resources '''
from resources.user_interface.mainwindow import Ui_MainWindow
from resources.user_interface.dialog_create_db import Ui_create_db_page_

# ------------------------------------------------------------- #
# 2 - Settings, constants, helper functions                     #
# ------------------------------------------------------------- #
''' Loads the view from settings file ''' 
def load_ui(self):
    # Debug
    debug_print(level="top", name="Startup", message="Loading settings.", function="load_ui")

    # Check if config exists
    debug_print(level="sub", message="Checking if config exists.")
    config = ConfigMain()

    # Load theme 
    debug_print(level="sub", message="Reading and applying theme from settings file.")
    palette = QPalette()
    dark_theme_dir = resource_path(STYLE_DARK)
    light_theme_dir = resource_path(STYLE_LIGHT) 
    theme = config.selected_theme
    if theme == "dark":
        self.setStyleSheet(open(dark_theme_dir, "r").read())
        self.ui.animate_toggle.setChecked(True)

        palette.setColor(QPalette.Window, QColor(27, 29, 35))
        self.setPalette(palette)
    else:
        self.setStyleSheet(open(light_theme_dir, "r").read())

        # TODO - Palatte
    
    # Update database list
    debug_print(level="sub", message="Reading database list from config.")
    self.ui.tree_databaseViewHome.clear()
    self.ui.tree_databaseViewAdd.clear()
    config.ui_update_database_list(self)

    # Set database 


# ------------------------------------------------------------- #
# 3 - Classes                                                   #
# ------------------------------------------------------------- #
''' Main window '''
class MainWindow(QMainWindow):
    # ------------------------- #
    #        Main window        #
    # ------------------------- # 
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize user self
        self.init_ui()

        # Custom widgets
        self.custom_widgets()

        # Connections
        self.connections()

        # Settings/prefrences
        self.load_settings()


    # ------------------------- #
    # 2.2 - User self      #
    # ------------------------- # 
    def init_ui(self):
        # Load UI 
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
        # Load UI
        load_ui(self)
     
        # Read databases
        database_dir(self)


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
        self.ui.btn_deleteDatabase__btn_small.clicked.connect(lambda: database_delete(self))

        # Change database
        self.ui.tree_databaseViewHome.itemClicked.connect(lambda: database_activate(self))
        self.ui.tree_databaseViewAdd.itemClicked.connect(lambda: database_activate(self))

        # General buttons
        self.ui.btn_refreshDatabase__btn_small.clicked.connect(lambda: update_dbList(self)) # Update db list
        self.ui.animate_toggle.clicked.connect(lambda: ui_change_theme(self)) # Change theme

        # Dialogs
        self.ui.btn_pref__btn_small.clicked.connect(CreateDBTemplate)

        # Testing
        self.ui.btn_settings__btn_large.clicked.connect(lambda: db_check(self))
        # self.ui.btn_settings__btn_large.clicked.connect(lambda: ConfigTemplate().test())
        # self.ui.btn_settings__btn_large.clicked.connect(lambda: Database2().create_database("test", "test"))





# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------------------- #
# 4 - Functions                                                 #
# ------------------------------------------------------------- #
# --------------------------- #
# 3.1 - Change theme          #
# --------------------------- # 
''' Connected to custom theme change widget - changes the theme from dark to light. '''
def ui_change_theme(self): # UPDATED
    # ------------- #
    #     Debug     #
    # ------------- #
    debug_print(level="top", name="User interface", message="Changing theme and saving theme to config.", function=ui_change_theme.__name__)
    
    # ------------- #
    #    Classes    #
    # ------------- #
    palette = QPalette()
    config_main = ConfigMain()

    # ------------- #
    #   Variables   #
    # ------------- #    
    dark_theme_dir = resource_path(STYLE_DARK)
    light_theme_dir = resource_path(STYLE_LIGHT) 
    button_state = self.ui.animate_toggle.isChecked()

    # ------------- #
    #     Error     #
    # ------------- #

    # ------------- #
    #     Logic     #
    # ------------- #
    if button_state:
        # Dark theme
        theme = "dark"
        self.setStyleSheet(open(dark_theme_dir, "r").read()) # Dark
        
        palette.setColor(QPalette.Window, QColor(27, 29, 35))
        self.setPalette(palette)
    else:
        # Light theme
        self.setStyleSheet(open(light_theme_dir, "r").read()) # Dark
        theme = "light"

        # TODO - Palette

    # Save to config
    config_main.change_theme(theme)

    # ------------- #
    #      End      #
    # ------------- #
    debug_print(complete=1)


# --------------------------- #
# 3.2 - Load theme            #
# --------------------------- # 
''' Loads theme from settings file. '''
def ui_load_theme(self): # UPDATED
    # ------------- #
    #     Debug     #
    # ------------- #
    debug_print(level="top", name="User interface", message="Reading and applying theme from settings file.", function=ui_load_theme.__name__)
    
    # ------------- #
    #    Classes    #
    # ------------- #
    palette = QPalette()
    config_main = ConfigMain()
    
    # ------------- #
    #    Classes    #
    # ------------- #    
    dark_theme_dir = resource_path(STYLE_DARK)
    light_theme_dir = resource_path(STYLE_LIGHT) 
    theme = config_main.selected_theme

    # ------------- #
    #     Error     #
    # ------------- #

    # ------------- #
    #     Logic     #
    # ------------- #
    if theme == "dark":
        # Dark theme
        self.setStyleSheet(open(dark_theme_dir, "r").read()) # Dark
        self.ui.animate_toggle.setChecked(True)

        palette.setColor(QPalette.Window, QColor(27, 29, 35))
        self.setPalette(palette)

    else:
        # Light theme
        self.setStyleSheet(open(light_theme_dir, "r").read()) # Dark)

        # TODO - Palatte


# --------------------------- #
# 3.3 - Sidebar toggle        #
# --------------------------- # 
''' Animation and logic for the sidebar toggle menu. '''
def ui_menu_toggle(self): # UPDATED
    # ------------- #
    #     Debug     #
    # ------------- #
    debug_print(level="top", name="User self", message="Sidebar toggle menu activated.", function=ui_menu_toggle.__name__)

    # ------------- #
    #    Classes    #
    # ------------- #

    # ------------- #
    #   Variables   #
    # ------------- #
    current_width = self.ui.sidebar_left.width()

    # ------------- #
    #     Error     #
    # ------------- #

    # ------------- #
    #     Logic     #
    # ------------- #
    # Define animation
    self.animation = QPropertyAnimation(self.ui.sidebar_left, b"minimumWidth")
    self.animation.setDuration(300)
    self.animation.setStartValue(current_width)
    self.animation.setEasingCurve(QEasingCurve.InOutQuart)

    # Set needed width
    if current_width != 200:
        self.animation.setEndValue(200)
    else:
        self.animation.setEndValue(65)

    # Run
    self.animation.start()


# --------------------------- #
# 3.4 - Change page           #
# --------------------------- # 
''' Changes the page when button is pressed. Also manages css states for the buttons. '''
def ui_change_page(self, previous_page=None, page=None): # TODO - create custom button class for page buttons
    # ------------- #
    #     Debug     #
    # ------------- #
    debug_print(level="top", name="User interface", message=f"Changing page to '{page}'", function=ui_change_page.__name__)

    # ------------- #
    #    Classes    #
    # ------------- #

    # ------------- #
    #   Variables   #
    # ------------- #

    # ------------- #
    #     Error     #
    # ------------- #
    
    # ------------- #
    #     Logic     #
    # ------------- #
    # Change page
    if page == "home" and previous_page != 0:
        self.ui.pageWidget.setCurrentIndex(0)
        self.ui.txt_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Home</span></p></body></html>", None))
        self.ui.btn_home__btn_large.setStyleSheet("background-color: rgb(85, 170, 255)")
    elif page == "add" and previous_page != 1:
        self.ui.pageWidget.setCurrentIndex(1)
        self.ui.txt_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Add or remove data</span></p></body></html>", None))
        self.ui.btn_add__btn_large.setStyleSheet("background-color: rgb(85, 170, 255)")
    elif page == "view" and previous_page != 2:
        self.ui.pageWidget.setCurrentIndex(2)
        self.ui.txt_header.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">View data</span></p></body></html>", None))
        self.ui.btn_data__btn_large.setStyleSheet("background-color: rgb(85, 170, 255)")
    else:
        return 0

    # Resets previous button
    if previous_page == 0:
        self.ui.btn_home__btn_large.setStyleSheet("background-color: rgb(27, 29, 35)")
    elif previous_page == 1:
        self.ui.btn_add__btn_large.setStyleSheet("background-color: rgb(27, 29, 35)")
    elif previous_page == 2:
        self.ui.btn_data__btn_large.setStyleSheet("background-color: rgb(27, 29, 35)")

# --------------------------- #
# 3.5 - Set selected database #
# --------------------------- # 
''' Updates the view to represent the currently selected db - Reads config file. '''
def ui_selected_database(self):
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


# ------------------------------------------------------------- #
# 5 - Application start                                         #
# ------------------------------------------------------------- #
if __name__ == "__main__":
    # Create application
    app = QApplication(sys.argv)

    # Show GUI window
    window = MainWindow()
    window.show()
    
    # App execute/loop
    sys.exit(app.exec_())