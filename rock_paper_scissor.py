import random

user_win = 0
comp_win = 0
options = ['rock','paper','scissor']

while True:
    user_input = input('type rock/paper/scissor or for quit Q ').lower()
    
    if user_input == 'q':
        break

    if user_input not in options:
        continue
    
    random_num = random.randint(0,2)
    # print(random_num)
    comp_guess = options[random_num]
    print(comp_guess)

    if user_input == 'rock' and comp_guess == 'scissor':
        print('You won!')
        user_win += 1
    
    elif user_input == comp_guess:
        print('Draw Match!')

    elif user_input == 'paper' and comp_guess == 'rock':
        print('You won!')
        user_win += 1
    
    elif user_input == 'scissor' and comp_guess == 'paper':
        print('You won!')
        user_win += 1
    
    else:
        print('Computer win!')
        comp_win += 1

print('You win',user_win,'times')
print('Computer win',comp_win,'times')
