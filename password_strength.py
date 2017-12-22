
'''
Description of functionality
V the use of both upper-case and lower-case letters (case sensitivity)
V inclusion of one or more numerical digits
V inclusion of special characters, such as @, #, $
prohibition of words found in a password blacklist
prohibition of words found in the user's personal information
prohibition of use of company name or an abbreviation
prohibition of passwords that match the format of calendar dates, license plate numbers, telephone numbers, or other common numbers
'''

import re


def get_password_strength(password):
    password_strength = 0
    #the use of both upper-case and lower-case letters (case sensitivity)
    if not (password.isupper() | password.islower()): password_strength += 1

    #inclusion of one or more numerical digits
    has_number = False
    for letter in password:
        if letter.isnumeric(): has_number = True
    if has_number: password_strength += 1

    #inclusion of special characters, such as @, #, $
    symbols = ['/', '.', ',', '"', "'", ':', ';', '>', '<', '!', '@', '#', '$', '%', '^', '&', '?', '*', '(', ')', '{',
               '}', '[', ']', '|', '-', '+']
    has_symbol = False
    for letter in password:
        if letter in symbols: has_symbol = True
    if has_symbol: password_strength += 1

    '''
    prohibition of words found in a password blacklist
    prohibition of words found in the user's personal information
    prohibition of use of company name or an abbreviation
    '''
    password_blacklist = ['One', 'Two', 'Three']
    for prohibited_word in password_blacklist:
        if re.search(prohibited_word,password) != None: return 'Password is incorrect. Please, do not use prohibited words, like your personal information, company name, etc'

    #password length testing
    if len(password) == 0: return 'Please enter the password'
    elif len(password) < 6: password_lenght = 3
    elif len(password) < 10: password_lenght = 5
    else:
        password_lenght = 7
    password_strength += password_lenght

    #testing for date, phone number format in password
    if re.search(r'\d[.-]\d{2}[.-]\d',password):return 'Do not use date format in password'
    if re.search(r'\d{11}', password): return 'Do not use phone number in password'

    return password_strength


if __name__ == '__main__':
    print(get_password_strength('Moonspell111000#'))
