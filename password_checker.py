import re

# Password Strength Checker by Napu Dumran
# Created for my Cybersecurity-Projects portfolio to demonstrate scripting and security awareness for a SOC analyst role. 

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password too short! Use at least 8 characters for better security.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Great length! 12+ characters is excellent.")
    else:
        score += 1
        feedback.append("Good length, but try for 12+ characters to boost security.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Nice! Includes uppercase letters.")
    else:
        feedback.append("Add uppercase letters to strengthen your password.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Good job including lowercase letters.")
    else:
        feedback.append("Include lowercase letters for a stronger password.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("Numbers included, solid choice!")
    else:
        feedback.append("Add numbers to improve password complexity.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Special characters detected, great for security!")
    else:
        feedback.append("Include special characters (e.g., !@#$) for extra strength.")

    # Check for common patterns
    common_patterns = ["password", "1234", "qwerty"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 1
        feedback.append("Avoid common words like 'password' or '1234'—they’re easy to guess!")

    # New: Check for repeated characters (e.g., "aaa", "111")
    if re.search(r"(.)\1{2}", password):
        score -= 1
        feedback.append("Avoid repeating the same character (e.g., 'aaa')—it weakens your password.")

    # Determine strength and visual meter
    if score >= 6:
        strength = "Strong"
        meter = "[Strong ===]"
    elif score >= 4:
        strength = "Moderate"
        meter = "[Moderate ==-]"
    else:
        strength = "Weak"
        meter = "[Weak ---]"

    return strength, meter, feedback

def main():
    print("Secure Password Checker by [Your Name]")
    print("A tool to help you create strong passwords, built for cybersecurity awareness.")
    print("Enter a password to test its strength (or press Enter to exit).\n")
    
    while True:
        password = input("Enter your password: ")
        if not password:
            print("Stay secure! Exiting...")
            break
        
        strength, meter, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {strength} {meter}")
        print("Security Tips:")
        for comment in feedback:
            print(f"- {comment}")
        print("\nTry another password or press Enter to exit.")

if __name__ == "__main__":
    main()
