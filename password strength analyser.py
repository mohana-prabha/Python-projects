#password strength analyser

import re

def analyse_password(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >=12:
        score +=2
    elif len(password) >=8:
        score +=1
    else:
        suggestions.append("Increse password length (min 12 characters).")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score =+1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score +=1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # Check numbers
    if re.search("[0-9]", password):
        score +=1
    else:
        suggestions.append("Add at least one number (0-9).")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?|<>]", password):
        score +=1
    else:
        suggestions.append("Add at least one special character (!@#$ etc).")

    # Strength level
    if score <=2:
        strength = "Weak"
    elif score <=4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions

print("password strength analyser\n")

password = input("Enter a password to analyse: ")

strngth,suggestions= analyse_password(password)

print("\nPassword Strength:", strngth)

if suggestions:
    print("\nSuggestions to Improve:")
    for s in suggestions:
        print("-", s)
        
else:
    print("\nYour password is very strong, no improvements needed!")        

