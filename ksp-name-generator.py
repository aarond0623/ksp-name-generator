from random import choice

vessels = {
        'aircraft': 'A',
        'base': 'BS',
        'capsule': 'C',
        'lander': 'L',
        'launcher': 'W',
        'rover': 'R',
        'satellite': 'S',
        'space plane': 'S',
        'space shuttle': 'O',
        'space station': 'SS'
}

manned_state = {
    'manned': 'V',
    'unmanned': 'P'
}

missions = {
        'crew transport': 'C',
        'fuel': 'F',
        'cargo': 'K',
        'scanner': 'N',
        'rescue': 'R',
        'communication': 'T',
        'science': 'Y'
}

lifters = {
        'suborbital': '/a',
        'low orbital': '/b',
        'high orbital': '/c',
        'lunar': '/d',
        'interplanetary': '/e'
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

name = ""

print("Select a vessel type, or blank for none: ")
selectionlist = sorted(vessels.keys())
for i, item in enumerate(selectionlist):
    print(f"{i + 1}. {item}")
while True:
    selection = input("Enter value: ")
    try:
        selection = int(selection)
        assert 0 < selection <= len(selectionlist)
        vessel = selectionlist[selection - 1]
        break
    except:
        if selection == '':
            vessel = ''
            break
        continue

name += vessels.get(vessel, '')

if vessel in ['aircraft', 'capsule', 'lander', 'rover', 'space plane', 'space shuttle', '']:
    print("Select manned/unmanned: ")
    selectionlist = sorted(manned_state.keys())
    for i, item in enumerate(selectionlist):
        print(f"{i + 1}. {item}")
    while True:
        selection = input("Enter value: ")
        try:
            selection = int(selection)
            assert 0 < selection <= len(selectionlist)
            manned = selectionlist[selection - 1]
            break
        except:
            continue
    name += manned_state[manned]

number = input("Enter iteration number: ")
name += f"-{number}"

print("Select a mission suffix, or blank for none: ")
selectionlist = sorted(missions.keys())
for i, item in enumerate(selectionlist):
    print(f"{i + 1}. {item}")
while True:
    selection = input("Enter value: ")
    try:
        selection = int(selection)
        assert 0 < selection <= len(selectionlist)
        mission = selectionlist[selection - 1]
        break
    except:
        if selection == '':
            mission = ''
            break
        continue

name += missions.get(mission, '')

print("Select a lifter suffix, or blank for none: ")
selectionlist = sorted(lifters.keys())
for i, item in enumerate(selectionlist):
    print(f"{i + 1}. {item}")
while True:
    selection = input("Enter value: ")
    try:
        selection = int(selection)
        assert 0 < selection <= len(selectionlist)
        lifter = selectionlist[selection - 1]
        break
    except:
        if selection == '':
            lifter = ''
            break
        continue

name += lifters.get(lifter, '')

print(name)

selection = input("Would you like a mission name? y/N: ")

while selection.lower() == 'y':
    if vessel in ['aircraft', 'space plane', 'space shuttle'] or lifter == 'suborbital':
        names += names_a
    if lifter == 'interplanetary':
        names += names_e
    mission = choice(names)
    print(f"{name} {mission}")
    selection = input("Choose a different mission name? y/N: ")
