# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
import sys
from PySide2.QtWidgets import QApplication
from modules.user_interface import MainWindow
from modules.dialogs import FirstTimeSetup, CreateDBTemplate

# ------------------------------------------------------------- #
# 2 - Application start                                         #
# ------------------------------------------------------------- #
if __name__ == "__main__":
    # Create application
    app = QApplication(sys.argv)

    # Show GUI window
    window = MainWindow()
    window.show()
    
    # App execute/loop
    sys.exit(app.exec_())