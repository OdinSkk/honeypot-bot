import discord
from discord.ext import commands

HONEYPOT_CHANNEL_ID = 1440025458279448678
BOT_TOKEN = "MTQ0MDAzMDE1MzM2NjU3MzE5MA.GlUFPn.t6P8wSEPQJbCCjNZnXwwycaukjidBIcb65Hmy"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🔥 Bot conectado como {bot.user}")
    print("✔ El bot está listo y el honeypot activo")

@bot.event
async def on_message(message):
    print(f"[DEBUG] Mensaje detectado en canal {message.channel.id}: {message.content}")

    if message.author.bot:
        return

    if message.channel.id == HONEYPOT_CHANNEL_ID:
        print("⚠ Mensaje en HONEYPOT, intentando banear...")
        try:
            await message.guild.ban(message.author, reason="Entró en el honeypot")
            print(f"🚫 Usuario baneado: {message.author}")
        except Exception as e:
            print(f"❌ Error al banear: {e}")

    await bot.process_commands(message)

bot.run(BOT_TOKEN)
