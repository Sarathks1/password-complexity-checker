import re

def assess_password_strength(password):
    # Initialize criteria
    length_criteria = len(password) >= 12
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_character_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Calculate strength score
    score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_character_criteria
    ])
    
    # Determine strength
    if score == 5:
        strength = "Very Strong"
        feedback = "Excellent! Your password is very strong."
    elif score == 4:
        strength = "Strong"
        feedback = "Good job! Your password is strong."
    elif score == 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Consider adding more variety."
    elif score == 2:
        strength = "Weak"
        feedback = "Your password is weak. It needs improvement."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. Please choose a stronger one."

    # Return results
    return {
        "strength": strength,
        "feedback": feedback,
        "criteria": {
            "length": length_criteria,
            "uppercase": uppercase_criteria,
            "lowercase": lowercase_criteria,
            "number": number_criteria,
            "special_character": special_character_criteria
        }
    }

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    result = assess_password_strength(password)
    print(f"Password Strength: {result['strength']}")
    print(result['feedback'])