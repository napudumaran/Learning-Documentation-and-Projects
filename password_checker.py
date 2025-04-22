import re

# Password Strength Checker by Napu Dumaran
# Created for my Cybersecurity-Projects portfolio to demonstrate scripting and security awareness for a SOC analyst role.\
# # This password checker follows NIST 800-63B passphrase guidelines and supports NIST 800-53 compliance

def check_password_strength(password):
    score = 0
    feedback = []

    # New: Input validation for empty passwords or spaces
    if not password.strip() or re.search(r"\s", password):
        feedback.append("Invalid input! Use a strong passphrase without spaces or empty inputs.")
        return "Invalid", "[Invalid ---]", feedback
    # End of input validation

    # Check length
    if len(password) < 8:
        feedback.append("Password too short! Try to think of a passphrase instead!")
    elif len(password) >= 12:
        score += 2
        feedback.append("Great length! 12+ characters is satisfactory.")
    else:
        score += 1
        feedback.append("Good length, but try for 12+ characters meet security standards. Try using a passphrase.")

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
        feedback.append("Numbers included, satisfactory!")
    else:
        feedback.append("Add numbers to improve password complexity.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Special characters detected, satisfactory for password security!")
    else:
        feedback.append("Include special characters. (e.g., !@#$)")

    # Check for common patterns
    common_patterns = ["password", "1234", "qwerty"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 1
        feedback.append("Avoid common words like 'password' or '1234,' try a passphrase instead!")

    # New: Check for repeated characters (e.g., "aaa", "111")
    match = re.search(r"(.)\1{2}", password)
    if match:
   	 score -= 2
   	 repeated_char = match.group(1)
   	 feedback.append(f"Avoid repeating '{repeated_char}' multiple times, it makes for a weak password.")

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
    print("Secure Password Checker by Napu Dumaran")
    print("A tool to help you create strong passwords, built for cybersecurity awareness.")
    print("Try to use a passphrase or a password manager per 2025 NIST password guidelines")
    print("Enter a password to test its strength (or press Enter to exit).\n")
    
    while True:
        password = input("Enter your password: ")
        if not password:
            print("Exiting...")
            break
        
        strength, meter, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {strength} {meter}")
        print("Security Tips:")
        for comment in feedback:
            print(f"- {comment}")
        print("\nTry another password or press Enter to exit.")

if __name__ == "__main__":
    main()
