# Cálculo da distância percorrida ao longo de um ano

londonTOoxford_miles = 60
distance_1year = ((londonTOoxford_miles*1.609)*2) * (52*5)
print(f'Yearly distance: {distance_1year:.0f}Km')

# Cálculo da distância de uma viagem de ida e volta para a Lua

EarthTOmoon_km = 383400
moonTrip = EarthTOmoon_km * 2

# Cálculo da quantidade de anos que levaria pra ir a Lua e voltar

years = moonTrip/distance_1year

print(f'Yuri would have travelled the equivalent of going to the Moon and back in {years:.0f} years!')