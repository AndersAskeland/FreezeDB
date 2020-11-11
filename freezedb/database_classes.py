# A "module" for defining different classes used in the sqllite database.
# Will be imported into application.py (__init___)

# IMPORT
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, registry

# SETTINGS
mapper_registry = registry()
Base = mapper_registry.generate_base()
Base = declarative_base()

# IDENTIFICATION OF SAMPLE
class Sample(Base):
    __tablename__ = 'sample'
    
    participant_id = Column(Integer, primary_key=True, nullable=False)
    identifier = Column(Integer, nullable=False)
    blood_type = Column(String, nullable=False)
    date = Column(String, nullable=False)
    
    # Back population
    locations = relationship("Location", back_populates="samples")
    
    def __repr__(self):
        return f"Sample(participant_id={self.participant_id!r}, identifier={self.identifier!r}, blood_type={self.blood_type!r}, date={self.date!r})"

# LOCATION OF SAMPLE IN FREEZER
class Location(Base):
    __tablename__ = 'location'
    rack_id = Column(Integer, primary_key=True)
    physical_location = Column(String, nullable=False)
    participant_id = Column(Integer, ForeignKey('sample.participant_id'))

    samples = relationship("Sample", back_populates="locations")
    
    def __repr__(self):
        return f"Location(rack_id={self.rack_id!r}, physical_location={self.physical_location!r}, participant_id={self.participant_id!r})"

