# ----------------------------------------------------------------------------- #
# Title: Dialogs                                                                #
#                                                                               #
# What: Different types of dialogs used in the program.                         #
#                                                                               #
# ----------------------------------------------------------------------------- #
# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
''' External modules '''
import sys
from PySide2.QtWidgets import QWizardPage, QLabel, QVBoxLayout, QApplication, QScrollArea, QWizard, QSizePolicy, QFileDialog, QWizard, QHBoxLayout, QPushButton, QLineEdit, QSpacerItem, QDialog
from PySide2.QtCore import QCoreApplication
from lorem_text import lorem

''' Local functions '''

''' Local classes '''
from modules.widgets import SidebarFirstSetup, AnimatedToggle

''' Local resources '''
from resources.user_interface.dialog_create_db import Ui_create_db_page_
 
# ------------------------------------------------------------- #
# 2 - Settings/constants                                        #
# ------------------------------------------------------------- #


# ------------------------------------------------------------- #
# 3 - Classes                                                   #
# ------------------------------------------------------------- #
# --------------------------- #
# 3.1 - First time startup    #
# --------------------------- # 
''' Dialog/wizard that is shown on first program startup. '''
class FirstTimeSetup(QWizard):
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

        # Wizard settings
        self.wizard.setWindowTitle("FreezeDB - First time setup")
        self.wizard.setWizardStyle(QWizard.ModernStyle)        
        self.wizard.setMinimumSize(730, 400)
        
        # Sidebar
        self.sidebar = SidebarFirstSetup()
        self.wizard.setSideWidget(self.sidebar)

        # Run
        self.wizard.show()
        self.wizard.exec_()


    # Welcome
    def introPage(self):
        page = QWizardPage()
        page.setTitle("FreezeDB - First time setup")

        label = QLabel("""Welcome to FreezeDB. FreezeDB is a simple application that can manage data related to clinical samples. \n\nAs this is the first time you open this application on the current computer, you'll need to accept the licence terms and select the default storage location.""")
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        page.setLayout(layout)

        return page

    
    # Licence page
    def licencePage(self):
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

    # Select DB page
    def selectDBPage(self, text="No folder selected!"):
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

    # Set folder
    def dialog_setFolder(self):
        dlg = QFileDialog()
        
        # Options
        dlg.setLabelText(QFileDialog.Accept, "Select directory")
        dlg.setFileMode(QFileDialog.Directory)
        dlg.Option.ShowDirsOnly

        # Retrieve  selection
        if dlg.exec_():
            self.selected_dir = dlg.selectedFiles()[0] + "/"
            self.set_folder_label()

    # Store folder into settings
    def data_folder(self):
        return str(self.selected_dir)

    # Set folder name
    def set_folder_label(self):
        print("Inside set text function")
        if self.selected_dir == None:
            return "No Folder Selected!"
        else:
            self.line.setText(str(self.selected_dir))


class CreateDBTemplate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set widget
        self.dialog = Ui_create_db_page_()
        
        # 
        self.dialog.setupUi(self)

        self.exec_()