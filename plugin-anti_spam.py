from xander_plugin import *
from datetime import datetime, timezone

# [times messaged, time of last message]
counter_dict = {}

def onload():
    log("Anti-spam plugin loaded!")

async def onmessage(message):
    try:
        check = datetime.now(timezone.utc) - counter_dict[message.author.id][1]
        if check.total_seconds() > 10:
            del counter_dict[message.author.id]
    except:
        pass

    try:
        counter_dict[message.author.id][0] += 1
        counter_dict[message.author.id][1]
    except KeyError:
        counter_dict[message.author.id] = [1, datetime.now(timezone.utc)]
    
    if counter_dict[message.author.id][0] > 5:
        await modlog(message.author.name + ' spammed on server "' + message.guild.name + '"', message, True)
        print(counter_dict)
        return False
    
    return True


def onexit():
    log("Anti-spam plugin exit run.")
