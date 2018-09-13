import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from datetime import date
import calendar
my_date = date.today()
day=calendar.day_name[my_date.weekday()]



Client = discord.Client()
client = commands.Bot (command_prefix = "!" )

@client.event
async def on_ready():
    print("Bot is ready!")
    
@client.event
async def on_message(message):
    if message.content == "When is practice" or message.content=="When is practice?" or message.content=="practice" or message.content=="practice schedule" or message.content=="when is practice"or message.content=="when is practice?":
        await client.send_message(message.channel,"Practice is everyday from 3 to 4:30. On Tuesdays it ends at 4. Wednesdays are meet days. Sometimes there is practice on weekends.")
    if message.content == "cookie":
        await client.send_message(message.channel,":cookie:")
    if message.content == "Is there practice today?":
       if day =="Monday":
            await client.send_message(message.channel,"Its Monday my dude, yes!")
       if day == "Saturday":
            await client.send_message(message.channel,"There is a possibility let me check on that")
       if day == "Sunday":
            await client.send_message(message.channel,"No")
       if day == "Sunday":
            await client.send_message(message.channel,"No")
       if day == "Wednesday":
            await client.send_message(message.channel,"There is a meet today!") 
       else:
            await client.send_message(message.channel,"Yes!")
       



client.run("NDg4ODMyMjA2MDI2ODMzOTIw.Dnh9hA.p6A3P8HdL47_LDRkJylyvib4PXI")
