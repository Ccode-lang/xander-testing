from xander_plugin import *


def onload():
    log("Reaction test plugin loaded!")

async def onreactionadd(reaction, user):
    print(reaction.emoji)
    return True
async def onreactionremove(reaction, user):
    print(reaction.emoji)
    return True




def onexit():
    log("Reaction test plugin exit run.")
