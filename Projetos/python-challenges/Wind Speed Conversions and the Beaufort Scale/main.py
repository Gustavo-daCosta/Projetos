forces = {
    0: ["Calm", 0, 1, "0 ft (0 m)", "Sea like a mirror","Smoke rises vertically"],
    1: ["Light air", "1–3 knots", "0–1 ft""Ripples with appearance of scales are formed, without foam crests","Direction shown by smoke drift but not by wind vanes."],
    2: ["Light breeze", "4-6 knots", "0-1 ft", "Small wavelets still short but more pronounced; crests have a glassy appearance but do not break","Wind felt on face; leaves rustle; wind vane moved by wind."],
    3: ["Gentle breeze", "7-10 knots", "2-4 ft", "Large wavelets; crests begin to break; foam of glassy appearance; perhaps scattered white horses","Leaves and small twigs in constant motion; light flags extended."],
    4: ["Moderate breeze", 11, 16, "3.5-6 ft", "Small waves becoming longer; fairly frequent white horses","Raises dust and loose paper; small branches moved."],
    5: ["Fresh breeze", 17, 21, "6-10 ft", "Moderate waves taking a more pronounced long form; many white horses are formed; chance of some spray","Small trees in leaf begin to sway; crested wavelets form on inland waters."],
    6: ["Strong breeze", 22, 27, "", "Large waves begin to form; the white foam crests are more extensive everywhere; probably some spray","Large branches in motion; whistling heard in telegraph wires; umbrellas used with difficulty."],
    7: ["High wind, moderate gale, near gale", "", "", "Sea heaps up and white foam from breaking waves begins to be blown in streaks along the direction of the wind; spindrift begins to be seen","Whole trees in motion; inconvenience felt when walking against the wind."],
    8: ["Gale, fresh gale", "", "", "Moderately high waves of greater length; edges of crests break into spindrift; foam is blown in well-marked streaks along the direction of the wind","Twigs break off trees; generally impedes progress."],
    9: ["Strong/severe gale", "", "", "High waves; dense streaks of foam along the direction of the wind; sea begins to roll; spray affects visibility","Slight structural damage (chimney pots and slates removed)."],
    10: ["Storm, whole gale", "", "", "Very high waves with long overhanging crests; resulting foam in great patches is blown in dense white streaks along the direction of the wind; on the whole the surface of the sea takes on a white appearance; rolling of the sea becomes heavy; visibility affected","Seldom experienced inland; trees uprooted; considerable structural damage."],
    11: ["Violent storm", "", "", "Exceptionally high waves; small- and medium-sized ships might be for a long time lost to view behind the waves; sea is covered with long white patches of foam; everywhere the edges of the wave crests are blown into foam; visibility affected","Very rarely experienced; accompanied by widespread damage."],
    12: ["Hurricane force", "", "", "The air is filled with foam and spray; sea is completely white with driving spray; visibility very seriously affected","Devastation"]
}

print('''Select a unit of speed:
1 - MPH (Meters per hour)
2 - Km/h (Kilometers per hour)
3 - Knot (Marine Knot)''')

while True:
    try:
        speedUnit = int(input('Select a unit of speed: '))
    except TypeError:
        print('ERROR! Invalid number')
    finally:
        if isinstance(speedUnit, int) is True:
            if speedUnit == 1 or speedUnit == 2 or speedUnit == 3:
                break
            else:
                print('ERROR! Type a number between 1 and 3')
while True:
    try:
        speed = float(input('Input the speed: '))
    except TypeError:
        print('ERROR! Invalid number')
    finally:
        if isinstance(speed, float) is True or isinstance(speed, int) is True:
            break

if speed == 1:
    knots = speed/1852
elif speed == 2:
    knots = speed/1.852
else:
    knots = speed

for force in range(0, 13):
    if knots == force:
        print(f'''KNOTS: {knots}
Description: ''')