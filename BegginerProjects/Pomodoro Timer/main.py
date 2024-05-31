from time import sleep
from os import system

checkmarks = 0

def defineTask():
    global task
    task = input("Define the task you wold like to work on: ")
    print(f'Your task: {task}')

defineTask()
while carryOn is True:
    print('Starting pomodoro timer')
    sleep(minutes = 25)
    system('clear')
    print('Pomodoro timer finished')
    checkmarks += 1
    if checkmarks == 4:
        print('Take a long break - 30 minutes')
        sleep(minutes = 30)
        checkmarks = 0
        print('The long break has ended.')
        input('Press enter to continue...')
        system('clear')
    else:
        print('Take a short break - 5 minutes')
        sleep(minutes = 5)
        print('The short break has ended')
        input('Press enter to continue...')
        system('clear')

    while True:
        carryOn = input("Do you want to continue? (y/n) ").lower()
        if carryOn == "y" or carryOn == "yes":
            carryOn = True
            continue
        elif carryOn == "n" or carryOn == "no":
            carryOn = False
            break
        else:
            print("Please answer yes or no.")

print('Goodbye!')

'''
    Extension Task #1:

To make your program more robust, you should make sure that the program only accepts a valid “Yes” or “No” answer to the question “Would you like to carry on?”.
To do so you will implement a validation routine to validate the user input. You can find more about Yes/No validation routines on this post.

Extension Task #2:

Add a few inputs at the start of the code for the user to change the settings of their pomodoro timer. The three settings that the user should be able to change are:
How long (in minutes) should a pomodoro interval last for (e.g. 25 minutes)?
How long (in minutes) should a short break last for (e.g. 5 minutes)?
How long (in minutes) should a long break last for (e.g. 30 minutes)?
Your program should then use the settings provided by the end-user.

Extension Task #3:

Add a “Reset” button to your program. When the user clicks the button, the pomodoro timer should reset to the default settings.

Extension Task #4:

Add a “Quit” button to your program. When the user clicks the button, the program should end.
'''