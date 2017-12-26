import re
import getpass


def load_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as raw_file:
        return raw_file.read()


def is_word_in_blacklist(blacklist, word):
    if word.lower() in blacklist:
        return True


def has_numbers(word):
    if re.search(r'\d', word):
        return True


def has_symbols(word):
    if re.search(r'\W', word):
        return True


def is_min_length(word, min_length):
    if len(word) >= min_length:
        return True


def has_uppercase(word):
    if re.search(r'[A-Z]', word):
        return True


def has_lowercase(word):
    if re.search(r'[a-z]', word):
        return True


def is_not_date(word):
    if not re.search(r'\d{2,4}[.-]\d{2}[.-]\d{2,4}(?#searches for date in the string)', word):
        return True


def is_not_phone_number(word):
    if not re.search(r'[7-8]\d{10}', word):
        return True


def is_not_empty(word):
    if word != '':
        return True


def get_password_strength(password, password_blacklist_file_name):
    password_strength = 0
    if is_not_empty(password):
        password_strength += 1
    if is_min_length(password, 10):
        password_strength += 1
    if is_not_date(password):
        password_strength += 1
    else:
        return 0
    if is_not_phone_number(password):
        password_strength += 1
    else:
        return 0
    if has_lowercase(password):
        password_strength += 1
    if has_uppercase(password):
        password_strength += 1
    if has_numbers(password):
        password_strength += 1
    if has_symbols(password):
        password_strength += 1
    if is_word_in_blacklist(load_file(password_blacklist_file_name), password):
        password_strength += 1
    else:
        return 0
    return password_strength


if __name__ == '__main__':
    password = getpass.getpass()
    print('Password strength is: ', get_password_strength(password, 'password_blacklist.txt'))
