import random
import string

def generate_password(length):
    # Define the character set: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choices
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

