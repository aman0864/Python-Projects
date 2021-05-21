# Date 13-05-2021
import string as st
from random import shuffle as sh
from pyperclip import copy as co
from time import sleep as sl
import os
os.system('cls' if os.name == 'nt' else 'clear')

# password_content = list(st.ascii_letters)
# password_content.extend(list(st.digits))
# 9
password_content = list(st.punctuation)
print(password_content[22])
print(len(password_content[23]))
print(password_content[24])

# sh(password_content)
print(password_content)
