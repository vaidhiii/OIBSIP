import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ''
    
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("No character types selected. Please select at least one character type.")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        use_letters = input("Include letters? (y for yess/n for no): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y for yess/n for no): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y for yess/n for no): ").strip().lower() == 'y'
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
