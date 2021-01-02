#user makes 3 choices
#1st choice - sword/arrows/pistol
#2st choice - left/right
#3nd choice - run/fight
#4rd choice - help/kill
health = 6
print('Your health is:',health)
arrows = 7
weapon = input('Choose your weapon - sword ⚔️ or arrows 🏹: ').lower().strip()
if weapon == 'sword':
    print('Good choice!')
    left_right = input('Enter left or right: ').lower().strip()
    if left_right == 'left':
        print('Nice! You chose the right path!')
        print('Remaining health:' ,health)
    if left_right == 'right':
        print('oof! You bonk into a tree and lose 2 health!')
        health = health - 2
        print('Remaining health:' ,health)
    bear_choice = input('AHHHH!!!!! There is a bear!! Do you attack or run:').lower().strip()
    if bear_choice == 'attack':
        print('NICE! You succesfully speared the bear in pieces!')
        print('Remaining health:' ,health)
    if bear_choice == 'run':
        print('NO!! The bear catches you and scratches you on the arm! You lose 2 health!')
        health = health - 2
        print('Remaining health:' ,health)
    sleep_choice = input('You are extremely tired. Do you continue or sleep:').lower().strip()
    if sleep_choice == 'sleep':
        print('Congrats! You gained 2 health!')
        health = health + 2
        print('Remaining health:' ,health)
    if sleep_choice == 'continue':
        print('Bad choice! You were very tired. You lost 3 health')
        health = health - 3
        print('Remaining health:' ,health)



elif weapon == 'arrows' or 'arrow':
    print('Good choice! You have',arrows,'arrows')
    left_right = input('Do you choose left or right: ').lower().strip()
    if left_right == 'left':
        print('Nice! You chose the right path!')
        print('Arrows left:',arrows)
        print('Remaining health:' ,health)
    if left_right == 'right':
        print('oof! You bonk into a tree and and loose 2 health!')
        print('Arrows left:',arrows)
        health = health - 2
        print('Remaining health:' ,health)
    bear_choice = input('AHHHH!!!!! There is a bear!! Do you attack or run:').lower().strip()
    if bear_choice == 'attack':
        print('NICE! You succesfully speared the bear in pieces!')
        arrows = arrows - 2
        print('Arrows left:',arrows)
        print('Remaining health:' ,health)
        
    if bear_choice == 'run':
        print('NO!! The bear catches you and scratches you on the arm! You lose 2 health!')
        print('Arrows left:',arrows)
        health = health - 2
        print('Remaining health:' ,health)
    sleep_choice = input('You are extremely tired. Do you continue or sleep:').lower().strip()
    if sleep_choice == 'sleep':
        print('Congrats! You gained 2 health!')
        print('Arrows left:',arrows)
        health = health + 1
        print('Remaining health:' ,health)
    if sleep_choice == 'continue':
        print('Bad choice! You were very tired. You lost 3 health')
        print('Arrows left:',arrows)
        health = health - 3
        print('Remaining health:' ,health)
if health<1:
    print("Oh no! You lost all you health! GAME OVER 😔😔😔")
if arrows<1:
    print("Oh no! You lost all you arrows! GAME OVER 😔😔😔")



     









