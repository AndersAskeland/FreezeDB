##################################################################################
##                                                                              ##
## Title: SQL functions                                                         ##
##                                                                              ##
## What: All functions related to the sqlalchemy.                               ##
##                                                                              ##
##################################################################################

##################################################################
## 1 - IMPORT MODULES & FRAMEWORKS                              ##
##################################################################

# External modules
from datetime import date
import os.path
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Boolean, select, func
from sqlalchemy.orm import Session, declarative_base

# Internal modules
from classes.sql_classes import Database, Base

##################################################################
## 2 - SETTINGS AND CONSTANTS                                   ##
##################################################################


# Function that creates a connection to the needed database
def engine_connect(database):
    engine = create_engine("sqlite:///databases/" + database + ".db", echo=True, future=True)
    return(Session(bind=engine))


##################################################################
## 3 - FUNCTIONS                                                ##
##################################################################

# 3.1 NUMBER OF SQL DATABASE ROWS - Function that calculates the number of samples in the specified database and table.
def n_samples(database_name):
    print(database_name)
    # Connect to engine
    session = engine_connect(database=database_name)


    print(session)

    # Query db
    samples_n = session.query(Database).count()

    # Close session
    session.close()

    # Return
    return(samples_n)



# 3.2 EXTRACT SQL TABLE NAMES - Extracts the keys/values of the column names
def sql_column_keys(database):
    # Create session
    session = engine_connect(database=database)

    print(Database.__table__.columns.keys())
    # Get names in list
    return(Database.__table__.columns.keys())


# 3.3 RETURN DICTIONARY OF SQL DB - Returns a itterable dictionary to use for qtablewidgets
def sql_to_dict(database, table):
    # Connect
    session = engine_connect(database=database)

    # Query db
    dict = session.query(table).filter(Database.delete == False).all()

    # Close session
    session.close()

    # Return
    return(dict)



def create_database(db_name):
    # Connect to db
    engine = create_engine("sqlite:///databases/" + db_name + ".db", echo=True, future=True)

    # Write bases on base (classes) - See sql_classes.py
    Base.metadata.create_all(engine)


# Find current max
def max_identifier(session, sample_type):
    # Query
    max = session.execute(select(Database, func.max(Database.identifier)).filter(Database.sample_type == sample_type)).fetchone()
    print("WOHO") 
    if max.Database is None:
        return(None)
    else:
        return(int(max.Database.identifier) + 1)  

# Add data
def add_sql_data(self, session, sample_type, n, identifier):
    current_identifer = max_identifier(session, sample_type)

    if current_identifer is None:
        current_identifer = identifier
    
    # Extract 
    for i in range(n):
        dat_citrate = Database(
            participant_id = int(self.ui.lineEdit_add_participant_ID.text()),
            visit = self.ui.lineEdit_add_visit.text(),
            sample_type = sample_type,
            identifier = current_identifer + i,
            date=date.today(),
            delete=0
        )
        # Add to session
        session.add(dat_citrate)

# Delete items
def delete_sql_data(self, session, identifier):
    pass

def db_query_sample_type(self, db_name):
    # Establish connection
    session = engine_connect(db_name)

    # Create empty return list
    data = [
        session.query(Database).filter(Database.sample_type == "Citrate").count(),
        session.query(Database).filter(Database.sample_type == "EDTA").count(),
        session.query(Database).filter(Database.sample_type == "Serum").count(),
        session.query(Database).filter(Database.sample_type == "EV_EDTA").count()]

    print(data)
    # Remove all 0 values
    clean_data = [x for x in data if x > 0]
    print(clean_data)
    # Check if list is empty
    if not clean_data:
        return False
    else:
        return clean_data
