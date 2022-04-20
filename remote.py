import tv
import time

tv = tv.TV()

print('Press "oo" to power on TV')

def change_state(x):
    if tv.poweron == 1:
        if x == 'oo': # Power 
            tv.power()
        elif x == 'io':
            tv.volume(x)
        elif x == 'oi':
            tv.channel(x)
        elif x == 'ii':
            tv.brightness(x)
        else:
            tv.error()
    else:
        if x == 'oo':
            tv.power()
        else:
            tv.error()

while 1: 
    user_input = input()
    change_state(user_input)