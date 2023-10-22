from xander_plugin import *


def onload():
    log("Voice plugin loaded!")

async def onmessage(message):
    if message.content == "!join":
        await join_vc(message.author.voice.channel)
        return False
    elif message.content == "!leave":
        await leave_vc()
    return True


def onexit():
    log("Voice plugin exit run.")
