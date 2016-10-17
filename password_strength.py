import re
import requests
import getpass
import os


def load_blacklist_passwords():
    with open('blacklist.txt', mode='r') as txt_file:
        black_list = txt_file.read().split('\n')
    return black_list


def load_blacklist_passwords_from_site():
    url = 'https://raw.githubusercontent.com/danielmiessler/ \
    SecLists/master/Passwords/10_million_password_list_top_1000.txt'
    black_list_get = requests.get(url)
    black_list_passwords = black_list_get.text.split('\n')
    with open('blacklist.txt', 'w') as black_list:
        black_list.write(black_list_get.text)
    return black_list_passwords


def get_password_strength(password, black_list_passwords=None):
    strength = 0
    worst_len, bad_len, good_len, best_len = (3, 6, 8, 10)
    has_digits = re.search(r'\d+', password)
    has_small_letters = re.search(r'[a-z]', password)
    has_big_letters = re.search(r'[A-Z]', password)
    has_whitespaces = re.search(r'\s', password)
    has_other_symbols = re.search(r'[^A-Za-z\s\w]', password)
    len_pass = len(password)
    if password not in black_list_passwords:
        strength += 1
    if len_pass > worst_len:
        strength += 1
    if len_pass > bad_len:
        strength += 1
    if len_pass > good_len:
        strength += 1
    if len_pass > best_len:
        strength += 1
    if has_digits:
        strength += 1
    if has_small_letters:
        strength += 1
    if has_big_letters:
        strength += 1
    if has_whitespaces:
        strength += 1
    if has_other_symbols:
        strength += 1
    return strength

if __name__ == '__main__':
    password = getpass.unix_getpass()
    if os.path.exists('blacklist.txt'):
        black_list = load_blacklist_passwords()
    else:
        black_list = load_blacklist_passwords_from_site()
    password_strength = get_password_strength(password, black_list)
    print('Hardness of your password is {0}'.format(password_strength))
