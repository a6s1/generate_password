import random
import string

def generate_password(length=16):
    """Generate a random password with a minimum length of 16 characters."""
    if length < 16:
        raise ValueError("Password length should be at least 16 characters")
    
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length-4)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

# Example usage
password_length = 16
password = generate_password(password_length)
print(f"Generated password: {password}")
