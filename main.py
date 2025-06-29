import requests

projects = {}

# "mod-id" : [available, required, selfUpdate]
server_projects = {
    "fabric-api": [False, True, False],
    "muffintime-resource-pack": [False, True, True],
    "invis-item-frame": [True, False, False],  # Old version works fine
    "muffintime-data-pack": [False, True, True],
    "armorstandeditor": [False, False, False],
    "bluemap-banners": [False, True, True],
    "better-log4j-config": [True, True, False],  # Old version works fine
    "bluemap": [False, True, False],
    "carpet": [False, False, False],
    "chathook": [False, True, True],
    "chunky": [False, False, False],
    "clumps": [False, True, False],
    "litemoretica": [False, False, False],
    "c2me-fabric": [False, True, False],
    "fabric-language-kotlin": [False, True, False],
    "ferrite-core": [False, True, False],
    "fsit": [False, True, False],
    "invview": [False, False, False],
    "krypton": [False, True, False],
    "lithium": [False, True, False],
    "noisium": [False, True, False],
    "no-chat-reports": [False, True, False],
    "player-roles": [False, True, False],
    "player-statistics": [False, False, False],
    "servercore": [False, True, False],
    "shulkerboxtooltip": [False, True, False],
    "simple-voice-chat": [False, True, False],
    "spark": [False, False, False],
    "snowball-and-egg-knockback": [False, True, False],
    "tabtps": [False, True, False],
    "vmp-fabric": [False, True, False],
    "worldedit": [False, False, False]
}

client_projects = {
    "fabric-api": [False, True, False],
    "muffintime-resource-pack": [False, True, True],
    "muffintime-data-pack": [False, True, True],
    "3dskinlayers": [False, True, False],
    "asteroid": [False, True, False],
    "bettertab": [False, False, False],
    "capes": [False, False, False],
    "cloth-config": [False, True, False],
    "continuity": [False, True, False],
    "c2me-fabric": [False, False, False],
    "cosmetica": [False, False, False],
    "distanthorizons": [False, True, False],
    "effective": [False, False, False],
    "ebe": [False, True, False],
    "fabric-language-kotlin": [False, True, False],
    "ferrite-core": [False, True, False],
    "flashback": [False, True, False],
    "freecam": [False, True, False],
    "indium": [False, True, False],
    "iris": [False, False, False],
    "krypton": [False, True, False],
    "lambdynamiclights": [False, True, False],
    "lighty": [False, True, False],
    "litematica": [False, True, False],
    "litemoretica": [False, False, False],
    "lithium": [False, True, False],
    "malilib": [False, True, False],
    "midnightlib": [False, True, False],
    "modmenu": [False, True, False],
    "nbttooltip": [False, True, False],
    "no-chat-reports": [False, True, False],
    "no_fog": [False, True, False],
    "no-resource-pack-warnings": [False, True, False],
    "mpalladium": [False, True, False],
    "reeses-sodium-options": [False, True, False],
    "screenshot-to-clipboard": [False, False, False],
    "shulkerboxtooltip": [False, False, False],
    "simple-voice-chat": [False, True, False],
    "smooth-scroll": [False, True, False],
    "sodium": [False, True, False],
    "sodium-extra": [False, True, False],
    "sodium-shadowy-path-blocks": [False, True, False],
    "twitch-chat": [False, False, True],
    "viafabricplus": [False, True, False],
    "worldedit": [False, False, False],
    "worldedit-cui": [False, False, False],
    "xaeros-minimap": [False, True, False],
    "xaeros-world-map": [False, True, False],
    "xaeroplus": [False, True, False],
    "yacl": [False, True, False]
}

talkToMe = input("Check server or client: ")
if talkToMe.lower() == "server":
    projects = server_projects
elif talkToMe.lower() == "client":
    projects = client_projects

apiUrl = "https://api.modrinth.com/v2/"
mcVersion = "1.21.6"

for key in projects.keys():
    response = requests.get(apiUrl + f"project/{key}/version")

    if response.status_code == 200:
        versions = response.json()
        available = [v for v in versions if mcVersion in v['game_versions']]
        if available:
            projects[key][0] = True

    else:
        print(f"Error {key}: {response.status_code}")
        print(response.text)

checkedMods = 0
availableMods = 0
availableModsWhenSelfUpdate = 0


for key in projects.keys():
    checkedMods += 1
    if projects[key][0] is True:
        availableMods += 1
    elif projects[key][2] is True:
        availableModsWhenSelfUpdate += 1

print(f"There are {round((availableMods/checkedMods) * 100, 2)}% of projects available. ({availableMods})")
print(f"There are {round(((availableMods + availableModsWhenSelfUpdate)/checkedMods) * 100, 2)}% of projects available, when self updated. ({availableMods + availableModsWhenSelfUpdate})")
print(f"There are {checkedMods} projects.\n")


requiredCheckedMods = 0
requiredAvailableMods = 0
requiredAvailableModsWhenSelfUpdate = 0

for key in projects.keys():
    if projects[key][1] is True:
        requiredCheckedMods += 1
        if projects[key][0] is True:
            requiredAvailableMods += 1
        elif projects[key][2] is True:
            requiredAvailableModsWhenSelfUpdate += 1

print(f"There are {round((requiredAvailableMods/requiredCheckedMods) * 100, 2)}% of required projects available. ({requiredAvailableMods})")
print(f"There are {round(((requiredAvailableMods + requiredAvailableModsWhenSelfUpdate)/requiredCheckedMods) * 100, 2)}% of required projects available, when self updated. ({requiredAvailableMods + requiredAvailableModsWhenSelfUpdate})")
print(f"There are {requiredCheckedMods} required projects.\n")

print("These mods are not yet available:")
for key in projects.keys():
    if projects[key][0] is False:
        print(key, f" - https://modrinth.com/mod/{key}")
