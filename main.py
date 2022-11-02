from typing import (Coroutine, Literal , Union)
from keep_alive import keep_alive
import discord
import random
import os
from discord.ext import commands
from discord import DMChannel
import string

client = commands.Bot(command_prefix = os.getenv('PREFIX')) 
client.remove_command('help')

url = "https://discord.gift/"
text = 'Your Unlocked Nitro Code=>'

nitroEmbed=discord.Embed(title="Nitro Code Is Ready", url="https://dsc.gg/sizar-team", description=f"Hello brother, I have generated the Nitro Gift link for you 🙂 , please check your DM to see your Nitro link, use the opposite command to generate it again: **{os.getenv('PREFIX')}gen**", color=discord.Color.blue())
nitroEmbed.set_footer(text="Created By Mr.SIN RE#1528")

#command Nitro ganerator
@client.command()
async def gen(ctx) -> Union[Coroutine , Literal[None]]:
  if ctx.message.channel.id == (place_channel_id) or ctx.message.channel.id == (place_channel_id): #if you have some channel paste this code <or ctx.message.channel.id == (place-channel-id)> and enjoy 🙂
    user = await client.fetch_user(f"{ctx.author.id}")
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    number = list(string.digits)
    chars = lower + upper + number
    code = "".join(random.choices(chars, k=16))
    await ctx.send(embed= nitroEmbed)
    await DMChannel.send(user,fr"{text}{url}{code}")       

#command avatar 
@client.command()
async def avatar(ctx, member : discord.Member=None) -> Union[Coroutine , Literal[None]]:
    if not member:
        member = ctx.author
    av_emb = discord.Embed(
        title = "Avatar Link 🔗",
        url = member.avatar_url,
        colour =discord.Color.random()
    )
    av_emb.set_author(
        name=f"{member}",
        icon_url=member.avatar_url
    )
    av_emb.set_footer(
        text=f"Requested by {ctx.author}",
        icon_url=ctx.author.avatar_url
    )
    av_emb.set_image(url=member.avatar_url)
    await ctx.send(embed=av_emb)

#command help
helpEmbed=discord.Embed(title="Nitro Bot Help Command", url="https://dsc.gg/sizar-team", description="this is bot help embed, and you can see all bot commands.", color=discord.Color.random())
helpEmbed.set_footer(text="Created By Mr.SIN RE#1528 :)",icon_url="https://media.discordapp.net/attachments/880347850666545182/915858409738350602/image0-1_1.gif")
helpEmbed.add_field(name=f"**{os.getenv('PREFIX')}gen**" , value="generating a nitro code" ,inline=False)
helpEmbed.add_field(name=f"**{os.getenv('PREFIX')}avatar**", value="send target user avatar", inline=False)
@client.command()
async def help(ctx) -> Union[Coroutine , Literal[None]]:
  """all commands of bot"""
  await ctx.send(embed = helpEmbed)


keep_alive()       
client.run(os.getenv('TOKEN'))
