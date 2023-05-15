print("****GET TO KNOW YOU*****")
print("Hi! My name is Kola.\n")
name = input("What is your name?: ")
print("\nIt is nice to meet you {}".format(name))


while True:
    age = eval(input("\nHow old are you?: "))
    if age in range(0, 19):
        print("\nYou are a teenager")

    elif age > 18:
        print("\nWelcome to Kola's room.")
        break

print("\nTo get to the next question, please provide the answer to the question below")
print("\nWhat is the highest mountain in the world?:")
print("A. Mt. Sinai\nB. Mt. Manaslu\nC. Mt. Lhotse\nD. Mt. Everest")
optionList = ["A", "B", "C", "D"]

trial = 0
while trial < 2:
    mountainName = input("pick an answer from the above options: ")

    if mountainName not in optionList:
        print("\nInvalid answer")

    elif mountainName == "D" or mountainName == "d":
        print("\nYou are right. Next level Prayers")
        break
    else:
        print("Please try again")
        print("You have one more trial")
        trial += 1


if trial == 2:
    print("\nYou failed to move to the next stage. Better luck next time")
else:
    print("Congrats {}! you made it to the end".format(name))
    print("*******************************************\n**************************\n*****************\n***********\n******")
