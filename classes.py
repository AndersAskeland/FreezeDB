# A "module" for defining different classes used in the sqlite database.
# Will be imported into application.py (__init___). I have defined s
# ample (unique id), blood, urine, operator, location

# IMPORT
# External modules
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.sqltypes import Date
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt
import random

# SETTINGS
Base = declarative_base()

# REGULAR CLASSES
class MenuSelection:
    def __init__(self, level, sub_menu, setting):
        self.level = level
        self.sub_menu = sub_menu
        self.setting = setting

# QT classes
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


# DATABASE CLASSES
# Sample
class Sample(Base):
    __tablename__ = "sample"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)

    # Relationships
    blood_sample = relationship("Blood", back_populates="sample")
    urine_sample = relationship("Urine", back_populates="sample")


# Blood samples
class Blood(Base):
    __tablename__ = "blood"

    participant_id = Column(Integer, nullable=False)
    identifier = Column(Integer, nullable=True, primary_key=True, unique=True)
    visit = Column(String, nullable=False)
    blood_type = Column(String, nullable=False)
    date_time = Column(Date, nullable=True)
    freeze_cycles = Column(Integer, nullable=True)
    operator_collection = Column(String, nullable=True)
    operator_centrifugation = Column(String, nullable=True)
    rack_id = Column(Integer, nullable=True)
    location = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    # Foreign key
    id = Column(Integer, ForeignKey("sample.id"))

    # Back populate sample
    sample = relationship("Sample", back_populates="blood_sample")

    # Print method
    def __repr__(self):
        return(f"Sample(ID={self.participant_id!r}, identifer={self.identifier!r}, blood type={self.blood_type!r}, date={self.date_time!r})")


# Urine samples
class Urine(Base):
    __tablename__ = "urine"

    participant_id = Column(Integer, primary_key=True, nullable=False)
    date_time = Column(Date, nullable=True)
    visit = Column(String, nullable=True)
    operator_centrifugation = Column(String, nullable=True)
    freez_thaw_cycles = Column(Integer, nullable=True)
    rack_id = Column(Integer, nullable=True)
    location = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    # Foreign key
    id = Column(Integer, ForeignKey("sample.id"))

    # Back populate sample
    sample = relationship("Sample", back_populates="urine_sample")

    # Print method
    def __repr__(self):
        return(f"Sample(ID={self.participant_id!r} date={self.date_time!r})")
