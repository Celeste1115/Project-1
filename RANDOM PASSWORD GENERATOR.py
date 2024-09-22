import random
import string

# Function to generate a random password
def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase  # Add uppercase letters
    if use_digits:
        characters += string.digits  # Add digits (0-9)
    if use_special:
        characters += string.punctuation  # Add special characters
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Input from the user
try:
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number for the length.")
