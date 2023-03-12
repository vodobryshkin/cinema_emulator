from random import choice

sym = '1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()'.split('')
num = ''

for i in range(16):
    num += choice(sym)

