import random
import time

operators = ['+','-','*','//']
total_answers = 10

def guess():
    num1 = random.randint(1,15)
    num2 = random.randint(1,15)
    ope_selection = random.choice(operators)
    # inp = input('You want to start the operations? ').lower()

    operation = str(num1) +''+ ope_selection + '' + str(num2)
    result = eval(operation)
    return operation, result 
    # print(result)

start_time = time.time()
wrong = 0

for i in range(total_answers):
    operation,result = guess()
    while True:
        output = input('math question # '+ operation + " :")
        if output == str(result):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time,2)
print('Nice Work')
print('You can do it at ',total_time,'time period')



