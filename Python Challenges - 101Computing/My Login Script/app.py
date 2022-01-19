#My Login Script - www.101computing.net/my-login-script

# INCOMPLETO

from os import system

USERNAME="admin"
PASSWORD="p4$$W0rd"

while True:
    print("#####################")
    print("#    Login Screen   #")
    print("#####################")
    print('''[ 1 ] LOGIN 
    [ 2 ] CREATE USER
    [ 3 ] DELETE USER
    [ 4 ] EXIT''')

    while True:
        try:
            option = int(input("Enter your option: "))
        except:
            print("ERROR! Please enter a valid option")
        finally:
            if option in range(1,5):
                break
            else:
                print("ERROR! Please enter a valid option")
    if option == 1:
        print('login')
    
    elif option == 2:
        print('create user')
    
    elif option == 3:
        print('delete user')

    else:
        system('cls')
        print('Goodbye!')
        break