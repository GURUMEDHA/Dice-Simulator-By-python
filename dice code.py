import random
print("This Is Dice Simulator By Python")
x ="y"

while x=="y":
    Num= random.randint(1,6)
    if Num==1:
        print("-------")
        print("|     |")
        print("|  O  |")
        print("|     |")
        print("-------")

    if Num==2:
        print("-------")
        print("|     |")
        print("|O   O|")
        print("|     |")
        print("-------")

    if Num==3:
        print("-------")
        print("|  O  |")
        print("|  O  |")
        print("|  O  |")
        print("-------")

    if Num==4:
        print("-------")
        print("|O   O|")
        print("|     |")
        print("|O   O|")
        print("-------")

    if Num==5:
        print("-------")
        print("|O   O|")
        print("|  O  |")
        print("|O   O|")
        print("-------")

    if Num==6:
        print("-------y")
        print("|O   O|")
        print("|O   O|")
        print("|O   O|")
        print("-------")
    x=input("press y to Roll Again ; Press n to stop :")
    