import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt

class MainMenu(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]

        self.input = QPushButton("1 - Data input")
        self.export = QPushButton("2 - Export data to CSV")

        self.logo = QLabel("Welcome to FreezeDB\n A simple database manager.")
        self.logo.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.export)

        self.setLayout(self.layout)

        # Connecting the signal
        self.input.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.logo.setText(random.choice(self.hello))


class InputMenu(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]

        self.input = QPushButton("1 - Data input")
        self.export = QPushButton("2 - Export data to CSV")

        self.logo = QLabel("Welcome to FreezeDB\n A simple database manager.")
        self.logo.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.export)

        self.setLayout(self.layout)

        # Connecting the signal
        self.input.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.logo.setText(random.choice(self.hello))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainMenu()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())