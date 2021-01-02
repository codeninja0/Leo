import random
number = random.randint(1,100)
tries = 1
while True:
    userinput = int(input("Guess a number between 1 and 100: "))
    if userinput > number:
        print("My number is less than that")
        tries = tries + 1
    if userinput < number:
        print("My number is greater than that")
        tries = tries + 1
    if userinput == number:
        #print("My number is",number)
        if tries == 1:
            print("WHAT!!!! YOU ONLY TOOK 1 TRY!!!!!")
   
        if tries > 7:
            print("YOU SUCK!")
            print('You took',tries,'tries')
        if tries <= 7 and tries > 1:
            print("YOU ARE AWESOME!")
            print('You took',tries,'tries')

        #break


     