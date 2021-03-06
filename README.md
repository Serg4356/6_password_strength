# Password Strength Calculator

This programm checks the password by list of demands, such as:

1. the use of both upper-case and lower-case letters (case sensitivity)
2. inclusion of one or more numerical digits
3. inclusion of special characters, such as @, #, $
4. prohibition of words found in a password blacklist
5. prohibition of passwords that match the format of calendar dates and telephone numbers.

And also returns a grade of password from 0 to 10. If programm finds password in password_blacklist.txt it will display a warning message. File 'password_balcklist.txt' contains prohibited passwords. You can add words, which you consider to be prohibited, in it. Also you can find more unrecommended passwords [here](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

``` bash

'Password strength is 0' 

```

# Quickstart

Example of script launch on Windows, Python 3.5:

``` bash

$ python password_strength.py

```

After that programm asks the user to enter password. Example of programm output:

``` bash

Password:
# password input is shielded so there is no letter appeares
Password strength is: 0

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
