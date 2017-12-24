import re
import sys
import getpass

def get_password_balcklist(file_name):
    with open(file_name, 'r', encoding='utf-8') as raw_file:
        return(raw_file.read())

def is_password_in_blacklist(password_blacklist,password):
    for prohibited_word in password_blacklist:
        if re.search(prohibited_word, password):
            return True
        else:
            return False

def get_password_strength(password, password_blacklist):
    password_strength = 0
    patterns = [r'\d', r'\W', r'(?!.*\d{2,4}[.-]\d{2}[.-]\d{2,4})', r'\d{11}']
    for pattern in patterns:
        if re.search(pattern, password):
            password_strength += 2
    if not (password.isupper() | password.islower()):
        password_strength += 2
    if not is_password_in_blacklist(password_blacklist,password): password_strength += 2

    return password_strength


if __name__ == '__main__':
    password_blacklist = get_password_balcklist('password_blacklist.txt')
    password = getpass.getpass()
    print('Password strength is: ', get_password_strength(password,password_blacklist))
