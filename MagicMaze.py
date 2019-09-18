import random
def life_counter(errors,lives):
    if errors<10 :
        errors +=1
    elif errors==10:
        lives+=1
        errors=0
    if lives==3:
        print("You lost")
        exit()
directions=['N','S','E','W']
random.shuffle(directions)
#print(directions)# to know the pasword in advance
print( end= "Welecome to de magic maze, which way do you want to go? ")
counter=0
errors=0
lives=0
while(True):
    guess= input("N,S,E,W\n")
    if (guess=='N' or guess=='S' or guess=='E' or guess=='W'):
        #print(directions[counter])#try to get what gets from the list each turn
        if(guess==directions[counter]):
            print("Well done")
            counter+=1
            if(counter==len(directions)):
                print("You Win")
                exit()
        else:
            print("Wrong answer")
            life_counter(errors,lives)
    else:
        print("Not a valid answer")
        life_counter(errors,lives)




