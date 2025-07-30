import re

def check_strength(password):
    length = len(password) >= 8
    lowercase = bool(re.search(r'[a-z]', password))
    uppercase = bool(re.search(r'[A-Z]', password))
    digit = bool(re.search(r'\d', password))
    special = bool(re.search(r'[@$!%*?&]', password))



    score = sum([length, lowercase, uppercase, digit, special])
    if score ==5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"
    

if __name__ == "__main__":
    pw = input("Enter a password to check: ")
    result = check_strength(pw)
    print(f"Password Strength: {result}")
    