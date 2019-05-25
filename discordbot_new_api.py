#!/usr/bin/python3.6
import logging
import discord
from discord.ext import commands
import random
import subprocess
import os
import asyncio
import datetime
import time
import re   #for owoify
import requests
from imgurpython import ImgurClient

logging.basicConfig(level=logging.INFO)

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

client = discord.Client()

#mystuff

schedule_arr=['!monday','!tuesday','!wednesday','!thursday','!friday','!saturday','!sunday']#,'!tbs']

active_task = 0
nyaa_fail_counter = 0
def toggle_task():
  global active_task
  active_task = not(active_task)

def add_nyaa_fail():
  global nyaa_fail_counter
  nyaa_fail_counter += 1

def reset_nyaa_fail():
  global nyaa_fail_counter
  nyaa_fail_counter = 0


def getcurrday():
  wd = datetime.datetime.today().weekday()
  days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  return(days[wd])


def new_anime():
 fh = open("/mnt/Niceseagate/Ph/Anime/newanime", 'r+')
 for line in fh:
   pass
 last1 = line
 fh.seek(fh.tell() - len(last1))
 fh.truncate()
 fh.close()
 fh = open("/mnt/Niceseagate/Ph/Anime/newanime", 'r+')
 for line in fh:
   pass
 last2 = line
 fh.seek(fh.tell() - len(last2))
 fh.truncate()
 fh.close()
 fh = open("/mnt/Niceseagate/Ph/Anime/newanime", 'r+')
 for line in fh:
   pass
 last3 = line
 fh.seek(fh.tell() - len(last3))
 fh.truncate()
 fh.close()
 fh = open("/mnt/Niceseagate/Ph/Anime/newanime", 'r+')
 for line in fh:
   pass
 last4 = line
 fh.seek(fh.tell() - len(last4))
 fh.truncate()
 fh.close()
 fh = open("/mnt/Niceseagate/Ph/Anime/newanime", 'r+')
 for line in fh:
   pass
 last5 = line
 fh.write(last4)
 fh.write(last3)
 fh.write(last2)
 fh.write(last1)
 fh.close()
 msg = last5 + '\n' + last4 + '\n' + last3 + '\n' + last2 + '\n' + last1
 return(msg)


def moveanime():
 CMD = 'moveanime.sh > tmp'
 fp = subprocess.check_output(CMD, shell=True)
 list = []
 out=''
 f = open("tmp", "r")
 for line in f:
     list.append(line)
 for x in list:
     out = out + x
 f.close()
 os.remove('tmp')
 return(out)


def owoify(v):
  v = re.sub('[rl]','w',v)  #replace r or l for w
  v = re.sub('[RL]','W',v)
  v = re.sub('(n)([aeiou])','ny\g<2>',v)    #replace n followed by a or e... for ny(a or e...)
  v = re.sub('(N)([aeiou])','Ny\g<2>',v)
  v = re.sub('(n)([AEIOU])','ny\g<2>',v)
  v = re.sub('(N)([AEIOU])','NY\g<2>',v)
  v = v.replace('ove','uv')
  v = v.replace('cwizzy','cwizzy chan')
  v = v.replace('siyaah','sayaka chan')
  v = v.replace('buwwet','buwwet chan')
  return(v)

def randomthigh()
  client_id = '6d6801a1d5fb69d'
  client_secret = '74d6a3f5f56ae62e73ce05d7855effe2548ea89d'
  access_token = 'e49a47fc68fa09d88e2e53e901773e13c46946dc'
  refresh_token = '1d1d7ed324b3e4581b61b84562389969980d5c1f'
  
  client = ImgurClient(client_id, client_secret, access_token, refresh_token) #required to access imgur Api

  Links = []
  items = client.get_album_images('y73csJo')

  for item in items:
    Links.append(item.link)

return(random.choice(Links))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    message.content = message.content.casefold()
    if message.author == client.user:
        return

    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    elif message.content.startswith('!owner'):
        msg = '{0.author.guild.owner.mention} is the owner'.format(message)
        await message.channel.send(msg)

    elif message.content.startswith('!clear'):
        msg = message.content[len('!clear '):].strip()
        count = int(msg)
        if message.author == message.author.guild.owner:
          deleted = await message.channel.purge(limit=count)
          cleared = await message.channel.send('Deleted {} message(s)'.format(len(deleted)))
          await asyncio.sleep(3)
          await cleared.delete()
        else:
          def same_user(m):
            return m.author == message.author
          deleted = await client.purge_from(message.channel, limit=count, check=same_user)
          cleared = await message.channel.send('Deleted {} message(s)'.format(len(deleted)))
          await asyncio.sleep(3)
          await cleared.delete()

    elif message.content.startswith('!newanime'):
        msg = new_anime().format(message)
        msg='```\n'+msg+'```'
        await message.channel.send(msg)

    elif message.content.startswith('!moveanime'):
        msg = moveanime().format(message)
        await message.channel.send(msg)

    elif message.content.startswith('!resize'):
        CMD = 'aaresize.sh'
        fp = subprocess.check_output(CMD, shell=True)
        await message.channel.send('probs resized idk')

    elif message.content.startswith('!currweather'):
        location = message.content[len('!currweather '):].strip()
        CMD = '/home/nande/discordbot/currweather.py ' + '\'' + location + '\'' ' > tmp'
        fp = subprocess.check_output(CMD, shell=True)
        f = open("tmp","r")
        msg = ''
        for line in f:
          msg = msg + line
        f.close()
        os.remove('tmp')
        msg='```\n'+msg+'```'
        await message.channel.send(msg)

    elif message.content.startswith('!forecast'):
        location = message.content[len('!forecast '):].strip()
        CMD = '/home/nande/discordbot/forecast3h.py ' + '\'' + location + '\'' ' > tmp'
        fp = subprocess.check_output(CMD, shell=True)
        f = open("tmp","r")
        msg = ''
        for line in f:
          msg = msg + line
        f.close()
        os.remove('tmp')
        msg='```\n'+msg+'```'
        await message.channel.send(msg)


    elif message.content.startswith('!nyaa') and (message.author == message.author.guild.owner):
      if active_task==1:
        add_nyaa_fail()
      else:
        toggle_task()
        await message.channel.trigger_typing()
        search1 = message.content[len('!nyaa '):].strip()
        search_term= search1.replace(" ","&")
        CMD = '/home/nande/discordbot/searchrss.py ' + '\'' +search_term + '\'' ' > tmp'
        fp = subprocess.check_output(CMD, shell=True)
        f = open("tmp","r")
        n=0
        z=1
        name=[]
        link=[]
        for line in f:
          if n==0:
            name.append(line)
            n=1
          else:
            link.append(line)
            n=0
            z+=1
        f.close()
        os.remove('tmp')
        x=0
        msg = ''
        while x<len(name)-1:
          if x==15:
             break
          msg = msg + repr(x+1) + ':  ' +  name[x]
          x+=1

        if not msg:
          await message.channel.send('Couldn\'t find anything')
        else:
          msg='Type the number to download:\n```\n'+msg+'```'
          available_to_dl = await message.channel.send(msg)
          time1 = int(time.time())
          nyaa_auth = message.author
          def check(m):
              return m.author == nyaa_auth
          message = await client.wait_for('message',check=check)
          while message.content.isdigit()==0:
            if message.content=='q':
              z=1
              break
            elif (time1-int(time.time())>20):
              z=1
              break
            message = await client.wait_for('message',check=check)
          if z!=1:
            select = int(message.content)-1
            CMD = 'deluge-console -c /var/lib/deluge/.config/deluge/ add ' + link[select]
            CMD = CMD.strip('\n')
            subprocess.call(CMD, shell=True)
            await message.channel.send('Downloading\n{}'.format(name[select]))
          else:
            await message.channel.send('k')
        if nyaa_fail_counter!=0:
          await message.channel.send('{} failed, me slow...'.format(nyaa_fail_counter))
        await available_to_dl.delete()
        toggle_task()
        reset_nyaa_fail()

    elif message.content.startswith('!makeschedule'):
       if message.author == message.author.guild.owner:
         CMD = '/home/nande/discordbot/hschedule.py > /mnt/Niceseagate/Ph/Anime/schedule.txt'
         subprocess.call(CMD, shell=True)
         await message.channel.send('New Schedule saved')
       else:
         await message.channel.send('No u')

    elif message.content.startswith('!today'):
       f=open('/mnt/Niceseagate/Ph/Anime/schedule.txt','r')
       msg = ''
       x=0
       for line in f:
         if x==1:
           if '|' in line:
             break
           else:
             msg = msg + line
         if getcurrday() in line:
           msg = msg + line[line.find('|')+1:]
           x=1
       if not msg:
         await message.channel.send('Nothing on {}'.format(getcurrday()))
       else:
         msg='```\n'+msg+'```'
         await message.channel.send(msg)

    elif message.content in schedule_arr:
       day = message.content[1:].strip()
       #if day == 'tbs':
        # day = 'to be scheduled'
       f=open('/mnt/Niceseagate/Ph/Anime/schedule.txt','r')
       msg = ''
       x=0
       for line in f:
         if x==1:
           if '|' in line:
             break
           else:
             msg = msg + line
         if day.capitalize() in line:
           msg = msg + line[line.find('|')+1:]
           x=1
       if not msg:
          await message.channel.send('error')
       else:
         msg='```\n'+msg+'```'
         await message.channel.send(msg)

    elif message.content.startswith('!schedule'):
      f=open('/mnt/Niceseagate/Ph/Anime/schedule.txt','r')
      z=0
      x=0
      msg=['','','','','','','']#,'']
      for day in schedule_arr:
        day = day[1:].strip()
        #if day == 'tbs':
        #  day = 'to be scheduled'
        for line in f:
         if x==1:
           if '|' in line:
             msg[z+1] = msg[z+1] + line[line.find('|')+1:]
             break
           else:
             msg[z] = msg[z] + line
         if day.capitalize() in line:
           msg[z] = msg[z] + line[line.find('|')+1:]
           x=1
        z+=1
      for m in msg:
        if not m:
          await message.channel.send('error')
          await asyncio.sleep(1)
        else:
         m='```\n'+m+'```'
         await message.channel.send(m)
         await asyncio.sleep(1)


    elif message.content.startswith('!deleteme'):
        await message.delete()

    elif message.content.startswith('!owo'):
        msg = owoify(message.content[4:].strip())
        await message.delete()
        await message.channel.send(msg)
        
    elif message.content.startswith('!thighs'):
        msg = randomthigh()
        await message.delete()
        await message.channel.send(msg)

    elif message.content.startswith('!'):
        msg = await message.channel.send(message.content[1:].strip()+' urself')
        await asyncio.sleep(3)
        await msg.delete()

    '''else:
        await message.channel.send(content=owoify(message.content)) #cant edit other peoples messages, tragic'''

    '''elif message.content.startswith('!quit'):
        discord.Client().close()'''

    '''if message.content.startswith('!siyaahpls'):
      if message.author == message.author.guild.owner:
        await client.replace_roles('186084839051493376','gib time'.id)

    if message.content.startswith('!siyaahk'):
      if message.author == message.author.guild.owner:
        await client.replace_roles('186084839051493376','pleb'.id)
    '''



'''@client.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message:\n{1.content}'
    await client.send_message(after.channel, fmt.format(after, before))

@client.event
async def on_message_delete(message):
    fmt = '{0.author.name} has deleted the message:\n{0.content}'
    await message.channel.send(fmt.format(message))
'''
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

'''@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)
'''
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))
'''
@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))
'''
client.run('NDM1NDUxMjQyOTQwOTg5NDUw.Dd0aoA.3mB8VKYMJpYetLZzWJsXHNLh6G4')
