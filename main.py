#Number Guessing game
import random #importing the random module
x=random.randrange(10)
# Writing the Program's Heading
head="Number Guessing Game"
subhead="Here the program will genarate random number from 1 to 10"
subhead1="Let's See, If you can guess it"
print(head.center(50))
print(subhead.center(50))
print(subhead1.center(50))
#Taking Input from buddy
name=input("What's Your Name Buddy:")
i=int(input("Guess the Number:"))
if i!=x:
        print("The Correct Number is :",x)
if i==x:
        print("Hurrah You Made it Buddy, Congrats")
        exit()
#Applying input Rules
if i>10:
    print("Read the Rules ",name," bro. The program will genarate number upto 10\nRestart the program")
    print()
    exit()
#Making the logic

while i!=x:
    print("Try again ", name ," Buddy, Take another chance")
    x=random.randrange(10)
    i=int(input("Guess the Number:"))
    if i!=x:
        print("The Correct Number is :",x)
    
    if i>10:
        print("Read the Rules",name," bro. The program will genarate number upto 10\nRestart the program")
        exit()
    if i==x:
        print("Hurrah You Made it Buddy, Congrats")
        break
        
