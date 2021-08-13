# -----------------------------------------------------------------------------
# Module: Property classifications   
#
# What: Property classifications as done in qtDesigner.   
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules
from PySide2.QtWidgets import QFrame, QLabel, QGraphicsDropShadowEffect, QPushButton, QTabWidget
from PySide2.QtGui import QColor

# Local functions 

# Local classes 

# Local resources 

# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class QCard(QFrame):
    ''' Cards that contains information. '''
    def __init__(self,parent=None):
        super().__init__(parent)
        
        # Drop shadow effect. TODO: Make it like google material design.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setColor(QColor (0,0,0,200)) 
        self.shadow.setBlurRadius(6)
        self.shadow.setOffset(0, 3)
        self.setGraphicsEffect(self.shadow)

class QDatabaseSettings(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        # Drop shadow effect. TODO: Make it like google material design.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setColor(QColor (0,0,0,200)) 
        self.shadow.setBlurRadius(6)
        self.shadow.setOffset(0, 3)
        self.setGraphicsEffect(self.shadow)

class QSideBar(QFrame):
    ''' Sidebars on top and left. '''
    def __init__(self,parent=None):
        super().__init__(parent)

class QTextTitle(QLabel):
    ''' Text title. TODO: Don't know why i need this? '''
    def __init__(self,parent=None):
        super().__init__(parent)

class QSmallButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
        
class QMenuButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)

class QMediumButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)

class QTextOutput(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)

