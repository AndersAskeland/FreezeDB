# -----------------------------------------------------------------------------
# Module: Dialog's
#
# What: Different types of dialog's used in the program.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
# External modules
from lorem_text import lorem
from PySide2.QtWidgets import QWizardPage, QLabel, QVBoxLayout, QScrollArea, QWizard, QSizePolicy, QFileDialog, QWizard, QHBoxLayout, QPushButton, QLineEdit, QSpacerItem, QDialog
from PySide2.QtCore import QCoreApplication

# Local functions 
from modules.helpers import resource_path

# Local classes
from modules.widgets import SidebarFirstSetup
from modules.constants import STYLESHEET

# Local resources 
from resources.user_interface.dialog_create_db import Ui_create_db_page_
 
# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------
class FirstTimeSetup(QWizard):
    ''' Wizard that is shown on first program startup. '''
    # ------------------- Attributes ------------------- # 

    # ------------------ Constructor ------------------- # 
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set text/etc
        self.selected_dir = None
        self.label_selection = self.set_folder_label()

        # Build page
        self.wizard = QWizard()
        self.wizard.addPage(self.introPage())
        self.wizard.addPage(self.licencePage())
        self.wizard.addPage(self.selectDBPage())

        # Settings
        self.wizard.setWindowTitle("FreezeDB - First time setup")
        self.wizard.setWizardStyle(QWizard.ModernStyle)        
        self.wizard.setMinimumSize(730, 400)
        
        # Sidebar
        self.sidebar = SidebarFirstSetup()
        self.wizard.setSideWidget(self.sidebar)

        # Run
        self.wizard.show()
        self.wizard.exec_()

    # -------------------- Pages -------------------- # 
    def introPage(self):
        ''' Front page of first time setup dialog. '''
        page = QWizardPage()
        page.setTitle("FreezeDB - First time setup")

        label = QLabel("""Welcome to FreezeDB. FreezeDB is a simple application that can manage data related to clinical samples. \n\nAs this is the first time you open this application on the current computer, you'll need to accept the licence terms and select the default storage location.""")
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        page.setLayout(layout)

        return page

    def licencePage(self):
        ''' Page showing licence. '''
        page = QWizardPage()
        page.setTitle("Licence terms")
        page.setButtonText(QWizard.NextButton, "Accept")

        # Widgets
        nameLabel = QLabel("You must accept the above terms to continue.")
        licence = QLabel(lorem.paragraphs(10))
        licence.setWordWrap(True)
        licenceBox = QScrollArea()
        licenceBox.setWidget(licence)        

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(licenceBox)
        layout.addWidget(nameLabel)
        page.setLayout(layout)

        return page

    def selectDBPage(self, text="No folder selected!"):
        ''' Page allowing user to select folder where database files are to be stored. '''
        self.page = QWizardPage()
        self.page.setTitle("Set data folder")

        # Widgets
        self.lbl_subtitle = QLabel("Select the base data folder in where your data is to be stored.")
        self.lbl_subtitle.setWordWrap(True)
        self.lbl_location = QLabel("Location")
        
        self.line = QLineEdit()
        self.line.setReadOnly(True)

        self.pushButton = QPushButton()
        self.pushButton.clicked.connect(lambda: self.dialog_setFolder())
        self.pushButton.setText(QCoreApplication.translate("FirstTimeSetup", u"Select directory", None))

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Layouts
        self.pageLayout = QVBoxLayout()
        self.selectionLayout = QHBoxLayout()

        self.pageLayout.addWidget(self.lbl_subtitle)
        self.pageLayout.addItem(self.verticalSpacer)
        self.pageLayout.addWidget(self.lbl_location)
        self.pageLayout.addLayout(self.selectionLayout)

        self.selectionLayout.addWidget(self.line)
        self.selectionLayout.addWidget(self.pushButton)

        # Add layout
        self.page.setLayout(self.pageLayout)

        # Check
        self.page.registerField("folder*", self.line)

        # Return
        return self.page

    # -------------------- Function -------------------- # 
    def dialog_setFolder(self):
        ''' Popup dialog that allows user to select folder using native wizard. '''
        dlg = QFileDialog()
        
        # Options
        dlg.setLabelText(QFileDialog.Accept, "Select directory")
        dlg.setFileMode(QFileDialog.Directory)
        dlg.Option.ShowDirsOnly

        # Retrieve selection
        if dlg.exec_():
            self.selected_dir = dlg.selectedFiles()[0] + "/"
            self.set_folder_label()

    def data_folder(self):
        ''' Set data folder. NOTE: Might not be used. '''
        return str(self.selected_dir)

    def set_folder_label(self):
        ''' Set folder label. TODO: Figure out what this does. '''
        if self.selected_dir == None:
            return "No Folder Selected!"
        else:
            self.line.setText(str(self.selected_dir))


class CreateDBTemplate(QDialog):
    ''' Dialog/wizard to create database template. '''
    def __init__(self, parent=None):
        super().__init__(parent)

        # Setup UI
        self.dialog = Ui_create_db_page_()
        self.dialog.setupUi(self)

        # Template
        self.setStyleSheet(open(resource_path(STYLESHEET), "r").read())

        # Run
        self.exec_()