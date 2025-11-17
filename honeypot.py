import discord
from discord.ext import commands
import os

HONEYPOT_CHANNEL_ID = 1440025458279448678
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

HONEYPOT_MESSAGE = (
    "⚠️ **Honeypot Channel** ⚠️\n"
    "If you talk in here, you will be banned automatically.\n"
    "Appeals will not be given."
)

@bot.event
async def on_ready():
    print(f"🔥 Bot conectado como {bot.user}")
    print("✔ El bot está listo y el honeypot activo")

    channel = bot.get_channel(HONEYPOT_CHANNEL_ID)
    if channel:
        try:
            await channel.send(HONEYPOT_MESSAGE)
            print("📌 Mensaje de honeypot enviado correctamente")
        except Exception as e:
            print(f"❌ Error enviando el mensaje del honeypot: {e}")

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
