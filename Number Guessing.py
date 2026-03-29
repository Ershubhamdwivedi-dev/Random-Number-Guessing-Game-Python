import random
Cnumber=random.randrange(1,101)
userInput=int(input("Enter Your Number: "))
if userInput>Cnumber:
    print("Computer Number",Cnumber)
    print("Your guess number too High: ")
elif Cnumber>userInput:
    print("Computer Number",Cnumber)
    print("Your guess number too Low: ")
else:
    print("Computer Number",Cnumber)
    print("Your guess number is equal: ")