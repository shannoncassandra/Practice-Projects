#You guess the computer's number

import random

while True:
    try:
        your_numb = int(input("Guess what number I'm thinking of? "))
        break
    except ValueError:
        print('I said a NUMBER!')

comp_numb = (random.randrange(0,10))
        
if your_numb == comp_numb:
    print('Good Job! The number was {}'.format(your_numb))
else:
    print('Wrong! The number was {}'.format(comp_numb))


