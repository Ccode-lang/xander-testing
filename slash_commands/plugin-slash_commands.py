from xander_plugin import *
from discord import app_commands

def onload():
    log("Slash command plugin loaded!")
    
async def async_onload():
    plugins = getother("plugins")
    tree = app_commands.CommandTree(client)
    for plugin in plugins:
        try:
            plugin.register_slash(tree)
        except:
            pass
    await tree.sync()

def onexit():
    log("Slash command plugin exit run.")