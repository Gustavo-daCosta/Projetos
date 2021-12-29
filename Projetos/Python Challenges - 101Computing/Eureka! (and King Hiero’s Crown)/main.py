
while True:
    try:
        mass = float(input('Enter the mass of the object in kilograms: '))
        volume = float(input('Enter the volume of the object in cubic meters: '))
    except ValueError:
        print('\nPlease enter a number.')
    finally:
        break
density = mass / volume

Metal = {
    'Aluminum': [2.4, 2.7],
    'Bronze': [8.1, 8.3],
    'Silver': [10.4, 10.6],
    'Lead': [11.2, 11.4],
    'Gold': [17.1, 17.5],
    'Platinum': [21.0, 21.5],
}

for metal in Metal:
    if density >= Metal[metal][0] and density <= Metal[metal][1]:
        print('\nThe metal is', metal)
        break
else:
    print('\nThe metal is not found.')

print(f'The density of the object is {density:.2f} kg/m^3')