# ----------------------------------------------------------------------------- #
# Title: Property classifications                                               #
#                                                                               #
# What: Property classifications as done in qtDesigner.                         #
#                                                                               #
# ----------------------------------------------------------------------------- #

# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
''' External modules '''
from PySide2.QtWidgets import QFrame, QLabel

# ------------------------------------------------------------- #
# 2 - Properties                                                #
# ------------------------------------------------------------- #
class QCard(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)

class QSideBar(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)

class QTextTitle(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)