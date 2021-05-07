import re
n = int(input())
plant_info = {}
for _ in range(n):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    plant_info[plant] = {'rarity': rarity, 'ratings': []}

data = input()
while not data == 'Exhibition':
    command, parameters = data.split(': ')
    if command == "Rate":
        plant_name, parameters = parameters.split(" - ")
        parameters = int(parameters)
        if plant_name in plant_info:
            plant_info[plant_name]['ratings'].append(parameters)
        else:
            print("error")
    elif command == "Update":
        plant_name, rarity = parameters.split(" - ")
        rarity = int(rarity)
        if plant_name in plant_info:
            plant_info[plant_name]['rarity'] = rarity
        else:
            print("error")
    elif command == "Reset":
        plant_name = parameters
        if plant_name in plant_info:
            plant_info[parameters]['ratings'].clear()
        else:
            print("error")
    else:
        print("error")

    data = input()

for pl_name, value_plant in plant_info.items():
    if value_plant['ratings']:
        avr = sum(value_plant['ratings'] )/ len(value_plant['ratings'])
    else:
        avr = 0
    plant_info[pl_name]['average'] = avr

sorted_plants = sorted(plant_info.items(), key=lambda tkvp: (-tkvp[1]['rarity'], -tkvp[1]['average']))
print("Plants for the exhibition:")
for key, value in sorted_plants:
    print(f'- {key}; Rarity: {value["rarity"]}; Rating: {value["average"]:.2f}')
