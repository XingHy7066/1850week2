def valid_password(password):
    if len(password) < 8:
        return False
    
    contains_letters = any(c.isalpha() for c in password)
    contains_numbers = any(c.isdigit() for c in password)
    
    if contains_letters and contains_numbers:
        return True
    else:
        return False

while True:
    password_input =  input("Enter your password(at least 8 characters): ")

    if valid_password(password_input):
        print("Your password is valid")
        break
    else:
        print("Your password must contain at least 8 characters, and a mix of letters and numbers.")
    
        continue
