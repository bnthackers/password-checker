import re
import requests
import hashlib
import getpass

def check_password_strength(password):
    """Checks the strength of a password based on common criteria."""
    strength_score = 0
    feedback = []

    # 1. Length Check (score increases with length)
    if len(password) >= 8:
        strength_score += 1
    if len(password) >= 12:
        strength_score += 1
    else:
        feedback.append("• Should be at least 8 characters long.")

    # 2. Character Type Checks using Regular Expressions
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("• Should contain lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("• Should contain uppercase letters.")

    if re.search(r"\d", password): # \d is for digits
        strength_score += 1
    else:
        feedback.append("• Should contain numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("• Should contain special characters (e.g., !@#$%).")

    return strength_score, feedback

def check_pwned(password):
    """Checks if a password has been exposed in a data breach using HIBP API."""
    # 1. Hash the password with SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # 2. Split the hash
    hash_prefix, hash_suffix = sha1_password[:5], sha1_password[5:]
    
    # 3. Call the API
    api_url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    try:
        response = requests.get(api_url)
        response.raise_for_status() # Raise an exception for bad status codes
    except requests.RequestException as e:
        print(f"Error calling API: {e}")
        return None, 0 # Return None to indicate an error

    # 4. Check for our suffix in the response
    leaks = response.text.splitlines()
    for line in leaks:
        leaked_suffix, count = line.split(':')
        if leaked_suffix == hash_suffix:
            return True, int(count) # Found it!

    return False, 0 # Password is not found in leaks

def main():
    """Main function to run the password checker."""
    try:
        password = getpass.getpass("Enter the password to check: ")
        if not password:
            print("Password cannot be empty.")
            return

        # --- Strength Check ---
        print("\n--- Analyzing Password Strength ---")
        score, feedback = check_password_strength(password)
        print(f"Strength Score: {score}/6")
        if feedback:
            for item in feedback:
                print(item)
        else:
            print(" Excellent! Your password meets all complexity requirements.")
        
        # --- Leak Check ---
        print("\n--- Checking for Leaks (using HIBP) ---")
        is_leaked, leak_count = check_pwned(password)

        if is_leaked is None:
            print("Could not check for leaks due to an API error.")
        elif is_leaked:
            print(f" WARNING: This password has been found in {leak_count} data breaches.")
            print("You should NOT use this password.")
        else:
            print(" Good news! This password was not found in any known data breaches.")

    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    main()