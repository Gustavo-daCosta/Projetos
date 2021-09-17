# Your task is to write a Python script to generates a random date in the format: DD/MM/YYYY.

from datetime import date
from random import randint

# Verificação para saber se o ano é bissexto
def leap_year(gen_year):
    if (gen_year % 4 == 0):
        if gen_year % 100 == 0:
            if gen_year % 400 == 0:
                isLeap = True
            else:
                isLeap = False
        else:
            isLeap = True 
    else:
        isLeap = False
    return isLeap

actualDate = date.today()

print(actualDate)

# Generate Year
year = randint(0, actualDate.year)
if year < 10:
    year = f'000{year}'
elif year >= 10 and year < 100:
    year = f'00{year}'
elif year >= 100 and year < 1000:
    year = f'0{year}'
else:
    year = str(year)

# Generate Month
month = randint(1, 12)
if month < 10:
    month = str(month)
    month = '0' + month
else:
    month = str(month)

# Generate Day
days31 = [1, 3, 5, 7, 8, 10, 12]
if month in days31:
    day = randint(1, 31)
elif month not in days31 and month != 2:
    day = randint(1, 30)
else:
    if leap_year() is False:
        day = randint(1, 28)
    else:
        day = randint(1, 29)
if day < 10:
    day = f'0{day}'
else:
    day = str(day)

date = f'{day}/{month}/{year}'
print(f'Generated date: {date}')