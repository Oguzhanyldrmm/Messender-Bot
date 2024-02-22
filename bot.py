import discord

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True
intents.dm_messages = True

client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print(f'{client.user} logged.')


@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = await client.fetch_user(payload.user_id)


    if user == client.user:
        return

    if str(payload.emoji) == '✅':
        await user.send(message.content)



client.run('MTIwOTQ2OTkzMDg1NzE3NzE2OA.Gzq0a4.dv6SALXX-Mr1In2L6EeTuLMBvzyl9dlOXxDpzY')

