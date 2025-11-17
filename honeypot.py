import discord
from discord.ext import commands
import os

# Leer el token desde Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID del canal honeypot
HONEYPOT_CHANNEL_ID = 1440025458279448678

# Activar intents necesarios
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

# Crear el bot
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

    # Si alguien escribe en el honeypot -> ban inmediato
    if message.channel.id == HONEYPOT_CHANNEL_ID:
        print("⚠ Mensaje en HONEYPOT, intentando banear...")
        try:
            await message.guild.ban(message.author, reason="Entró en el honeypot")
            print(f"🚫 Usuario baneado: {message.author}")
        except Exception as e:
            print(f"❌ Error al banear: {e}")

    # Procesar otros comandos
    await bot.process_commands(message)

bot.run(BOT_TOKEN)
