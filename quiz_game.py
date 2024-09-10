
quiz = input('Are you interested to start the quiz ? ').lower()
correct = 0

if quiz == 'yes':

    ans = input('what is full form of CPU ? ').lower()
    if ans == 'central processing unit':
        print('Correct!')
        correct += 1
    else:
        print('Incorrect!')

    ans = input('what is full form of GPU ? ').lower()
    if ans == 'graphics processing unit':
        print('Correct!')
        correct += 1
    else:
        print('Incorrect!')

    ans = input('what is full form of RAM ? ').lower()
    if ans == 'random access memory':
        print('Correct!')
        correct += 1
    else:
        print('Incorrect!')

    ans = input('what is full form of UPS ? ').lower()
    if ans == 'unit processing':
        print('Correct!')
        correct += 1
    else:
        print('Incorrect!')
    
    print('You got an ',correct/4*100,'%')
    
else:
    print('Thank You!')
    print('if you want to start it rerun code :)')

