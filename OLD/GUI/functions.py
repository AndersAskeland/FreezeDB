# A file containing all the different functions that are possible.

## IMPORT
# External 
from datetime import datetime, date
import sys, os
import csv
from sqlalchemy import create_engine, func
from sqlalchemy import future
from sqlalchemy.orm import Session
from sqlalchemy.orm import identity
from sqlalchemy.future import select


# SETTINGS
engine = create_engine("sqlite:///freeze.db", echo=True, future=True)  # Configure SQL database using engine object (echo = logging)
session = Session(bind=engine)

# Change database
def connect_engine(database):
    engine = create_engine("sqlite:///databases/" + database + ".db", echo=True, future=True)
    return(Session(bind=engine))


# Extract data into dictionary
def read_sql(db, participant_id=None):
    if participant_id is None:
        return(session.execute(select(db)).all())
    else:
        return(session.execute(select(db).filter(db.participant_id == participant_id)).all())

## Write data to CSV
def write_csv(sql_data):
    with open("export.csv", "a") as file:
        # Open file
        writer = csv.writer(file)

        # Header (column names)
        writer.writerow(["Participant_id", "Identifier", "Visit", "Blood_type", "Date"]) # Make header

        # Write data
        for data in sql_data:
            for row in data:
                writer.writerow([row.participant_id, row.identifier, row.visit, row.blood_type, row.date_time])

# Find current max
def max_identifier(db, blood_type):
    max = session.execute(select(db, func.max(db.identifier)).filter(db.blood_type == blood_type)).fetchone()
    if max.Blood is None:
        return(None)
    else:
        return(int(max.Blood.identifier) + 1)  

def nSamples(db, table):
    session = connect_engine(db)
    n = session.query(table).count()
    session.close()
    return(n)

# Get table columns
def sql_table_names(db, table):
    # Create session
    session = connect_engine(db)

    # Get names in list
    return(table.__table__.columns.keys())

# Load row sql data into dict
def loadSQL(db, table):
    # Connect, query, and close db
    session = connect_engine(db)
    dat = session.query(table).all()
    session.close()

    # Return
    return(dat)


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

