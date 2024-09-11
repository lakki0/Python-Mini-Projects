from cryptography.fernet import Fernet

master_pass = input('What is master password? ')

# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key','wb') as file:
#         file.write(key)
# write_key()

def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key 

key = load_key() + master_pass.encode()
fern_key = Fernet(key)
# print(key) 

def add():
    userName = input('user name : ')
    userPass = input('user password : ')

    with open('password.txt','a') as f:
        f.write(userName+' | '+str(fern_key.encrypt(userPass.encode()).decode())+'\n')

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            userName , password = data.split('|')
            # print(userName,password)
            print(userName,'|',fern_key.decrypt(password.encode()).decode())

while True:
    user_inp = input('Would you like to add new password or view or quit q? ').lower()

    if user_inp == 'q':
        break

    if user_inp == 'add':
        add()
    
    elif user_inp == 'view':
        view()
    
    else:
        print('Invalid input')
        continue




