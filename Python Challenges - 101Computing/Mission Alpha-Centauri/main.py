import os

starDict = {
    'Alpha Centauri': [0, 4.24],
    "Barnard's Star": [1, 5.96],
    'Luhman 16': [2, 6.59],
    'WISE 0855-0714': [3, 7.2],
    'Wolf 359': [4, 7.78]
}
counter = 0

print(f'''
---------------------------------------------------------
                        SELECT A STAR
---------------------------------------------------------''')
for star, lightYears in starDict.items():
    counter += 1
    print(f'[{counter}] {star}\t\t{lightYears[1]} light-years')

while True:
    try:
        star = int(input('Type the number of the star: '))
    except:
        print('ERRO! Digite uma opção válida.')
    finally:
        if (star in starDict.keys()):
            break
        elif star >= 1 and star <= 6:
            break
        else:
            print('ERRO! Digite uma opção válida')


# 1. Calculate the number of seconds in a year
secondsYear = (((1*60)*60)*24)*365

# 2. Multiply this number by the speed of light
lightSpeed = 300000
distance = lightSpeed * secondsYear

# 3. Multiply this number by 4.2 (the distence of Alpha-Centauri from Earth in light-years)
for nameStar, lightYears in starDict.items():
    if star-1 == lightYears[0]:
        nameStar = star
        starDistance = lightYears[1]
distance = distance * starDistance

# 4. Output the result/distance in km

print(f'The distance from Earth to {nameStar} is {distance:.0f} km')