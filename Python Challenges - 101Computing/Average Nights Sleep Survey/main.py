from os import system

carryOn = "y"
totalHours = 0
numberOfStudents = 0

while carryOn == "y":
    while True:
        try:
            hours = int(input('How many hours do you sleep each night? '))
        except:
            print('ERROR! Try again.')
        finally:
            if isinstance(hours, int) is True and hours <= 16:
                break
    totalHours += hours
    numberOfStudents += 1
    average = totalHours / numberOfStudents
    print(f"Average number of hour per night: {average:.1f}")
    while True:
        try:
            carryOn = str(input("Do you want to carry on with the survey? y/n: ")).lower()
            if carryOn != 'n' and carryOn != 'y':
                raise ValueError
            break
        except:
            print('ERROR! Please just type "Y" or "N"')
    if carryOn == 'y':
        print('GoodBye!')
        break
    system('cls')