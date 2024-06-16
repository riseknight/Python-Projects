# Rock, Paper & Scissors (Python Code)

p1 = input('Player_1 input: ')
p2 = input('Player_2 input: ')

if (p1 == 'rock' or p1 == 'paper' or p1 == 'scissors') and (p2 == 'rock' or p2 == 'paper' or p2 == 'scissors'):
        if p1 == p2:
            print("it's a draw. ")
    
        elif (p1 == 'rock' and p2=='scissors') or (p1 == 'scissors' and p2 =='paper') or (p1 == 'paper' and p2 == 'rock'):
            print('Player_1 wins!')
        else:
            print('Player_2 wins')
else:
    print('Wrong input!') 

