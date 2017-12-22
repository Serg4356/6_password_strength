import re
import sys


def get_password_strength(password):
    password_strength = 0
    rules = [r'\d', r'\W', r'\d[.-]\d{2}[.-]\d', r'\d{11}']
    for rule in rules[:1]:
        if re.search(rule, password):
            password_strength += 2
    if not (password.isupper() | password.islower()):
        password_strength += 2
    password_blacklist = ['One', 'Two', 'Three']
    for prohibited_word in password_blacklist:
        if re.search(prohibited_word, password):
            return 'Password is incorrect. Please, do not use prohibited words'
    for rule in rules[2:]:
        if re.search(rule, password):
            return 'Password is incorrect'
    return password_strength


if __name__ == '__main__':
    print(get_password_strength(sys.argv[1]))
