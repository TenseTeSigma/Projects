import re

def show_info():
    print(r'''
            ____                                     _    
        |  _ \ __ _ ___ _____      _____  _ __ __| |   
        | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |   
        |  __/ (_| \__ \__  \ V  V / (_) | | | (_| |   
        |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|   
        / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
        | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
        | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
        \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  
                    
        Information:
        
        Your password will be stored in a bcrypt hash format.
        
        Requirements:
        - Must be between 5 and 20 characters
        - Must contain at least one uppercase letter
        - Must contain at least one number
        - Must contain at least one symbol [!, £, $, %, &, *, -, _]
    ''')

def basic_check(password):
    with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
        wordlist = set(line.strip() for line in f)

    if password in wordlist:
        return None
    else:
        print("Password not found in blacklisted list...")
        return password

def error_check(password):
    if len(password) < 5:
        print("Your password is too short")
        return None 
    if len(password) > 20:
        print("Your password is too long")
        return None
    return password

def pattern_check(password):
    if re.match(r'^\d+$', password):
        print("Your password is only numbers")
        return None
    
    if re.match(r'^(.)\1+$', password):
        print("Password is just repeated chars")
        return None
    
    common_sequences = ['qwerty', 'asdf', '12345', 'qazwsx', 'password', 'password123']
    if password.lower() in common_sequences:
        print("Password is in common words list")
        return None
    return password 

def complex_check(password):
    upper_count = 0
    lower_count = 0
    symbol_count = 0
    number_count = 0

    for s in password:
        if s.isupper():
            upper_count += 1

        if s.islower():
            lower_count += 1

        if s.isdigit():
            number_count += 1

        elif not s.isalnum():
            symbol_count += 1

    if upper_count <= 0:
        print("Your password contains no uppercases")
        return None
    
    if upper_count == len(password):
        print("Your password is all uppercase")
        return None
    
    if lower_count == len(password):
        print("Your password is only lowercases")
        return None
    
    if symbol_count <= 0:
        print("Your password contains zero symbols")
        return None
    
    if number_count <= 0:
        print("Your password has zero numbers")
        return None
    else:
        return password

def main():
    running = True
    while running:
        show_info()
        username = str(input("Enter your username: "))
        pwd = str(input("Enter your password: "))
        print("Checking your input...")

        if error_check(pwd) == None:
            print("Failed error check")
        
        elif basic_check(pwd) == None:
            print("Failed basic check")
        
        elif pattern_check(pwd) == None:
            print("Failed pattern check")

        elif complex_check(pwd) == None:
            print("Password is not complex enough")

        else:
            print("Password is secure, entry made in .json file")
            running = False
            return pwd

if __name__ == "__main__":
    main()