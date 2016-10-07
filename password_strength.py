import re
import requests

def get_black_list_passwords():
    URL = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt'
    black_list_get = requests.get(URL)
    black_list_passwords = black_list_get.text.split('\n')
    return black_list_passwords


def get_password_strength(password, black_list_passwords=None):
    hardness = 0
    worst_len, bad_len, good_len, best_len = (3, 6, 8, 10)
    has_digits = re.search(r'\d+', password)
    has_small_letters = re.search(r'[a-z]', password)
    has_big_letters = re.search(r'[A-Z]', password)
    has_whitespaces = re.search(r'\s', password)
    has_other_symbols = re.search(r'[^A-Za-z\s\w]', password)
    len_pass = len(password)
    if password not in black_list_passwords:
        hardness += 1
    if len_pass > worst_len:
        hardness += 1
    if len_pass > bad_len:
        hardness += 1
    if len_pass > good_len:
        hardness += 1
    if len_pass > best_len:
        hardness += 1
    if has_digits:
        hardness += 1
    if has_small_letters:
        hardness += 1
    if has_big_letters:
        hardness += 1
    if has_whitespaces:
        hardness += 1
    if has_other_symbols:
        hardness += 1
    return hardness

if __name__ == '__main__':
    password = input('enter your password: ')
    black_list_passwords = get_black_list_passwords()
    password_strength = get_password_strength(password,black_list_passwords)
    print('Hardness of your password is {0}'.format(password_strength))
