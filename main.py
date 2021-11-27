import random
randomNumber=random.randint(1,9)
chances=5
while(chances>0):
    number=int(input('ENTER A NUMBER BETWEEN 1&9 '))
    if(randomNumber==number):
        print('CONGRATULATION YOU GUESSED IT CORRECT')
        break
    elif(number<randomNumber):
        print('YOUR GUESS IS LESS PLS GUESS A HIGHER NUMBER')
    else:
        print('YOUR GUESS IS MORE PLS GUESS A LOWER NUMBER')
    chances -=1
if(chances==0):
    print('YOU LOSE AND THE NUMBER WAS ',randomNumber)