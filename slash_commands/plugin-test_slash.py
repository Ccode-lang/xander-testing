from xander_plugin import *
from discord import app_commands


def onload():
    log("Slash test plugin loaded!")

def register_slash(tree):
    tree.add_command(app_commands.Command(name="test", callback=test, description="Just testing stuff."), override = True)

async def test(ctx):
    await ctx.response.send_message("Hello!")

def onexit():
    log("Slash test plugin exit run.")