import re

def assess_password_strength(password):
    score = 0
    
    # Check length
    length_score = max(0, min(4, len(password) // 4))  # Assign up to 4 points based on length
    score += length_score
    
    # Check for presence of uppercase letters
    if re.search(r'[A-Z]', password):
        score += 2
    
    # Check for presence of lowercase letters
    if re.search(r'[a-z]', password):
        score += 2
    
    # Check for presence of numbers
    if re.search(r'\d', password):
        score += 2
    
    # Check for presence of special characters
    if re.search(r'[@#$%^&*()_+{}[\]:;"\'<>,.?/|\\]', password):
        score += 2
    
    return score

def main():
    password = input("Enter a password to assess its strength: ")
    strength_score = assess_password_strength(password)
    
    print(f"Password strength score: {strength_score} out of 12")
    if strength_score >= 8:
        print("Password is strong.")
    elif strength_score >= 6:
        print("Password is moderate.")
    else:
        print("Password is weak.")
    
if __name__ == "__main__":
    main()
