#The computer guesses your number

import random
import time

print("Ok, you have three seconds to pick a number! ")
time.sleep(3) 

my_list = ([0,1,2,3,4,5,6,7,8,9,10])
x = (random.choice(my_list))


while input('Is your number {}  '.format(x)) == 'no':
    my_list.remove(x)
    x = (random.choice(my_list))

else:
    print('yay')



