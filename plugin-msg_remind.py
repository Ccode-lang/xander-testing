from xander_plugin import *


from datetime import datetime, timezone


def onload():
    help_menu_edit("New message reminders", "On a message of 'xander_msg_reminder' the bot will check the last message timestamp and see if is past the timestamp of the last message check.")
    log("Messages reminder plugin loaded!")

lastcheck = datetime.now(timezone.utc)
lastmessage = lastcheck

async def onmessage(message):
    global lastcheck
    global lastmessage

    if message.content == "xander_msg_reminder":
        if lastmessage > lastcheck:
            channel = discord.utils.get(message.guild.text_channels, name="reminders")
            allowed_mentions = discord.AllowedMentions(everyone = True)
            await channel.send(content = "@everyone there has been new messages!", allowed_mentions = allowed_mentions)
            lastcheck = message.created_at
        return False
    
    lastmessage = message.created_at

    return True


def onexit():
    log("Messages reminder plugin exit run.")