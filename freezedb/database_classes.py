# A "module" for defining different classes used in the sqlite database.
# Will be imported into application.py (__init___). I have defined s
# ample (unique id), blood, urine, operator, location

# IMPORT
# External modules
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.sqltypes import DateTime


# SETTINGS
Base = declarative_base()


# DATABASE CLASSES
# Sample
class Sample(Base):
    __tablename__ = "sample"

    id = Column(Integer, nullabe=False, unique=True, primary_key=True)

    # Relationships
    blood_sample = relationship("Blood", back_populates="sample")
    urine_sample = relationship("Urine", back_populates="sample")


# Blood samples
class Blood(Base):
    __tablename__ = "blood"

    participant_id = Column(Integer, primary_key=True, nullable=False)
    identifier = Column(Integer, primary_key=True, nullable=False, unique=True)
    visit = Column(String, nullable=False)
    blood_type = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=False)
    freeze_cycles = Column(Integer, nullable=True)
    operator_collection = Column(String, nullable=False)
    operator_centrifugation = Column(String, nullable=False)
    rack_id = Column(Integer, Nullable=False)
    location = Column(String, nullable=False)
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
    date_time = Column(DateTime, nullable=False)
    visit = Column(String, nullable=False)
    operator_centrifugation = Column(String, nullable=False)
    freez_thaw_cycles = Column(Integer, nullable=True)
    rack_id = Column(Integer, Nullable=False)
    location = Column(String, nullable=False)
    notes = Column(String, Nullable=True)

    # Foreign key
    id = Column(Integer, ForeignKey("sample.id"))

    # Back populate sample
    sample = relationship("Sample", back_populates="urine_sample")

    # Print method
    def __repr__(self):
        return(f"Sample(ID={self.participant_id!r} date={self.date_time!r})")
