# INPUT

weightOnEarth = float(input('Type your weight in kg: '))

# PROCESS

planets = {
    'Earth': weightOnEarth,
    'Moon': (weightOnEarth/9.81) * 1.622,
    'Mercury': (weightOnEarth/9.81) * 3.7,
    'Venus': (weightOnEarth/9.81) * 8.87,
    'Mars': (weightOnEarth/9.81) * 3.711,
    'Jupiter': (weightOnEarth/9.81) * 24.79,
    'Saturn': (weightOnEarth/9.81) * 10.44,
    'Uranus': (weightOnEarth/9.81) * 8.69,
    'Neptune': (weightOnEarth/9.81) * 11.15,
}

# OUTPUT

print(f'PLANET\t\tWEIGHT')
print('-'*22)
for planet, weight in planets.items():
    print(f'{planet}\t\t{weight:.1f}Kg')
print('-'*22)