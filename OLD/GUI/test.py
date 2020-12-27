# %%
###############################
##       Test of scandir     ##
###############################

# Import
import os

# Stuff
dirs = os.scandir("./databases")

for dir in dirs:
    print(dir.name)

print (len([name for name in os.scandir('./databases') if os.path.isfile(name)]))

for i, file in enumerate(os.scandir("./databases")):
    if file.name.endswith(".db"):
        print(f"ID: {i}")
        print(f"File name: {file.name}")



# %%
###############################
##   Test of sql extraction  ##
###############################

# Import
from datetime import datetime, date
import sys, os
import csv
from sqlalchemy import create_engine, func
from sqlalchemy import future
from sqlalchemy.orm import Session
from sqlalchemy.orm import identity
from sqlalchemy.future import select
from classes import Blood

# Connect engine
engine = create_engine("sqlite:///freeze.db", echo=False, future=True)  # Configure SQL database using engine object (echo = logging)
session = Session(bind=engine)

# n = session.query(Blood).columns.keys()

# print(n)
# Find data
print(len(Blood.__table__.columns.keys()))

for i, row in enumerate(session.query(Blood).all()):
    print(f"Row {i}: {row.__dict__}")
    print(f"Participant ID: {row.__dict__['participant_id']}")



# result_dict = [u._asdict() for u in data]


""" for dat in result_dict:
    for i in dat:
        print(i) """

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
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

# %%
