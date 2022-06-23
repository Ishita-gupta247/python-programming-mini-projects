name=input('Enter you name:')
print("welcome", name, "to this adventure!")
answer=input("you are on dirt road, it has come to an end  and you can go left or right. which way would you like to go?")
if answer.lower()=="left":
    answer=input("you come to mountain..do you want to climb or do trekking around?")
    if answer.lower()=="climb":
      print("you got biten by snake while climbing..better luck nex time")
    elif answer.lower()=="walk":
        print("whoops!!you come to dead end:(")
    else:
        print("Invalid choice!!you lose :(")
elif answer.lower()=="right":
    answer=input("You come to river side want to go 'back' or 'cross' river by bridge or 'swim' across river?")
    if answer.lower()=="back":
        print("You come back to starting point!! you lose:(")
    elif answer.lower()=="cross":
        print("you cross the bridge..you meet alien..would you talk to them or not? say(yes/no)")
    elif answer.lower()=="swim":
        print("you got biten by alligator:(")

    else:
        print("Invalid choice!!you lose :(")
else:
    print("Invalid choice!!you lose :(")               