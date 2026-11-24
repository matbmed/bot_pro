import discord
from discord.ext import commands
import random
#permissão
intents = discord.Intents.default()
intents.message_content = True

#comandos
bot = commands.Bot(command_prefix='$', intents=intents)

#login
@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

#cara ou coroa
@bot.command()
async def moeda(ctx):
    resultado = random.choice(['Cara 🪙', 'Coroa 🪙'])
    await ctx.send(f"O resultado foi: **{resultado}**")

#emoji
@bot.command()
async def emoji(ctx):
    emojis = [
        '😀', '😂', '😍', '🤔', '😎', '🥳', '😭', '🤯', 
        '🔥', '💯', '🎉', '🎮', '🚀', '⭐', '💎', '🍕', 
        '🎵', '🐱', '🐶', '🦄', '👻', '🤖', '💀', 
        '🪖', '⚜️', '🛦', '⛨', '♞', '♱', '⚔️', '🏎️', 
        '𓃮', '🍖', '🍔', '🥩', '💥'
    ]
    escolhido = random.choice(emojis)
    await ctx.send(f"Seu emoji aleatório é: **{escolhido}**")

bot.run("digite seu token:")
