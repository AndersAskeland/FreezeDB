# The import module. This module is responbile for inserting new data
# into the database


## IMPORT MODULES
# External
from datetime import date
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

# Internal
from freezedb.classes import Blood, Urine, Sample, ReturnValue
from freezedb.modules.etc import max_identifier


## SETTINGS
engine = create_engine("sqlite:///freeze.db", echo=True, future=True)  # Configure SQL database using engine object (echo = logging)
session = Session(bind=engine)


## MAIN
def data_input(selection):
    # Blood database
    if selection == 1:
        # Inputs required
        participant_id = int(input("Participant ID: "))
        visit = str(input("Visit: "))


        # Citrate
        # Extract max
        max = max_identifier(Blood, "Citrate")

        # Check if empty
        if max is None:
            max = 1001

        # Write
        for i in range(20):
            dat = Blood(
                participant_id=participant_id, 
                visit=visit, 
                blood_type="Citrate", 
                identifier=max + i,
                date_time=date.today()   
                )
            session.add(dat)


        # EDTA
        # Extract max
        max = max_identifier(Blood, "EDTA")

        # Check if empty
        if max is None:
            max = 2001

        # Write
        for i in range(20):
            dat = Blood(
                participant_id=participant_id, 
                visit=visit, 
                blood_type="EDTA", 
                identifier=max + i,
                date_time=date.today()
                )
            session.add(dat)

        # SERUM
        # Extract max
        max = max_identifier(Blood, "Serum")

        # Check if empty
        if max is None:
            max = 3001

        # Write
        for i in range(10):
            dat = Blood(
                participant_id=participant_id, 
                visit=visit, 
                blood_type="Serum", 
                identifier=max + i,
                date_time=date.today()
                )
            session.add(dat)

        # EV EDTA
        # Extract max
        max = max_identifier(Blood, "EV_EDTA")

        # Check if empty
        if max is None:
            max = 4001

        # Write
        for i in range(6):            
            dat = Blood(
                participant_id=participant_id, 
                visit=visit, 
                blood_type="EV_EDTA",
                identifier=max + i,
                date_time=date.today()
                )
            session.add(dat)

        # Return
        return ReturnValue(1, 1, None)

    
    # Urine database
    elif selection == 2:
        # Inputs required
        participant_id = int(input("Participant ID: "))
        visit = str(input("Visit: "))
        
        # Add to class
        dat = Urine(participant_id=participant_id, visit=visit)

        # Add to session
        session.add(dat)

        # Return
        return ReturnValue(1, 1, None)
    
    # Comit to db
    elif selection == 3:
        session.flush()
        session.commit()
        return ReturnValue(1, 0, None)
    
    else:
        pass

