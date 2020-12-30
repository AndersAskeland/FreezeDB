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
num = int(4891)
while True:
    if num > 1:
        for i in range(2, num):
            print(i)
            if num % i == 0:
                print("This number is not prime")
                break
        print("This number is prime")
        break
    else: 
        print("This number is not prime")
        break
# %%
def create_matrix(cells=[" "] * 9):
    matrix = []
    
    for i in range(3):
    # create empty row (a sublist inside our list)
        matrix.append([])
        for j in range(3):
            matrix[i].append(cells[j + (i * 3)])
        
    return matrix


matrix = create_matrix()

print("".join(list(map(''.join, matrix))).count(" "))

# %%

# %%
def main():
    # Start matrix
    matrix = create_matrix()

    # Show input
    print_matrix(matrix)

    # Set turn
    turn = 1

    # User loop
    while True:
        # Get input
        selection = get_input()

        # Check if outside
        if int(selection[ 0 ]) > 3 or int(selection[ 1 ]) > 3:
            continue

        # Write input
        elif matrix[ int(selection[ 0 ]) - 1 ][ int(selection[ 1 ]) - 1 ] == " ":
            # Check user
            if turn % 2 == 1:
                matrix[ int(selection[ 0 ]) - 1 ][ int(selection[ 1 ]) - 1 ] = "X"
            else:
                matrix[ int(selection[ 0 ]) - 1 ][ int(selection[ 1 ]) - 1 ] = "O"

            # Update matrix
            print_matrix(matrix)

            # Update turn
            turn += 1

            # Check winner or illegal
            check = check_win(matrix)

            if check[ 0 ]:
                print(check[ 1 ])
                break


def get_input():
    return input("Enter the coordinates:").split()


# Create matrix
def create_matrix(cells=[ " " ] * 9):
    matrix = [ ]

    for i in range(3):
        # create empty row (a sublist inside our list)
        matrix.append([ ])
        for j in range(3):
            matrix[ i ].append(cells[ j + (i * 3) ])

    return matrix


# Print matrix
def print_matrix(matrix):
    print("---------")
    print(f"| {matrix[ 0 ][ 0 ]} {matrix[ 0 ][ 1 ]} {matrix[ 0 ][ 2 ]} |")
    print(f"| {matrix[ 1 ][ 0 ]} {matrix[ 1 ][ 1 ]} {matrix[ 1 ][ 2 ]} |")
    print(f"| {matrix[ 2 ][ 0 ]} {matrix[ 2 ][ 1 ]} {matrix[ 2 ][ 2 ]} |")
    print("---------")


def check_win(matrix):
    # Win variable
    wins = 0
    x = "".join(list(map(''.join, matrix))).count("X")
    o = "".join(list(map(''.join, matrix))).count("O")

    # Check straight line
    for row in range(3):
        # Vertical win
        if matrix[ row ][ 0 ] == matrix[ row ][ 1 ] == matrix[ row ][ 2 ] and matrix[ row ][ 2 ] != " ":
            result = f"{matrix[ row ][ 0 ]} wins"
            wins += 1

        # Horisontal win
        elif matrix[ 0 ][ row ] == matrix[ 1 ][ row ] == matrix[ 2 ][ row ] and matrix[ row ][ 2 ] != " ":
            result = f"{matrix[ 0 ][ row ]} wins"
            wins += 1

    if abs(x - o) > 1 or wins > 1:
        return 1, "Impossible"

    elif wins == 1:
        return 1, result

    # Diagonal line
    elif (matrix[ 0 ][ 0 ] == matrix[ 1 ][ 1 ] == matrix[ 2 ][ 2 ] or matrix[ 2 ][ 0 ] == matrix[ 1 ][ 1 ] ==
          matrix[ 0 ][ 2 ]) and matrix[ 1 ][ 1 ] != " ":
        return 1, f"{matrix[ 1 ][ 1 ]} wins"

    elif abs(x - o) > 1 or wins > 1:
        return 1, "Impossible"

    elif x + o == 9:
        return 1, "Draw"

    else:
        return 0, "Game not finished"


main()


# %%
