import discord
import asyncio
from discord.ext.commands import bot
import os
from discord.ext import commands
import platform
import time
import json
import aiohttp
import traceback
discord.__version__
'1.0.0a'
#Sup
owner = ["362672438699622403"]


bot = commands.Bot(command_prefix='.', description='Ignore this')

bot.remove_command("help")
#insert rest of code here

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name='.help', type=2))
	print ('I am online.')
	print('I am running as ' + bot.user.name+',''with the ID:' + bot.user.id+' and I am connected in '+str(len(bot.servers))+' servers.'' I am connected with '+str(len(set(bot.get_all_members())))+' members')
	
@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
    colour = discord.Colour.orange()
    )
    embed.set_author(name='Help')
    embed.add_field(name='Kick', value='Kicks member | Kick permissions', inline=False)
    embed.add_field(name='Ban', value='Bans member | Ban permissions', inline=False)
    embed.add_field(name='help', value='Shows this message', inline=False)
    embed.add_field(name='say', value='Makes the bot say something', inline=False)
    embed.add_field(name='invite', value='Invite the bot', inline=False)
    embed.add_field(name='userinfo', value='Shows info of someone', inline=False)
    embed.add_field(name='serverinfo', value='Shows info of the current server', inline=False)
    embed.add_field(name='join', value='Joins the voice channel', inline=False)
    embed.add_field(name='mute', value='mutes someone')
    embed.add_field(name='unmute', value='unmutes someone')
    embed.add_field(name='owner', value='Tells you who made this bot', inline=False)
    embed.add_field(name='avatar', value='Sends image of someones avatar')
    await bot.send_message(author, embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban1(ctx, user: discord.Member):
	author = ctx.message =''
	embed = discord.Embed(
	colour = discord.Colour.red()
	)
	embed.set_author(name='Banned', icon_url='https://cdn.discordapp.com/attachments/500013774225276949/501729509670780928/1539692018604.png')
	embed.add_field(name='{} [{}]'.format(user.name, user.id), value='has been banned', inline=False)
	await bot.say(author, embed=embed)
	await bot.ban(user)
	
@bot.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await bot.join_voice_channel(channel)

@bot.command(pass_context=True, hidden=True)
async def setavatar(ctx, url):
	if ctx.message.author.id not in owner:
		return
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r:
			data = await r.read()
	await bot.edit_profile(avatar=data)
	await bot.say("I changed my icon")
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def everyone(ctx):
	await bot.say('**Disabled**', delete_after=1)
	await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick1(ctx, user: discord.Member):
	author = ctx.message =''
	#//kick
	embed = discord.Embed(
	colour = discord.Colour.red()
	)
	embed.set_author(name='Kicked', icon_url='https://cdn.discordapp.com/attachments/500013774225276949/501729508873994261/b98tkHo.gif')
	embed.add_field(name='{} [{}]'.format(user.name, user.id), value='has been kicked', inline=False)
	await bot.say(author, embed=embed)
	await bot.kick(user)

@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)
	
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Barry's Lounge", icon_url='https://cdn.discordapp.com/attachments/500008372439875594/501782017692925954/733414.jpeg')
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '362672438699622403':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)
        
@bot.command()
async def guildcount():
  	"""Bot Guild Count"""
  	await bot.say("**I'm in {} Guilds!**".format(len(bot.servers)))

  	
@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await bot.reply("{}".format(member.avatar_url))
    await bot.delete_message(ctx.message)
    
#blankcommand
        
@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '362672438699622403':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)
        
@bot.command(pass_context = True)
async def ban(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '362672438699622403':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Banned!", description="**{0}** was banned by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
        await bot.ban(member)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
        
@bot.command(pass_context = True)
async def kick(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.kick_members or ctx.message.author.id == '362672438699622403':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Kicked!", description="**{0}** was kicked by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
        await bot.kick(member)
        await bot.delete_message(ctx.message)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
        

        
@bot.command(pass_context=True, hidden=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id not in owner:
        return
    game = game.strip()
    if game != "":
        try:
            await bot.change_presence(game=discord.Game(name=game))
        except:
            await bot.say("Failed to change game")
        else:
            await bot.say("Successfuly changed game to {}".format(game))
    else:
        await bot.send_cmd_help(ctx)

@bot.command(pass_context=True, hidden=True)
async def setname(ctx, *, name):
    if ctx.message.author.id not in owner:
        return
    name = name.strip()
    if name != "":
        try:
            await bot.edit_profile(username=name)
        except:
            await bot.say("Failed to change name")
        else:
            await bot.say("Successfuly changed name to {}".format(name))
    else:
        await bot.send_cmd_help(ctx)
        await bot.delete_message(ctx.message)

@bot.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):
        await bot.send_cmd_help(ctx)
    elif isinstance(error, commands.BadArgument):
        await bot.send_cmd_help(ctx)
    elif isinstance(error, commands.CommandInvokeError):
        print("Exception in command '{}', {}".format(ctx.command.qualified_name, error.original))
        traceback.print_tb(error.original.__traceback__)



with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

@bot.command(pass_context = True)
@commands.has_permissions(manage_roles=True, ban_members=True)
async def warn(ctx,user:discord.User,*reason:str):
  if not reason:
    await bot.say("Please provide a reason")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)
    await bot.say("**{}** has been warned.".format(user.mention))

@bot.command(pass_context = True)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      await bot.say(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
      break
  else:
    await bot.say(f"{user.name} has never been reported", delete_after=60)  

@warn.error
async def kick_error(error, ctx):
  if isinstance(error, MissingPermissions):
      text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
      await bot.send_message(ctx.message.channel, text, delete_after=10)   
    
@bot.command(pass_context=True)
async def bans(ctx):
	x = await bot.get_bans(ctx.message.server)
	x = '\n'.join([y.name for y in x])
	embed = discord.Embed(titlr = "Those in a better place", description = x, color = 0xFFFFF)
	embed.set_footer(text="Banned Users")
	await bot.say(embed=embed, delete_after=300)

@bot.command()
async def invite():
  	await bot.say("**Check your DMs.**")
  	await bot.whisper("**Add me with this link** {}".format(discord.utils.oauth_url(bot.user.id)))
  	
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)





#ctx.message.author
#nextcmd
bot.run(os.getenv('Token'))

