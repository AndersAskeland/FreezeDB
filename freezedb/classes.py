# A "module" for defining different classes used in the sqlite database.
# Will be imported into application.py (__init___). I have defined s
# ample (unique id), blood, urine, operator, location

# IMPORT
# External modules
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.sqltypes import DateTime


# SETTINGS
Base = declarative_base()

# REGULAR CLASSES
class ReturnValue:
    def __init__(self, arg0, arg1, arg2):
        self.arg0 = arg0
        self.arg1 = arg1
        self.arg2 = arg2


# DATABASE CLASSES
# Sample
class Sample(Base):
    __tablename__ = "sample"

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)

    # Relationships
    blood_sample = relationship("Blood", back_populates="sample")
    urine_sample = relationship("Urine", back_populates="sample")


# Blood samples
class Blood(Base):
    __tablename__ = "blood"

    participant_id = Column(Integer, primary_key=True, nullable=False)
    identifier = Column(Integer, primary_key=True, nullable=True, unique=True)
    visit = Column(String, nullable=False)
    blood_type = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=True)
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
    date_time = Column(DateTime, nullable=True)
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