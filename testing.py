# %%
from configparser import ConfigParser

from sqlalchemy.engine.create import create_engine


parser = ConfigParser()
parser.read('config.ini')
print('test' in parser.sections())


print(parser.sections())
print(type(parser.get('settings', 'selected_db')))

with open('config.ini', 'w') as f:
    parser.set("settings", "selected_db", "none")
    parser.write(f)
try:
    dat = int(parser.get('settings', 'selected_db'))
except:
    print("exception")

# %%

# %%
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import Session, mapper

from classes.sql_classes import Database


###################
#### Create db ####
###################
# Create connection
engine = create_engine("sqlite:///databases/testingstuff2.db", echo=True, future=True)

# Metadata
metadata = MetaData()

# TODO
# Database setting wether it uses specified identifier or auto-increment.

# Create table
table = Table("database", metadata,
    Column('participant_id', Integer, nullable=False),
    Column('identifier', Integer, nullable=False, primary_key=True),
    Column('visit', String, nullable=False),
    Column('sample_type', String, nullable=False),
    Column('date', Date, nullable=False),
    Column('delete', Boolean, nullable=False),
    Column('freeze_cycles', Integer, nullable=True),
    Column('operator', String, nullable=True),
    Column('location', String, nullable=True),
    Column('notes', String, nullable=False)
    )

# Create database
# metadata.create_all(engine) 

mapper(Database, table)

# session = Session(bind=engine)

# print(session.query(Database).count())

""" 
engine = create_engine("sqlite:///databases/Test.db", echo=True, future=True)

session = Session(bind=engine)

mapper(Database, session) """


#print(session.query(Database).count())

# %%
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from classes.sql_classes import Blood

engine = create_engine("sqlite:///databases/deleted/Multisite_Blood.db", echo=True, future=True)

session = Session(bind=engine)



print(session.query(Blood).count())
# %%
