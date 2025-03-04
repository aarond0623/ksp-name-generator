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


def menu(prompt_text: str, choices: list[str], optional: bool = True) -> str:
    print(prompt_text)
    for i, item in enumerate(choices):
        print(f"{i + 1}. {item}")
    while True:
        selection = input("Enter choice: ")
        try:
            assert 0 < int(selection) <= len(choices)
            break
        except:
            if optional and selection == '':
                return ''
            continue
    return choices[int(selection) - 1]


def confirm(prompt_text: str, yes_default: bool = False) -> bool:
    if yes_default:
        yn = "[Y/n]"
    else:
        yn = "[y/N]"
    prompt_text = f"{prompt_text} {yn}: "
    confirmation = input(prompt_text).lower()
    while confirmation not in ['y', 'n', 'yes', 'no', '']:
        confirmation = input(prompt_text).lower()
    if confirmation in ['y', 'yes'] or (confirmation == '' and yes_default):
        return True
    if confirmation in ['n', 'no'] or (confirmation == '' and not yes_default):
        return False
    return False


name = ""

vessel_list = sorted(vessels.keys())
vessel = menu("Select a vessel type, or blank for none: ", vessel_list)
name += vessels.get(vessel, '')
print()

if vessel in ['aircraft', 'capsule', 'lander',
              'rover', 'space plane', 'space shuttle', '']:
    manned_list = sorted(manned_state.keys())
    manned = menu("Select manned/unmanned: ", manned_list, False)
    name += manned_state[manned]
    print()

    if confirm("Is this vessel experimental?"):
        name = 'X' + name
    print()

name = name[0:2]

number = input("Enter iteration of this vessel type: ")
name += f"-{number}"
print()

mission_list = sorted(missions.keys())
mission = menu("Select a mission suffix, or blank for none: ", mission_list)
name += missions.get(mission, '')
print()

lifter_list = [x[0] for x in sorted(lifters.items(), key=lambda x: x[1])]
lifter = menu("Select a lifter suffix, or blank for none: ", lifter_list)
name += lifters.get(lifter, '')
print()

print(f"VESSEL NAME: {name}")
print()

if confirm("Would you like a mission name?"):
    if (vessel in ['aircraft', 'space plane', 'space shuttle']
            or lifter == 'suborbital'):
        names += names_a
    if lifter == 'interplanetary':
        names += names_e
    while True:
        mission = choice(names)
        print()
        print(f"VESSEL NAME: {name} {mission}")
        print()
        if not confirm("Choose a different mission name?", True):
            break
