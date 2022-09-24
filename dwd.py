import random

num = random.randint(4,90)
newlet = 0
sorce = input("Type your encryption: " )
for letter in sorce:
    start = ord(letter)
    if(start % 2 == 0):
        newlet = num + start
    else:
        newlet += 1
    print(chr(newlet))
