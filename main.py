import requests
import os

projects = {}
download = False

apiUrl = "https://api.modrinth.com/v2/"
mcVersion = "1.21.10"

# project types
typeMod = "fabric"
typeResourcePack = "minecraft"  # modrinths loader variant for resourcepacks
typeDataPack = "datapack"

# "mod-id" : [type, available, required, selfUpdate]
server_projects = {
    "fabric-api": [typeMod, False, True, False],
    "muffintime-resource-pack": [typeResourcePack, False, True, True],
    "muffintime-data-pack": [typeDataPack, False, True, True],
    "armorstandeditor": [typeMod, False, False, False],
    "bluemap-banners": [typeMod, False, True, True],
    "better-log4j-config": [typeMod, False, True, True],
    "bluemap": [typeMod, False, True, False],
    "carpet": [typeMod, False, False, False],
    "chathook": [typeMod, False, True, True],
    "chunky": [typeMod, False, False, False],
    "clumps": [typeMod, False, True, False],
    "disconnect-packet-fix": [typeMod, False, True, False],
    "litemoretica": [typeMod, False, False, False],
    "c2me-fabric": [typeMod, False, True, False],
    "fabric-language-kotlin": [typeMod, False, True, False],
    "ferrite-core": [typeMod, False, True, False],
    "fsit": [typeMod, False, True, False],
    "invview": [typeMod, False, False, False],
    "krypton": [typeMod, False, True, False],
    "lithium": [typeMod, False, True, False],
    "noisium": [typeMod, False, True, False],
    "no-chat-reports": [typeMod, False, True, False],
    "player-roles": [typeMod, False, True, False],
    "player-statistics": [typeMod, False, False, False],
    "servercore": [typeMod, False, True, False],
    "shulkerboxtooltip": [typeMod, False, True, False],
    "simple-voice-chat": [typeMod, False, True, False],
    "spark": [typeMod, False, False, False],
    "snowball-and-egg-knockback": [typeMod, False, False, False],
    "tabtps": [typeMod, False, True, False],
    "vmp-fabric": [typeMod, False, True, False],
    "worldedit": [typeMod, False, False, False]
}

client_projects = {
    "fabric-api": [typeMod, False, True, False],
    "muffintime-resource-pack": [typeResourcePack, False, True, True],
    "muffintime-data-pack": [typeDataPack, False, True, True],
    "3dskinlayers": [typeMod, False, True, False],
    "asteroid": [typeMod, False, True, False],
    "bettertab": [typeMod, False, False, False],
    "capes": [typeMod, False, False, False],
    "cloth-config": [typeMod, False, True, False],
    "continuity": [typeMod, False, True, False],
    "c2me-fabric": [typeMod, False, False, False],
    "cosmetica": [typeMod, False, False, False],
    "distanthorizons": [typeMod, False, True, False],
    "effective": [typeMod, False, False, False],
    "ebe": [typeMod, False, True, False],
    "fabric-language-kotlin": [typeMod, False, True, False],
    "ferrite-core": [typeMod, False, True, False],
    "flashback": [typeMod, False, True, False],
    "freecam": [typeMod, False, True, False],
    "indium": [typeMod, False, True, False],
    "iris": [typeMod, False, False, False],
    "krypton": [typeMod, False, True, False],
    "lambdynamiclights": [typeMod, False, True, False],
    "lighty": [typeMod, False, True, False],
    "litematica": [typeMod, False, True, False],
    "litemoretica": [typeMod, False, False, False],
    "lithium": [typeMod, False, True, False],
    "malilib": [typeMod, False, True, False],
    "midnightlib": [typeMod, False, True, False],
    "modmenu": [typeMod, False, True, False],
    "nbttooltip": [typeMod, False, True, False],
    "no-chat-reports": [typeMod, False, True, False],
    "no_fog": [typeMod, False, True, False],
    "no-resource-pack-warnings": [typeMod, False, True, False],
    "mpalladium": [typeMod, False, True, False],
    "reeses-sodium-options": [typeMod, False, True, False],
    "screenshot-to-clipboard": [typeMod, False, False, False],
    "shulkerboxtooltip": [typeMod, False, False, False],
    "simple-voice-chat": [typeMod, False, True, False],
    "smooth-scroll": [typeMod, False, True, False],
    "sodium": [typeMod, False, True, False],
    "sodium-extra": [typeMod, False, True, False],
    "sodium-shadowy-path-blocks": [typeMod, False, True, False],
    "twitch-chat": [typeMod, False, False, True],
    "viafabricplus": [typeMod, False, True, False],
    "worldedit": [typeMod, False, False, False],
    "worldedit-cui": [typeMod, False, False, False],
    "xaeros-minimap": [typeMod, False, True, False],
    "xaeros-world-map": [typeMod, False, True, False],
    "xaeroplus": [typeMod, False, True, False],
    "yacl": [typeMod, False, True, False],
    "stonecutter-gui-remastered": [typeMod, False, True, False],
    "status-effect-bars": [typeMod, False, True, False],
    "sound": [typeMod, False, True, False],
    "rrls": [typeMod, False, True, False],
    "modelfix": [typeMod, False, True, False],
    "flightspeed": [typeMod, False, True, False],
    "screentoclip": [typeMod, False, True, False],
    "chat-calc-kt": [typeMod, False, True, False],
    "chatanimation": [typeMod, False, True, False],
    "smooth-gui": [typeMod, False, True, False],
    "bundles-beyond": [typeMod, False, True, False],
    "boat-item-view": [typeMod, False, True, False],
    "super-fast-math": [typeMod, False, True, False],
    "scalablelux": [typeMod, False, True, False],
    "scribble": [typeMod, False, True, False],
    "symbol-chat": [typeMod, False, True, False]
}

os.makedirs("downloads", exist_ok=True)
os.makedirs("downloads/" + typeMod, exist_ok=True)
os.makedirs("downloads/" + typeResourcePack, exist_ok=True)
os.makedirs("downloads/" + typeDataPack, exist_ok=True)

talkToMe = input(f"Check server or client for version {mcVersion} (server/client): ")
if talkToMe.lower() == "server":
    projects = server_projects
elif talkToMe.lower() == "client":
    projects = client_projects

talkToMeTwo = input(f"Download projects (yes/no)?  ")
if talkToMeTwo.lower() == "y" or talkToMeTwo.lower() == "yes":
    download = True

for key in projects.keys():
    response = requests.get(apiUrl + f"project/{key}/version")

    if response.status_code == 200:
        versions = response.json()

        available = [
            v for v in versions
            if mcVersion in v['game_versions'] and projects[key][0] in v['loaders']
        ]

        if available:
            if download:
                # Sort by date_published descending to get the latest first
                available.sort(key=lambda v: v['date_published'], reverse=True)

                print(f"Downloading version for {key}: {available[0]['version_number']}" if available else f"No version for {key}")

                file_info = available[0]["files"][0]
                file_response = requests.get(file_info["url"])

                file_path = f"downloads/{projects[key][0]}/{file_info['filename']}"
                with open(file_path, "wb") as f:
                    f.write(file_response.content)

            projects[key][1] = True

    else:
        print(f"Error fetching {key}: {response.status_code}")
        print(response.text)

checkedMods = 0
availableMods = 0
availableModsWhenSelfUpdate = 0


for key in projects.keys():
    checkedMods += 1
    if projects[key][1] is True:
        availableMods += 1
    elif projects[key][3] is True:
        availableModsWhenSelfUpdate += 1

print(f"\nThere are {round((availableMods/checkedMods) * 100, 2)}% of projects available. ({availableMods})")
print(f"There are {round(((availableMods + availableModsWhenSelfUpdate)/checkedMods) * 100, 2)}% of projects available, when self updated. ({availableMods + availableModsWhenSelfUpdate})")
print(f"There are {checkedMods} projects.\n")


requiredCheckedMods = 0
requiredAvailableMods = 0
requiredAvailableModsWhenSelfUpdate = 0

for key in projects.keys():
    if projects[key][2] is True:
        requiredCheckedMods += 1
        if projects[key][1] is True:
            requiredAvailableMods += 1
        elif projects[key][3] is True:
            requiredAvailableModsWhenSelfUpdate += 1

print(f"There are {round((requiredAvailableMods/requiredCheckedMods) * 100, 2)}% of required projects available. ({requiredAvailableMods})")
print(f"There are {round(((requiredAvailableMods + requiredAvailableModsWhenSelfUpdate)/requiredCheckedMods) * 100, 2)}% of required projects available, when self updated. ({requiredAvailableMods + requiredAvailableModsWhenSelfUpdate})")
print(f"There are {requiredCheckedMods} required projects.\n")

print("These mods are not yet available:")
for key in projects.keys():
    if projects[key][1] is False:
        print(key, f"- https://modrinth.com/mod/{key}")
