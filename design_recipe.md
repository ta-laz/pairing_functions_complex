# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

Extra if we want to include it: 
As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def age_verification(): 
    # Parameters: date of birth `YYYY-MM-DD` 
    # Return: str access granted or access denied based on the input
    # Side-effects: NA

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

# raise exception if input is empty 

age_verification("") => "Please enter your date of birth"

# raise exception if input is in incorrect format 

age_verification("12-12-12") => "Please enter your date of birth in YYYY-MM-DD format"

# if input is correct and user is over 16, we want to return "access granted"

age_verification("2009-01-01") => "Acccess granted"

# if input is correct and user is under 16, return "access denied, you are {age}, required age is 16"

age_verification("2025-01-01") => f"Access denied, you are {age}, required age is 16" 

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

```

Ensure all test function names are unique, otherwise pytest will ignore them!
