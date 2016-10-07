## 6_password_strength

### Prerequisites:

Run in console pip install -r requirements.txt to install 3rd party modules.

#### This script give mark to your password from 1 (*easy password*) to 10 (*heaviest password*)

### How to use:

Run script and enter your password.

### Description:
Script has 2 functions:

- get_black_list_passwords() - load black list of passwords from https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt

- get_password_strength(password ,black_list_passwords=None) - take password(*string*) and black list of passwords, return mark from 1 to 10

