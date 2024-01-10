from xander_plugin import *


def onload():
    log("Event create ping plugin loaded!")

async def onscheduledeventcreate(event):
    channel = discord.utils.get(
        event.guild.text_channels, name="announcement")
    await channel.send(f"@everyone new event named \"{event.name}\" was created!")
    



def onexit():
    log("Event create ping plugin exit run.")
