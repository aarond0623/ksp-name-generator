from random import choice

vehicleprefix = {
        'A': 'aircraft',
        'B': 'base',
        'D': 'probe',
        'L': 'lander',
        'O': 'space shuttle',
        'P': 'spaceplane',
        'R': 'rover',
        'S': 'space station',
        'T': 'satellite',
        'V': 'spaceship',
        'Z': 'no vessel'
}

purposeprefix = {
        'C': 'crew transport',
        'D': 'unmanned',
        'F': 'fuel',
        'H': 'heavy cargo',
        'K': 'communication',
        'N': 'scanner',
        'R': 'rescue',
        'X': 'experimental',
        'Y': 'science'
}

liftersuffix = {
        'A': 'suborbital',
        'B': 'low orbital',
        'C': 'high orbital',
        'D': 'lunar',
        'E': 'interplanetary'
}

names_a = [
        'Aether',
        'Aurora',
        'Skyward',
        'Stratos'
]

names_e = [
        'Astral',
        'Celestia',
        'Cosmos',
        'Elysium',
        'Expanse',
        'Odyssey',
        'Stellaris'
]

names = [
        'Aegis',
        'Aeon',
        'Arcadia',
        'Ardent',
        'Argo',
        'Ascendant',
        'Astra',
        'Astralis',
        'Astrid',
        'Athena',
        'Calypso',
        'Catalyst',
        'Cronos',
        'Daedalus',
        'Eclipse',
        'Ecliptic',
        'Epoch',
        'Equinox',
        'Eventide',
        'Frontier',
        'Galatea',
        'Genesis',
        'Helios',
        'Hermes',
        'Horizon',
        'Hyperion',
        'Illumina',
        'Ion',
        'Ionis',
        'Lumina',
        'Meridian',
        'Nebula',
        'Nebulon',
        'Nexus',
        'Nova',
        'Obsidian',
        'Olympic',
        'Orenda',
        'Paragon',
        'Parallax',
        'Phaedra',
        'Pioneer',
        'Poseidon',
        'Prometheus',
        'Radiance',
        'Radiant',
        'Seraph',
        'Serenity',
        'Solara',
        'Solaris',
        'Solstice',
        'Spectra',
        'Tempest',
        'Tempora',
        'Titan',
        'Titanus',
        'Valiant',
        'Vanguard',
        'Vesper',
        'Vortex',
        'Zenith'
]

print("Select a vessel type: ")
selectionlist = sorted(vehicleprefix.items(), key=lambda x: x[1])
for i, item in enumerate(selectionlist):
    print(f"{i+1}. {item[1]}")
while True:
    selection = input("Enter value: ")
    try:
        selection = int(selection)
        break
    except:
        continue
vessel = selectionlist[selection - 1][0]

print("Select a purpose prefix, or 0 for none: ")
selectionlist = sorted(purposeprefix.items(), key=lambda x: x[1])
for i, item in enumerate(selectionlist):
    print(f"{i+1}. {item[1]}")
while True:
    selection = input("Enter value: ")
    try:
        selection = int(selection)
        break
    except:
        if selection == '':
            selection = 0
            break
        continue
if selection == 0:
    purpose = ''
else:
    purpose = selectionlist[selection - 1][0]

print("Select a lifter suffix, or 0 for none: ")
selectionlist = sorted(liftersuffix.items(), key=lambda x: x[1])
for i, item in enumerate(selectionlist):
    print(f"{i+1}. {item[1]}")
while True:
    selection = input("Enter value: ")
    try:
        selection = int(selection)
        break
    except:
        if selection == '':
            selection = 0
            break
        continue
if selection == 0:
    lifter = ''
else:
    lifter = f"/{selectionlist[selection - 1][0]}"

number = input("Enter iteration number: ")

name = f"{vessel}{purpose}-{number}{lifter}"

print(name)

selection = input("Would you like a mission name? y/N: ")

while selection.lower() == 'y':
    if vessel in 'AHP' or lifter == 'A':
        names += names_a
    if lifter == 'E':
        names += names_e
    mission = choice(names)
    print(f"{name} {mission}")
    selection = input("Choose a different mission name? y/N: ")
