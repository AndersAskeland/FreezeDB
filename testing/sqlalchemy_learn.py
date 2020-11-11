## This is a the testing file used for creating the FreezeDB program.
## It will contain abunch of testing stuff, and setup, that I might use
## in the final program.

# IMPORT
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, registry

# SETTINGS
engine = create_engine("sqlite:///testing.db", echo=True, future=True) # Configure SQL database using engine object (echo = logging)
metadata = MetaData() #
mapper_registry = registry()
Base = mapper_registry.generate_base()
Base = declarative_base()

# CREATE PYTHON CLASS
class User_class(Base):
    __tablename__ = 'user_class'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("addresses", back_populates="user")
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address_class(Base):
    __tablename__ = 'address_class'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_class.id'))

    user = relationship("user", back_populates="addresses")
    
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

mapper_registry.metadata.create_all(engine) # write to db
Base.metadata.create_all(engine)


# CREATE PYTHON TABLE OBJECT
user_table = Table( # This is not yet written to DB
    "user_account",  # Tablename
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)

address_table = Table(
    "address",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String, nullable=False)
)

# CREATE DB USING METADATA/CORE
metadata.create_all(engine)

print(user_table.c.name)
# TEXT MODULE 
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM user_account"))
    print(result)

with engine.connect() as conn: # Print hello world
    result=conn.execute(text("SELECT 'hello world'"))
    print(result.all())

with engine.connect() as conn: # Create and insert into table
    conn.execute(text("CREATE TABLE IF NOT EXISTS test (x int, y int)"))
    conn.execute(text("INSERT INTO test (x,y) VALUES (:x, :y)"),
    [{"x": 1, "y":1}, {"x": 2, "y": 4}])
    conn.commit()

with engine.connect() as conn: # Select and loop
    result = conn.execute(text("SELECT x, y FROM test"))
    for row in result:
        print(f"Whole result: {result}")
        print(f"x: {row.x} y: {row.y}")

# BUNDLE COMMANDS
stmt = text("SELECT * FROM test WHERE y > :y").bindparams(y=1) # bindparams is outside engine connection
with engine.connect() as conn:
    result = conn.execute(stmt)
    print("Bundle commands")
    for row in result:
        print(f"x: {row.x} y:  {row.y}")


########################################
############ JYPITER CELL ##############
########################################
# %%



# %%
