#Create a Python project of a Magic 8 Ball which is a toy used for fortune-telling or seeking advice.

# import modules
import sys
import random

ans1 = True

while ans1:
    que = input("Ask the magic 8 ball a question you are seeking answer for.."+ " press(0-9) to get an answer .(dot) if you want to exit")
    print("\n")

    anss = random.randint(1, 9)

    if que == ".":
        sys.exit()

    elif anss == 1:
        print("It is certain")

    elif anss == 2:
        print("Outlook good")

    elif anss == 3:
        print("You may rely on it")

    elif anss == 4:
        print("Ask again later")

    elif anss == 5:
        print("Concentrate and ask again")

    elif anss == 6:
        print("Reply hazy, try again")

    elif anss == 7:
        print("My reply is no")

    elif anss == 8:
        print("My sources say no")
    elif anss == 9:
        print("Better not tell you now")