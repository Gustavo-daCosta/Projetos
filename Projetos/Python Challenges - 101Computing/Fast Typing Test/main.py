#Fast Typing Test Challenge - www.101computing.net/fast-typing-test/
import time
from os import system
from random import randint

system(command="clear")
def Level(textInput, condition, message):
    global totalStart, totalEnd, counter, start, end, averageTime
    counter = 1
    totalStart = time.time()
    while True:
        start=time.time()
        text = input(f"Type the {textInput} in the order: ").strip()
        end = time.time()
        if text.lower() == condition.lower():
            print(f"You typed the {message} in the correct order")
            break
        else:
            print(f"You typed the {message} in the wrong order")
            print("Try again!")
            counter += 1
    totalEnd = time.time()
    averageTime = str(round((totalEnd - totalStart)/counter, 2))

def Menu():
    global option

    print("><><><><><><><><><><><><><><><><><><><><><><><>")
    print(">             Reaction Time Tester            <")
    print("><><><><><><><><><><><><><><><><><><><><><><><>")
    print('''   Level [1] - Type the Alphabet
    Level [2] - Type the following quote: "The quick brown fox jumps over the lazy dog"
    Level [3] - Type a random pangram of the list:
    — “The quick brown fox jumps over the lazy dog”
    — “The five boxing wizards jump quickly”
    — “Pack my box with five dozen liquor jugs”
    — "The jay, pig, fox, zebra and my wolves quack!"
    — "By Jove, my quick study of lexicography won a prize!"
    Level [4] - Type a new phrase''')
    time.sleep(1)
    while True:
        try:
            option = int(input("Choose your level: "))
        except:
            print("Please, choose a number between 1 and 3")
            time.sleep(1)
        finally:
            if isinstance(option, int) and option in range(1,4):
                break
            else:
                print("Please, choose a number between 1 and 3")
                time.sleep(1)
    return option

pangrams = [
    "The quick brown fox jumps over the lazy dog",
    "The five boxing wizards jump quickly",
    "Pack my box with five dozen liquor jugs",
    "The jay, pig, fox, zebra and my wolves quack!",
    "By Jove, my quick study of lexicography won a prize!"
]

while True:
    Menu()
    system("cls")

    if option == 1:
        Level("alphabet", "abcdefghijklmnopqrstuvwxyz", "alphabet")
    elif option == 2:
        Level('quote: "The quick brown fox jumps over the lazy dog"',"The quick brown fox jumps over the lazy dog", "quote")
    elif option == 3:
        randomNum = randint(0, len(pangrams)-1)
        Level(f'pangram {pangrams[randomNum]}', pangrams[randomNum], "pangram")

    duration = round(end - start,2)
    totalTime = totalEnd - totalStart

    print(f"Reaction time in last attempt: {str(duration)} seconds")
    print(f"Total time: {totalTime:.1f} seconds")
    print(f"Total attempts: {counter}")
    print(f"Average time: {averageTime} seconds")
    input("Press Enter to continue...")
    system("cls")