from datetime import datetime, date

def age_verification(DOB):
    today = datetime.today()
    sixteen_years_ago = date(today.year -16, today.month, today.day)
    
    if DOB == "":
        raise Exception ("Please enter your date of birth")
    elif DOB != "":
        try: 
            DOB = datetime.strptime(DOB, "%Y-%m-%d").date()
            if DOB <= sixteen_years_ago:
                return "Access granted"
            else: 
                age = today.year - DOB.year
                return f"Access denied you are {age}, required age is 16"

        except ValueError: 
            raise Exception("Please enter your date of birth in YYYY-MM-DD format")  
