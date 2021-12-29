from os import system

while True:
    try:
        rating = int(input("Enter a rating between 0 and 5: "))
        if 0 <= rating <= 5:
            print("Thank you for your rating.")
            break
        else:
            print("Invalid Star Rating. Please enter a number between 0 and 5.")
            system('cls')
    except ValueError:
        print("Invalid Star Rating. Please try again.")
        system('cls')
print('Thank you!')