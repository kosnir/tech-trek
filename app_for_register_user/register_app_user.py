# Re-run this cell and examine the docstring of each function
from python_functions import validate_name, validate_email, validate_password, top_level_domains

print("validate_name\n")
print(validate_name.__doc__)
print("--------------------\n")

print("validate_email\n")
print(validate_email.__doc__) 
print("--------------------\n")

print("validate_password\n")
print(validate_password.__doc__)

# The top level domains variable is used in validate_email to approve only certain email domains
print(top_level_domains)

def validate_user(name, email, password):
    """
    This function registers a user with the app. It takes in three arguments:
    name: str - the name of the user
    email: str - the email of the user
    password: str - the password of the user
    
    The function will validate the name, email and password of the user. If the validation is successful, the function will return a dictionary with the user's details. If the validation fails, the function will return a string with the error message.
    """
    
  # Validate the name
    if not validate_name(name):
        raise ValueError("Invalid name")
    
    # Validate the email
    if not validate_email(email):
        raise ValueError("Invalid email")
    
    # Validate the password
    if not validate_password(password):
        raise ValueError("Invalid password")
    
    return True

def register_user(name, email, password):
    """
    This function registers a user with the app. It takes no arguments.
    
    The function will prompt the user to enter their name, email and password. It will then call the validate_user function to validate the user's details. If the validation is successful, the function will return a dictionary with the user's details. If the validation fails, the function will return a string with the error message.
    """
    
    # Prompt the user to enter their name, email and password
   
    if validate_user(name, email, password) == True:
        user = {
            "name": name,
            "email": email,
            "password": password
        }
        return user
    else:
        return False
