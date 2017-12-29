import re
import getpass


def load_password_blacklist(file_name):
    with open(file_name, 'r', encoding='utf-8') as raw_file:
        return raw_file.read().split('\n')


def is_password_in_blacklist(blacklist, password):
    return password.lower() in blacklist


def has_numbers(password):
    return bool(re.search(r'\d', password))


def has_symbols(password):
    return bool(re.search(r'\W', password))


def is_min_length(password):
    min_length = 10
    return len(password) >= min_length


def has_uppercase(password):
    return bool(re.search(r'[A-Z]', password))


def has_lowercase(password):
    return bool(re.search(r'[a-z]', password))


def is_not_date(password):
    return bool(re.search(r'\d{2,4}[.-]\d{2}[.-]\d{2,4}', password))


def is_not_phone_number(word):
    return not bool(re.search(r'[7-8]\d{10}', word))


def is_not_empty(word):
    return bool(word)


def get_password_strength(password):
    password_strength = 0
    check_list = [
        is_not_empty,
        is_not_phone_number,
        is_not_date,
        has_lowercase,
        has_uppercase,
        is_min_length,
        has_symbols,
        has_numbers
    ]
    for demand in check_list:
        if demand(password):
            password_strength += 1
    return password_strength


if __name__ == '__main__':
    password = getpass.getpass()
    password_blacklist = load_password_blacklist('password_blacklist.txt')
    if is_password_in_blacklist(password_blacklist,password):
        print('Password is prohibited, try again')
    else:
        print('Password strength is: ', get_password_strength(password))