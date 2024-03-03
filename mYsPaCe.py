#Return input word(s) with alternating lower and upper cases
#i%2==0 means its even, any number divided by two that has no remainder

def my_space(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

x=input("What's your name? ")
print("hI "+(my_space(x))+"! rAwR <3")
