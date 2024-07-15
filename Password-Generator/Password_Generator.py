import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random choices from the characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length for the password: "))
        
        if length <= 0:
            print("Password length should be a positive integer. Please try again.")
            return

        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

# Call the main function
main()

#Copyright &copy; 2024 by @Pavani-Manni | All Rights Reserved.