import discord
import requests
import json
from dotenv import load_dotenv
load_dotenv()
import os


client = discord.Client()

def get_request_handle(commandRequested):
  response = requests.get("https://bs3n68p70a.execute-api.eu-west-1.amazonaws.com/Live/status",
      params={'command':commandRequested},
      headers={'x-api-key':os.getenv("API_KEY")}
  )
  if response.status_code == requests.codes.ok: 
    return(response.text)
  else: 
    return("Error in bot!")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # So we dont loop on our own responses
  if message.author == client.user:
    return
  
  msg = message.content.lower()
  print (f"msg is {msg}")

  if not msg.startswith("$valheim"):
    print("doesnt start with keyword")
    return  
  if len(msg.split()) > 2: 
    print("only use one keyword please")
    await message.channel.send("Only use one keyword please")
  
  if 'status' in msg:
    quote = get_request_handle('status')
    await message.channel.send(quote)

  if 'commands' in msg:
    quote = get_request_handle('commandlist')
    await message.channel.send(quote)

  if 'off' in msg:
    quote = get_request_handle('commandlist')
    await message.channel.send(quote)


client.run(os.getenv("DISCORD_KEY"))