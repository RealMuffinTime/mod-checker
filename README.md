# mod-checker
Checks if and how much projects are available for a specific Minecraft version on Modrinth.  
Also downloads the needed version if available.

It is helpful if you are running a server or client with projects from modrinth.
It makes an easier desicion to upgrade to a new Minecraft version if your highly appreciated projects are available for that version.

You can set up multiple lists, and decide on run which to check.
Each list contains projects ids (mods/resourcepacks/datapacks) which have some varaibles saved to them. 
 * `project-id` specify what the project id is, this can be taken from the url on a modrinth project page.
 * `type` specify in which type you are interested for this list (mod/pack/...).
 * `available` is a internal vcariable you dont need to set.
 * `required` whether this mod is a dealbreaker to upgrade to the next version.
 * `selfUpdate` if you can update the project to the new version yourself, and don't need to rely on modrinth release.
