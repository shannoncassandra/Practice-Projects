#Prints Pi to a customized number of decimal places, within reason (up to 10).

import math
Pi = str(math.pi)

while True:
    try:
        pinum = int((input("How many decimal places of Pi do you want?: ")))
        
        if pinum == 0:
            print(Pi[0])

        if pinum == 1:
            print(Pi[:3])

        if pinum == 2:
            print(Pi[:4])
    
        if pinum == 3:
            print(Pi[:5])
            
        if pinum == 4:
            print(Pi[6])

        if pinum == 5:
            print(Pi[:7])

        if pinum == 6:
            print(Pi[:8])
    
        if pinum == 7:
            print(Pi[:9])
        
        if pinum == 8:
            print(Pi[:10])

        if pinum == 9:
            print(Pi[:11])
    
        if pinum == 10:
            print(Pi[:12])

        if pinum < 0:
            print('Too low')
            
        if pinum > 10:
            print('Too high')
            
        break
        
    except ValueError:
        print("It has to be a number! Try again.")
