import discord
from stockx import search
from config import TOKEN, CHANNEL_ID


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != CHANNEL_ID:
        return

    if message.content.split(' ')[0] == '!stockx':
        query = message.content.replace('!stockx ', '')

        item = search(query)

        embed = discord.Embed(
            title=item['title'],
            url='https://stockx.com/en-gb/' + item['urlKey']
        )
        embed.set_thumbnail(
            url=item['media']['imageUrl']
        )
        embed.add_field(
            name='Colourway',
            value=item['colorway']
        )
        embed.add_field(
            name='Style ID',
            value=item['styleId']
        )
        embed.add_field(
            name='Last Sale',
            value=item['market']['lastSale']
        )
        await message.channel.send(embed=embed)

client.run(TOKEN)

    