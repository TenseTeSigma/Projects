from password_checker import main as get_password
import bcrypt, json
import os
import datetime

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def save_to_json(hashed_password, filename="hashed_passwords.json"):
    if os.path.exists("hashed_passwords.json"):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}
    
    data[hashed_password] =  f"created at: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def main():
    password = get_password()
    hashed = hash_password(password)
    save_to_json(hashed)

if __name__ == "__main__":
    main()