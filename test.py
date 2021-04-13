# %%
import os, sys
from datetime import date
from sqlalchemy import Column, ForeignKey, UniqueConstraint, Table, create_engine, MetaData
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String, Date, Integer, Boolean
from PySide2.QtCore import Qt, QSize, QPoint, QPointF, QRectF, QEasingCurve, QPropertyAnimation, QSequentialAnimationGroup, Slot, Property
from PySide2.QtWidgets import QCheckBox
from PySide2.QtGui import QColor, QBrush, QPaintEvent, QPen, QPainter
from configparser import ConfigParser


# Code
config = ConfigParser()

config.read("resources/settings/template_default.ini")

section_required = config.items("optional_columns")

column_keys, columns_types, column_values, nullable_flags, primary_key_flags = [], [], [], [], []
print(section_required)

for item in section_required:
    column_keys.append((item[1].split(";")[0]))
    # column_values.append(Column + "(" + item[1].split(";")[1] + ", nullable=" + item[1].split(";")[2] + ", primary_key=" + item[1].split(";")[3] + ")")
    # print(column_values)
    columns_types.append((item[1].split(";")[1]))
    nullable_flags.append((item[1].split(";")[2]))
    primary_key_flags.append(True)
    
# Create dict
table_dict = {'__tablename__': 'myTableName'}
for item in section_required:
    table_dict[item[1].split(";")[0]] = Column(eval(item[1].split(";")[1]), primary_key=item[1].split(";")[3], nullable=item[1].split(";")[2])


# Create dict
# table_dict = {'__tablename__': 'myTableName'}
# for key in column_keys:
#     for value in column_values:
#         table_dict[key] = (value)


print(f"Key: {column_keys}")
print(f"Value: {column_values}")
print(f"Dict: {table_dict}")
print("\n\n")
print(f"Type: {columns_types}")
print(f"Nullable: {nullable_flags}")

# Database
Base = declarative_base()
engine = create_engine("sqlite:///test.db", echo=True)



# Create list
Base = declarative_base()
data = type("Samples", (Base,), table_dict)
data.__tablename__

Base.metadata.create_all(engine)



# class Database(Base):
# 	__tablename__ = "database"

# 	# Required columns
# 	participant_id = Column(Integer, nullable=False)
# 	identifier = Column(Integer, nullable=False, primary_key=True, unique=True)

# 	# Optional columns
# 	for i, item in enumerate(list_names):
# 		list_names[i] = Column((list_type[i]), nullable=(list_nullable[i]))

# Create list
# Base = declarative_base()
# attr_dict = {'__tablename__': 'myTableName',
# 	     'myFirstCol': Column(Integer, primary_key=True),
# 	     'mySecondCol': Column(Integer)}

# type("Samples", (Base,), attr_dict)

# metadata = MetaData(bind=engine)
# test = Table('customers', metadata,
#              *(Column(column_name, column_type,
#                       primary_key=primary_key_flag,
#                       nullable=nullable_flag)
#                for column_name,
#                    column_type,
#                    primary_key_flag,
#                    nullable_flag in zip(columns_names,
#                                         columns_types,
#                                         primary_key_flags,
#                                         nullable_flags)))

# test.create()

# %%
    # Instance attributes
    def __init__(self):
        self.config = self.read()

        # Items
        self.item_current_db = self.config.get("general", "selected_db")
        self.item_theme = self.config.get("general", "theme")
        self.item_dir = self.config.get("general", "dir")
        self.item_current_template = self.config.get("general", "current_template")

        # Section lists
        self.section_general = self.config.items("general")
        self.section_column_names = self.config.items("column_names")
        self.section_database_names = self.config.items("database_names")
        self.section_database_creation_date = self.config.items("database_creation_date")

# %%
Base = declarative_base()
attr_dict = {'__tablename__': 'myTableName',
	     'myFirstCol': Column(Integer, primary_key=True),
	     'mySecondCol': Column(Integer)}

data = type("Samples", (Base,), attr_dict)


# %%
