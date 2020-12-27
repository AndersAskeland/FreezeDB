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

# NUMBER OF SQL DATABASE ROWS - Function that calculates the number of samples in the specified database and table.
def n_samples(database, table):
    # Connect to engine
    session = engine_connect(database)

    # Query db
    samples_n = session.query(table).count()

    # Close session
    session.close()

    # Return
    return(samples_n)




