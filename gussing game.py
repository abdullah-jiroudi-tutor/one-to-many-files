import random
def start_playing():
    counter=1
    global score
    print("Welcome\nWe have a random number try to guess it with 3 times only")
    n=random.randrange(1,10)
    guess=int(input("Enter you guess:"))
    while guess != n:
        if counter == 3:
            print("limt HIT :( ")
            break
        if guess > n:
            print("Too high")
            guess = int(input("Enter you guess:"))
            counter+=1
        elif guess < n :
            print("Too low")
            guess = int(input("Enter you guess:"))
            counter+=1

    if guess == n:
        print("Great you guessed it correctly !")
        score+=1


score=0
print("Welcome to guessing Game")
print("Menu.")
print("1-start playing\n2-check score\n3-exit")
select=int(input("Enter you choice:"))
while select != 3:
    if select==1:
        start_playing()
    if select==2:
        print("your score is:",score)
    print("Menu")
    print("1-start playing\n2-check score\n3-exit")
    select = int(input("Enter you choice:"))

print("Good bye :)")




