import random
def life_counter(errors, lives):
    if errors < 10:
        errors += 1
    elif errors == 10:
        print("You lost one life")
        lives += 1
        errors = 0
    if lives == 3:
        print("You lost")
        exit()
    return errors, lives
counter = 0
errors = 0
lives = 0
directions=['N','S','E','W']
random.shuffle(directions)
#print(directions)# to know the password in advance
print( end= "Welcome to de magic maze, which way do you want to go? ")
while True:
    guess= input("N,S,E,W?\n")
    if guess in directions:
        #print(directions[counter])#try to get what gets from the list each turn
        if(guess==directions[counter]):
            print("Well done")
            counter+=1
            if(counter==len(directions)):
                print("You Win")
                exit()
        else:
            print("Wrong answer")
            errors,lives=life_counter(errors,lives)
    else:
        print("Not a valid answer")
        errors,lives=life_counter(errors,lives)