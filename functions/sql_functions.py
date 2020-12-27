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
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

##################################################################
## 2 - SETTINGS AND CONSTANTS                                   ##
##################################################################

# Function that creates a connection to the needed database
def engine_connect(database):
    engine = create_engine("sqlite:///databases/" + database + ".db", echo=False, future=True)
    return(Session(bind=engine))


##################################################################
## 3 - FUNCTIONS                                                ##
##################################################################

# 3.1 NUMBER OF SQL DATABASE ROWS - Function that calculates the number of samples in the specified database and table.
def n_samples(database, table):
    # Connect to engine
    session = engine_connect(database=database)

    # Query db
    samples_n = session.query(table).count()

    # Close session
    session.close()

    # Return
    return(samples_n)



# 3.2 EXTRACT SQL TABLE NAMES - Extracts the keys/values of the column names
def sql_column_keys(database, table):
    # Create session
    session = engine_connect(database=database)

    # Get names in list
    return(table.__table__.columns.keys())


# 3.3 RETURN DICTIONARY OF SQL DB - Returns a itterable dictionary to use for qtablewidgets
def sql_to_dict(database, table):
    # Connect
    session = engine_connect(database=database)

    # Query db
    dict = session.query(table).all()

    # Close session
    session.close()

    # Return
    return(dict)
