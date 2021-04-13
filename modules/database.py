import os
from datetime import date
from sqlalchemy import Column, ForeignKey, UniqueConstraint, Table, create_engine, MetaData
from sqlalchemy.orm import relationship, sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String, Date, Integer, Boolean

from modules.helpers import resource_path, get_path, resource_path, get_session, get_engine, get_database_path
from modules.configuration import ConfigMain, ConfigTemplate


class Database2:
    ''' Class attributes  '''

    ''' Instance attributes '''

    
    ''' Functions '''
    def create_database(self, database_name, selected_template, database_path):
        # Classes
        config_template = ConfigTemplate()

        # Variables
        date_time = date.today().strftime("%Y-%m-%d")

        # Database variables
        required_fields = config_template.required_fields
        optional_fields = config_template.optional_fields
        print(required_fields)

        # Create dictionary
        dict_samples = {'__tablename__': 'samples'}
        dict_metadata = 0

        for item in required_fields:
            dict_samples[item[1].split(";")[0]] = Column(eval(item[1].split(";")[1]), primary_key=item[1].split(";")[3], nullable=item[1].split(";")[2])
        for item in optional_fields:
            dict_samples[item[1].split(";")[0]] = Column(eval(item[1].split(";")[1]), primary_key=item[1].split(";")[3], nullable=item[1].split(";")[2])

        print(dict_samples)
        
        # Create class
        Base = declarative_base()
        table = type("Samples", (Base,), dict_samples)
        
        # Create database

        engine = get_engine(database_path)
        Base.metadata.create_all(engine)

        # Create database
        # Base.metadata.create_all(engine)


        # main_table = Table('samples', metadata,
        #      *(Column(column_name, column_type,
        #               primary_key=primary_key_flag,
        #               nullable=nullable_flag)
        #        for column_name,
        #            column_type,
        #            primary_key_flag,
        #            nullable_flag in zip(column_names,
        #                                 column_types,
        #                                 primary_key_flags,
        #                                 nullable_flags)))
        
        # meta_table = Table('metadata', metadata,
        #         Column('freezedb', Boolean),
        #         Column('layout_name', String),
        #         Column('creation_date', Date))

        
        # Commit
        # main_table.create()
        # meta_table.create()

        # Write metadata
        # mapper(meta_table, Meta([1, "test", date_time]))


class CurrentDatabase(Database2):
    ''' Class attributes  '''

    ''' Instance attributes '''
    def __init__(self, database):
        # General variables
        self.name = str(database)
        self.path = get_database_path(data_dir=self.data_dir, database_name=self.name)
        self.engine = get_engine(path=self.path)
        self.session = get_session(path=self.path)
        self.samples_n = self.number_of_samples()

    ''' Functions '''
    # Calculate number of samples
    def number_of_samples(self):
        return self.session.query(Database).filter(Database.delete == False).count()
    
    # Delete database
    def delete_db(self):
        os.remove(self.path)

    # Update GUI view
    def update_view(self, interface):
        # Update selection
        interface.ui.output_dbSelection__text_lg__font_bold.setText(self.name) # Home
        interface.ui.output_databaseTable__text_xl2.setText('Table view for database: "' + self.name + '".') # Add/update

        # Update number of samples
        interface.ui.output_dbSelection__text_lg__font_bold_2.setText(str(self.samples_n))


