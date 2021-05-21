# Date 13-05-2021
import string as st
from random import shuffle as sh
from pyperclip import copy as co
from time import sleep as sl
import os
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    try:
        user_choice_for_password_length = int(
            input('Please enter that how much big password you need to generate\n'))
    except:
        print('Please Enter only integer values')
        sl(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    punctuation_or_not = input(
        'Please tell that you need punctuations or not.\nPress Y to add.\nPress N to remove Punctuation.\n').lower()
    password_content = list(st.ascii_letters)
    password_content.extend(list(st.digits))
    if punctuation_or_not == 'y':
        password_content.extend(list(st.punctuation))

    while len(password_content) < user_choice_for_password_length:
        password_content.extend(list(st.ascii_letters))
        password_content.extend(list(st.digits))
        if punctuation_or_not == 'y':
            password_content.extend(list(st.digits))
    sh(password_content)
    password = ''.join(password_content)
    co(password)
    print('Your password is Copied to your Clipboard\n'+password)
