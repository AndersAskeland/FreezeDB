##################################################################################
##                                                                              ##
## Title: SQL classes                                                           ##
##                                                                              ##
## What: A module for defining different classes used in the sqlite database.   ##
##       Will be imported into where needed. I have statically defined the      ##
##       following tables: sample (unique id), blood, and urine.                ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External modules
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.sqltypes import Date
import random

# Internal modules


##################################################################
## 2 - SETTING AND CONSTANTS                                    ##
##################################################################
Base = declarative_base()


##################################################################
## 3 - CLASSES                                                  ##
##################################################################

# Sample (unique identifer)
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

    # TODO
    # Change class to only having one table. Choise if primray key should be user defined or auto-increment
    # Bood-type == sample-type, new delete column (bool)
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
