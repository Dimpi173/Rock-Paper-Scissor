import random
list1 = ["✊", "🖐️", "✌️"]
while True:
    com = random.choice(list1)
    user = input("Enter r for rock, p for paper and s for scissor: ").lower()
    if user == "r":
        if com == "✌️":
            print("You Won")
        elif com == "✊":
            print("Tie")
        elif com == "🖐️":
            print("Computer Won")
    elif user == "p":
        if com == "✌️":
            print("Computer Won")
        elif com == "✊":
            print("You Won")
        elif com == "🖐️":
            print("Tie")
    elif user == "s":
        if com == "✌️":
            print("Tie")
        elif com == "✊":
            print("Computer Won")
        elif com == "🖐️":
            print("You Won")
    else:
        print("Wrong Input")
        continue

    if user == "r":
        print("You chose: ✊")
    elif user == "p":
        print("You chose: 🖐️")
    elif user == "s":
        print("You chose: ✌️")
    print("Computer chose: ", com)
    stop = input("You want to play again? type 'yes' otherwise type 'no' : ").lower()
    if stop != "yes":
        break
    else:
        continue
