import re

def check_password_strength(password):
    # Strong password criteria:
    length_error = len(password) < 8
    numeric_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    
    password_ok = not (length_error or numeric_error or uppercase_error or lowercase_error or symbol_error)
    
    return {
        'Password is strong': password_ok,
        'Too short': length_error,
        'No numerics': numeric_error,
        'No uppercase letters': uppercase_error,
        'No lowercase letters': lowercase_error,
        'No symbols': symbol_error,
    }

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    result = check_password_strength(password)

    print("\nPASSWORD PRECHECK")
    for key, value in result.items():
        if key == 'Password is strong':
            print(f"{key}: {'Yes' if value else 'No'}")
        else:
            print(f"{key}: {'Yes' if value else 'No'}")
