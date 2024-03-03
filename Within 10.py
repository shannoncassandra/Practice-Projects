#Return true if your number is within 10 of 100 or 200.

def withinten(n):
    return (abs(100-n)<=10) or (abs(200-n)<=10)

n=int(input("What's your number? "))
print(withinten(n))
