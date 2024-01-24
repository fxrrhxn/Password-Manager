# Password Generator for GUI Password Manager
import random

# Define character sets for letters, symbols, and numbers
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
SYMBOLS = ['!', '@', '#', '%', '$', '&', '*', '+', '_']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Main function to generate a password with customizable lengths for each part
def generate_password(length_letters=10, length_symbols=2, length_numbers=3):
    # Initialize an empty string to store the generated password
    password = ""

    # Generate a sequence of random letters and append them to the password
    for _ in range(length_letters):
        letter = random.choice(LETTERS)
        password += letter

    # Generate a sequence of random symbols and append them to the password
    for _ in range(length_symbols):
        symbol = random.choice(SYMBOLS)
        password += symbol

    # Generate a sequence of random numbers and append them to the password
    for _ in range(length_numbers):
        number = random.choice(NUMBERS)
        password += number

    # Convert the password string to a list and shuffle it to enhance randomness
    password_list = list(password)
    random.shuffle(password_list)

    # Join the shuffled list to form the final password
    shuffled_password = ''.join(password_list)

    # Return the final generated and shuffled password
    return shuffled_password

# Run the script
if __name__ == '__main__':
    generate_password()