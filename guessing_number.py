import random

top_value = input('Enter top most number ')

if(top_value.isdigit()):
    top_value = int(top_value)

    if top_value <= 0:
        print('please enter number greater than zero')
        quit()
else:
    print('please enter next time as a number')
    quit()

guessing_num = random.randint(0,top_value)
attempts = 1

while True:
    attempts += 1
    user_num = input('enter the guessing number ')

    if(user_num.isdigit()):
        user_num = int(user_num)
        if user_num == guessing_num:
            print('Correct!')
            break
        elif user_num<guessing_num:
            print('Incorrect!')
            print('entered number is lesser')
        else:
            print('Incorrect!')
            print('entered number is greater')

    else:
        print('please enter next time as a number')
        

print('your attempts are',attempts)





