import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

binnum1 = [128, 64, 32, 16]
binnum2 = [8, 4, 2, 1]

prefix = ("?")

client = discord.Client()
client = commands.Bot(command_prefix = "?")

helpText = ("""
**Helpful Commands**
**""" + prefix + """help** - This command
**""" + prefix + """info** - See info about the Bot and Changelogs
**""" + prefix + """ping** - Pong!
**""" + prefix + """servers** - See how many servers I am running!
**""" + prefix + """invite** - Get a link to invite KrazyBot to your own server
**""" + prefix + """roll** - Rolls a dice
**""" + prefix + """say (message)** - Says what you say
**""" + prefix + """emoji (emoji name)** sends whatever emoji you say
**""" + prefix + """embed (message)** - embeds your message
**""" + prefix + """binary (number)** - turns the number you said into binary

**Fun Commands**
**""" + prefix + """cookie** - Sends a cookie
**""" + prefix + """watermelon** - Sends a watermelon
**""" + prefix + """eggplant** - Sends a eggplant
**""" + prefix + """pig** - Sends a pig

**If you need more help, join https://discord.gg/aShTH8T**
""")

version = ("0.1.3")

infoText = ("""
**Made by @KrazyCo#3341
Under heavy development

Changelogs:**

**0.1.0:**
Added ?embed
Changed colour of embeds
Made ?help look nicer
Added ?info
**0.1.1:**
Fixed ?embed - didn't like spaces
**0.1.2:**
Added ?invite
**0.1.2.5**
Added a nice version
**0.1.3:**
Added ?binary
Added ?roll
**0.1.4:**
Made ?invite look nicer
Made all embed colours look more like the logo


**Version """ + version + "**")


invText = ("An invite for KrazyBot - https://bit.ly/krazybot")
@client.event
async def on_ready():
    print ("Bot online")
    await client.change_presence(game=discord.Game(name=prefix + "help | %s Servers!" % len(client.servers)))

@client.event
async def on_message(message):
        userID = message.author.id
        args = message.content.split(" ")

    
        if message.content.upper() == prefix + "COOKIE":
            await client.send_message(message.channel, ":cookie:")
            await client.delete_message(message)
            print ("cookie")
        if message.content.upper() == prefix + "WATERMELON":
            await client.send_message(message.channel, ":watermelon:")
            await client.delete_message(message)
            print ("watermelon")
        if message.content.upper() == prefix + "EGGPLANT":
            await client.send_message(message.channel, ":eggplant:")
            await client.delete_message(message)
            print ("eggplant")
        if message.content.upper() == prefix + "PIG":
            await client.send_message(message.channel, ":pig:")
            await client.delete_message(message)
            print ("pig")
        
        if message.content.upper().startswith(prefix + "PING"):
            await client.send_message(message.channel, "<@%s> Pong!" % (userID))
            print ("Ping")
        if message.content.upper() == prefix + "ROLL":
            await client.send_message(message.channel, "I rolled a "+ str(random.randint(1,6)))
            print ("roll")
        if message.content.upper().startswith(prefix + "SAY"):
            if message.content.upper().startswith("?SAY ?SAY"):
                await client.send_message(message.channel, "Thats not allowed!")
                print ("spammers")
            else:
                await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                await client.delete_message(message)
                print ("say: %s" % (" ".join(args[1:])))
        if message.content.upper().startswith(prefix + "EMOJI"):
            await client.delete_message(message)
            await client.send_message(message.channel, ":%s:" % ("".join(args[1])))
            print ("emoji: %s" % ("".join(args[1:])))
        if message.content.upper().startswith(prefix + "SERVERS"):
            await client.send_message(message.channel, "I am serving %s servers!" % len(client.servers))
            await client.change_presence(game=discord.Game(name=prefix + "help | %s Servers!" % len(client.servers)))
            print ("servers: %s" % len(client.servers))
        if message.content.upper().startswith(prefix + "EMBED"):
            text = ("%s" % (" ".join(args[1:])))
            await client.delete_message(message)
            emb = discord.Embed(title=text, colour=0x1E894A)
            await client.send_message(message.channel, embed=emb)
            print ("embed: " + text)
        if message.content.upper().startswith(prefix + "INVITE"):
            em = discord.Embed(title= ":link: Click to add to your server! :link:", url= "https://discordapp.com/api/oauth2/authorize?client_id=445511107940188160&permissions=2146958583&scope=bot", colour=0x1E894A)
            await client.send_message(message.channel, embed=em)
            print ("invite")
        if message.content.upper().startswith(prefix + "BINARY"):
            input1 = int(args[1])
            input2 = input1
            endnum = []
            if input1 >= 256:
                await client.send_message(message.channel, "Invalid input, please try again with a number under 256")
            else:
                for i in range(4):
                    if input1 >= binnum1[i]:
                        endnum.extend("1")
                        input1 = int(input1-binnum1[i])
                    else:
                        endnum.extend("0")
                for i in range(4):
                    if input1 >= binnum2[i]:
                        endnum.extend("1")
                        input1 = int(input1-binnum2[i])
                    else:
                        endnum.extend("0")
                if input1 != 0:
                    print ("Error please try again")
                else:
                    await client.send_message(message.channel, "I got " + str("".join(endnum)) + " from " + str(input2))
                print ("binary: " + str(input2))
            



        if message.content.upper().startswith(prefix + "HELP"):
            em = discord.Embed(title="Help", description=helpText, colour=0x1E894A)
            await client.send_message(message.channel, embed=em)
            print ("help")
        if message.content.upper().startswith(prefix + "INFO"):
            em = discord.Embed(title="Info", description=infoText, colour=0x1E894A)
            await client.send_message(message.channel, embed=em)
            print ("info")


        


client.run('NDQ1NTExMTA3OTQwMTg4MTYw.DieGrg.3I8F62TOC6ufqz4SZ8NSZ95OL5k')
