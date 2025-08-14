from datetime import datetime, date

def age_verification(DOB):
    today = datetime.today()
    sixteen_years_ago = date(today.year -16, today.month, today.day)

    
    if DOB == "":
        raise Exception ("Please enter your date of birth")
    elif DOB != "":    
        
        try:
            DOB = datetime.strptime(DOB, "%Y-%m-%d").date()
            age = today.year - DOB.year
            if DOB <= sixteen_years_ago:
                return "Access granted"
            else: 
                if age < 0:
                    raise Exception("Invalid date of birth, date of birth cannot be in the future")
                return f"Access denied you are {age}, required age is 16"

        except ValueError: 
            raise Exception("Please enter your date of birth in YYYY-MM-DD format")  
