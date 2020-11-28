# A file containing all the different functions that are possible.

## IMPORT
# External 
from datetime import datetime, date
import sys, os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.orm import identity
from sqlalchemy.future import select

# Internal


# SETTINGS
engine = create_engine("sqlite:///freeze.db", echo=True, future=True)  # Configure SQL database using engine object (echo = logging)
session = Session(bind=engine)


# Find current max
def max_identifier(db, blood_type):
    max = session.execute(select(db, func.max(db.identifier)).filter(db.blood_type == blood_type)).fetchone()
    if max.Blood is None:
        return(None)
    else:
        return(int(max.Blood.identifier) + 1)  


# DELETE
def delete():
    print("Delete menu")


# VIEW
def lookup():
    print("View menu")


# SETTINGS
def settings():
    print("Settings menu")


# EXIT
def quit():
    sys.exit("Exiting program")

