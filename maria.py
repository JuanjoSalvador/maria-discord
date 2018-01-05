import discord
import settings

client = discord.Client()

@client.event
async def on_member_join(message):
    msg = 'Bienvenido, {0.author.mention}!'.format(message)
    await client.send_message(message.channel, msg, tts=True)


@client.event
async def on_ready():
    print("María online.")


client.run(settings.bot_token)