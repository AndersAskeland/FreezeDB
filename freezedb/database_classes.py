# A "module" for defining different classes used in the sqllite database.
# Will be imported into application.py (__init___). I have defined s
# ample (unique id), blood, urine, operator, location

# IMPORT
# External modules
from enum import unique
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.sqltypes import DateTime

# SETTINGS
Base = declarative_base()

# Add participant_ID ect to sample instead of blood.


# DATABASE CLASSES
# Sample
class sample(Base):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True, nullabe=False, unique=True)

    # Foreign key
    participant_id = Column(Integer, ForeignKey('blood.participant_id'))

    # Back population
    sample = relationship("")


# Blood samples
class blood(Base):
    __tablename__ = 'blood'

    participant_id = Column(Integer, primary_key=True, nullable=False)
    identifier = Column(Integer, primary_key=True, nullable=False, unique=True)
    visit = Column(String, nullable=False)
    blood_type = Column(String, nullable=False)
    dateTime = Column(DateTime, nullable=False)
    freeze_cycles = Column(Integer, nullable=True)
    operator_collection = Column(String, nullable=False)
    operator_centrifugation = Column(String, nullable=False)
    notes = Column(String, nullable=True)

    # Foreign key
    id = Column(Integer, ForeignKey('sample.id'))

    # Back population
    locations = relationship("Location", back_populates="samples")
    
    def __repr__(self):
        return f"Sample(participant_id={self.participant_id!r}, identifier={self.identifier!r}, blood_type={self.blood_type!r}, date={self.date!r})"

### Urine samples
class urine(Base):
    __tablename__ = 'urine'

    participant_id = Column(Integer, primary_key=True, nullable=False)
    dateTime = Column(DateTime, nullable=False)
    operator_centrifugation = Column(String, nullable=False)
    freez_thaw_cycles = Column(Integer, nullable=True)
    notes = Column(String, Nullable=True)

    # Foreign key
    id = Column(Integer, ForeignKey('sample.id'))


# LOCATION OF SAMPLE IN FREEZER
class Location(Base):
    __tablename__ = 'location'

    rack_id = Column(Integer, primary_key=True)
    physical_location = Column(String, nullable=False)
    participant_id = Column(Integer, ForeignKey('sample.participant_id'))

    samples = relationship("Sample", back_populates="locations")

    def __repr__(self):
        return f"Location(rack_id={self.rack_id!r}, physical_location={self.physical_location!r},participant_id={self.participant_id!r})"
