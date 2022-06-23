print("Welcome to my computer quiz!!")
playing=input("Do you want to play? ")
if playing.lower()!="yes":
    print("Hope to meet you next time :)") 
    quit()
print("Okay let's play :)")   
n=0 
answer=input("what does CPU stand for?")
if answer.lower()=="central processing unit":
    n+=1
    print("Yay! you got it right :)")
  
else:
    print("whoops!its wrong..")
answer=input("what does RAM stand for?")
if answer.lower()=="random access memory":
    n+=1
    print("Yay! you got it right :)")
    
else:
    print("whoops!its wrong..")
answer=input("what does GPU stand for?")
if answer.lower()=="graphic processing unit":
    n+=1
    print("Yay! you got it right :)")
    
else:
    print("whoops!its wrong..")
answer=input("what does ROM stand for?")
if answer.lower()=="read only memory":
    n+=1
    print("Yay! you got it right :)")
   
else:
    print("whoops!its wrong..")
answer=input("what does CD stand for?")
if answer.lower()=="compact disk":
    n+=1
    print("Yay! you got it right :)")
  
else:
    print("whoops!its wrong..")

print("you got "+str(n)+" questions correct\n")    
print("your score: "+str((n/5)*100)+" % ")