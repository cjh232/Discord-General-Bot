import discord
import secrets
import weather


client = discord.Client()


async def handle_commands(channel):

    embed = discord.Embed(title="Commands",
                          description="Some useful commands and formatting information",
                          color=discord.Color.purple())
    embed.add_field(name="$weather <city name> - <space separated tags>",
                    value="Gets weather data for the given city.",
                    inline=False)
    embed.add_field(name="$tags", value="Returns list of tags.", inline=True)
    embed.add_field(name="$cmd",  value="Returns list of commands.", inline=True)

    await channel.send(embed=embed)


async def bad_formatting(message):

    msg = '__**Error: Bad Formatting**__\n'
    msg += 'Type "$weather [city name] - [space separated tags]" to get weather results.\n'
    msg += 'Type "$tags" to see available tags.'

    await message.channel.send(msg)


async def handle_weather_request(message):

    content = message.content.split('-')

    op = content[0].rstrip().split(' ')
    tags = content[1].lstrip().split(' ') if len(content) > 1 else []

    _, *city = op

    location = ' '.join(city)

    res = weather.get_weather(location, tags)

    embed_description = res["desc"] if "desc" in res.keys() else ""

    embed = discord.Embed(title=res["city"], description=embed_description)

    for key, value in res.items():
        if key != "desc" and key != "city":
            embed.add_field(name=key, value=value, inline=False)

    await message.channel.send(embed=embed)


async def handle_tags(channel):

    tags_dict = {
        "- a": "All",
        "- p": "Pressure",
        "- t": "Temperature",
        "- h": "Humidity",
        "- f": "Feels like",
        "- w": "Wind speed"
    }

    embed = discord.Embed(title="Tags", description="List of tags to parse weather data.")

    for key, value in tags_dict.items():
        embed.add_field(name=value, value=key, inline=True)

    await channel.send(embed=embed)


@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$weather'):
        await handle_weather_request(message)
    
    if message.content.startswith('$cmd'):
        await handle_commands(message.channel)
    
    if message.content.startswith('$tags'):
        await handle_tags(message.channel)
        

token = secrets.TOKEN

client.run(token)
