from datetime import datetime 

def age_verification(DOB):
    if DOB == "":
        raise Exception ("Please enter your date of birth")
    elif DOB != "":
        try: 
            datetime.strptime(DOB, "%Y-%m-%d")
            return True # we need to expand this
        except ValueError: 
            raise Exception("Please enter your date of birth in YYYY-MM-DD format")  
