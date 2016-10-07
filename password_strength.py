import re
import requests


def get_password_strength(password):
    URL = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt'
    pass_base_get = requests.get(URL)
    pass_base_list = pass_base_get.text.split('\n')
    hardness = 0
    WORST_LEN, BAD_LEN, GOOD_LEN, BEST_LEN = (3, 6, 8, 10)
    if password not in pass_base_list:
        hardness += 1
    if len(password) > WORST_LEN:
        hardness += 1
    if len(password) > BAD_LEN:
        hardness += 1
    if len(password) > GOOD_LEN:
        hardness += 1
    if len(password) > BEST_LEN:
        hardness += 1
    if re.search(r'\d+', password):  #has digits
        hardness += 1
    if re.search(r'[a-z]', password):  #has small letters
        hardness += 1
    if re.search(r'[A-Z]', password):  #has big letters
        hardness += 1
    if re.search(r'\s', password):  #has whitespaces
        hardness += 1
    if re.search(r'[^A-Za-z\s\w]', password):  #has other symbols
        hardness +=1
    return hardness

if __name__ == '__main__':
    password = input('enter your password: ')
    get_hardness = get_password_strength(password)
    print('Hardness of your password is {0}'.format(get_hardness))
