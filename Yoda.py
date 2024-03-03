#Repeats your advice backwards. 
#the ' ' in before join includes a space. You can put anything there to separate the words

text=input("What is your advice? ")

def master_yoda(text):
    wordlist = text.split()
    reversed_wordlist = wordlist[::-1]
    return ' '.join(reversed_wordlist)

print(master_yoda(text))
