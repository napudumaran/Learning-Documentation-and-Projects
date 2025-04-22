import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short. Minimum length is 8 characters.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1
        feedback.append("Decent length, consider making it 12+ characters.")

    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Add uppercase letters for better strength.")

    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Add lowercase letters for better strength.")

    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("Add numbers for better strength.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Add special characters (e.g., !@#$) for better strength.")

    common_patterns = ["password", "1234", "qwerty"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 1
        feedback.append("Avoid common patterns like 'password' or '1234'.")

    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("Password Strength Checker")
    print("Enter a password to test its strength.")
    print("Press Enter without a password to exit.")
    
    while True:
        password = input("\nEnter password: ")
        if not password:
            print("Exiting...")
            break
        
        strength, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
