'''
Library Management System

Commands:
- Add Book Details
- Edit Book Details
- Delete Book
- View Book List
- Issue Book to Student
- Return Book
'''

import db_commands

db_commands.DB_connection()

def menu(msg: str):
    msgLength = len(msg) // 2
    print("=-="*msgLength)
    print(msg.center(50))
    print("=-="*msgLength)

def ErrorTreat_STR(succes_msg: str, error_msg: str):
    print("ERROR")

def ErrorTread_INT() :
    print("int")

while True:
    menu("Library Management System")
    print("""[ 1 ] Add Book Details
[ 2 ] Edit Book Details
[ 3 ] Delete Book
[ 4 ] View Book List
[ 5 ] Issue Book to Student
[ 6 ] Return Book
[ 7 ] Quit Program""")
    while True:
        try:
            option = int(input("Select an option: "))
            if 0 < option < 8:
                break
            else:
                raise SyntaxError
        except (SyntaxError, ValueError, TypeError):
            print("Invalid option! Please enter an option between 1 and 6.")

    if option == 1:
        menu("Add Book Details")

    elif option == 2:
        menu("Edit Book Details")
    
    elif option == 3:
        menu("Delete Book")
    
    elif option == 4:
        menu("View Book List")
    
    elif option == 5:
        menu("Issue Book to Student")
    
    elif option == 6:
        menu("Return Book")
    
    else:
        print("Goodbye!")
        exit()
