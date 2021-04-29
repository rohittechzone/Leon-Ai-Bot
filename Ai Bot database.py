from firebase import firebase
from googlesearch import search
import discord
import wikipedia
import pyjokes
import time

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
   if message.author == client.user:
        return
   if message.content.startswith('leon, '):
     word = message.content.replace('leon, ', '')
     word = word.lower()
     try:
         if word.startswith("search"):
             try:
                 await message.channel.send(wikipedia.summary(word, sentences=2))
             except:
                 await message.channel.send(search(word.replace('search',''))[0])
         elif 'joke' in word:
             await message.channel.send(pyjokes.get_joke())
         elif 'animate-angry' in word:
             msg = await message.channel.send(':rage:')
             for i in range(50):
                 time.sleep(0.1)
                 await msg.edit(content=":angry:")
                 time.sleep(0.1)
                 await msg.edit(content=":rage:")
         elif 'animate-lol' in word:
             msg = await message.channel.send(':joy:')
             for i in range(50):
                 time.sleep(0.1)
                 await msg.edit(content=":rofl:")
                 time.sleep(0.1)
                 await msg.edit(content=":joy:")
         elif 'animate-sweat_smilie' in word:
             msg = await message.channel.send(':sweat_smile:')
             for i in range(50):
                 time.sleep(0.1)
                 await msg.edit(content=":sweat:")
                 time.sleep(0.1)
                 await msg.edit(content=":sweat_smile:")        
         else:        
             database = firebase.FirebaseApplication('https://ai-bot-database-default-rtdb.firebaseio.com/', None)
             result = database.get('/data/'+word+'/answer/', '')
             await message.channel.send(result)
     except:
         try:
            await message.channel.send("Sorry I dont understand you")
            try:
                 await message.channel.send("Here is what i found : ")
                 await message.channel.send(wikipedia.summary(word, sentences=2))
            except:
                 await message.channel.send("Here is what i found : ")
                 await message.channel.send(search(word.replace('search',''))[0])
         except:
             await message.channel.send("Sorry I dont understand you")
client.run('ODExOTQ4NzU1Mjc1MzUwMDM2.YC5oNA.FqbLoiLRX4dCajl9cL88M99wxNw')
