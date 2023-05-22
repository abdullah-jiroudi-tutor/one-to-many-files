import random
def start_playing():
    global score
    diff=int(input("please select the diffculty :\n1-easy\n2-mid\n3-hard\nEnter your choise: "))
    counter=1
    if diff==1:
        print('welcome now we have a random number between 1 to 10 try to guess it within 3 times !')
        n = random.randint(1, 10)
    elif diff==2:
        print('welcome now we have a random number between 1 to 20 try to guess it within 3 times !')
        n = random.randint(1, 20)
    elif diff==3:
        print('welcome now we have a random number between 1 to 30 try to guess it within 3 times !')
        n = random.randint(1, 30)
    guess= int(input("Enter you guess : "))
    while guess !=n:
        if counter==3:
            print(" sorry you hit the number of limits :(")
            break
        if guess>n:
            print("too high !")
            guess = int(input("Enter you guess : "))
            counter=counter+1
        elif guess<n:
            print("too low !")
            guess = int(input("Enter you guess : "))
            counter=counter+1
    if guess==n:
        print("great you hit the number correct ! WOW")
        if diff==1:
            score = score + 1
        elif diff==2:
            score = score + 2
        elif diff==3:
            score = score + 3





score=0
print("Welcome to gusseing game ! :)")
print("menu : ")
print("1-start playing \n2-get score \n3-exit")
select=int(input("please select a number: "))
while select <3:
    if select==1:
        start_playing()
    if select==2:
        print("you score is: ",score)
    print("menu : ")
    print("1-start playing \n2-get score \n3-exit")
    select = int(input("please select a number: "))
print("thanks for playing good bye ! :)")
