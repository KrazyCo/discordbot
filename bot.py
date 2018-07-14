import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

binnum1 = [128, 64, 32, 16, 8, 4, 2, 1]

prefix = ("?")

client = discord.Client()
client = commands.Bot(command_prefix = "?")

#helpText = (
embed=discord.Embed(title="Krazy", description="These are the Krazy commands", colour = 0x1E894A)
embed.add_field(name='?info', value='See info about Krazy and the changelogs', inline=False)
embed.add_field(name='?ping', value='Pong!', inline=False)
embed.add_field(name='?serves', value='See how many serves I am in', inline=False)
embed.add_field(name='?invite', value='Get an invite for Krazy', inline=False)
embed.add_field(name='?roll', value='Rolls a dice', inline=False)
embed.add_field(name='?embed (message)', value='Embeds your message', inline=False)
embed.add_field(name='?binary (interger)', value='Turns the number you sent into 8 bit binary', inline=False)
embed.add_field(name='?link (URL) (message)', value='Puts a hyperlink in an embed', inline=False)
embed.add_field(name='If you need more help join', value='https://discord.gg/aShTH8T', inline=False)
#           )


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
**0.1.2.5:**
Added a nice version
**0.1.3:**
Added ?binary
Added ?roll
**0.1.4:**
Made ?invite look nicer
Made all embed colours look more like the logo
**0.1.5:**
Added ?link
Made ?help nicer
**0.1.6:**
Removed ?emoji
Removed ?say""")


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
        if message.content.upper().startswith(prefix + "LINK"):
            text = ("%s" % (" ".join(args[2:])))
            inputurl = (args[1])
            em = discord.Embed(title= text, url= inputurl, colour=0x1E894A)
            await client.send_message(message.channel, embed=em)
            await client.delete_message(message)
            print ("link")
        if message.content.upper().startswith(prefix + "BINARY"):
            binaryIn = (args[1])
            input1 = int(binaryIn)
            endnum = []
            if input1 >= 256:
                await client.send_message(message.channel, "Invalid input, please try again with a interger under 256")
            else:
                for i in range(8):
                    if input1 >= binnum[i]:
                        endnum.extend("1")
                        input1 = int(input1-binnum[i])
                    else:
                        endnum.extend("0")
                if input1 != 0:
                    print ("Error please try again")
                else:
                    binaryOut = endnum
            await client.send_message(message.channel, "I got " + str("".join(binaryOut)) + " from " + str(binaryIn))
            print ("binary: " + str(binaryIn))
            



        if message.content.upper().startswith(prefix + "HELP"):
            await client.send_message(message.author, embed=embed)
            dm = discord.Embed(title=":mailbox_with_mail: Check DM's", colour=0x1E894A)
            await client.send_message(message.channel, embed=dm)
            print ("help")
        if message.content.upper().startswith(prefix + "INFO"):
            em = discord.Embed(title="Info", description=infoText, colour=0x1E894A)
            await client.send_message(message.channel, embed=em)
            print ("info")


        


client.run('NDQ1NTExMTA3OTQwMTg4MTYw.DieGrg.3I8F62TOC6ufqz4SZ8NSZ95OL5k')
