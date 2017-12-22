import re
import sys


def get_password_strength(password):
    password_strength = 0
    if not (password.isupper() | password.islower()):
        password_strength += 2
    if re.search(r'\d', password):
        password_strength += 2
    if re.search(r'\W', password):
        password_strength += 2
    password_blacklist = ['One', 'Two', 'Three']
    for prohibited_word in password_blacklist:
        if re.search(prohibited_word, password):
            return 'Password is incorrect. Please, do not use prohibited words'
    if re.search(r'\d[.-]\d{2}[.-]\d', password):
        return 'Do not use date format in password'
    if re.search(r'\d{11}', password):
        return 'Do not use phone number in password'
    return password_strength


if __name__ == '__main__':
    print(get_password_strength(sys.argv[1]))
