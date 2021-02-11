import discord
from discord.ext import commands
import secrets
import weather

bot = commands.Bot(command_prefix='$')


@bot.command(name="weather")
async def _weather(ctx, *args):
    city_params = []
    tags_list = []
    bfr_tags = True

    for arg in args:
        if arg == '-':
            bfr_tags = False
            continue

        if bfr_tags:
            city_params.append(arg)
        else:
            tags_list.append(arg)

    city = ' '.join(city_params)

    res = weather.get_weather(city_name=city, tags=tags_list)

    embed_description = res["desc"] if "desc" in res.keys() else ""

    embed = discord.Embed(title=res["city"].title(),
                          description=embed_description,
                          color=discord.Color.purple())

    for key, value in res.items():
        if key != "desc" and key != "city":
            embed.add_field(name=key, value=value, inline=False)

    embed.set_footer(text="Weather data supplied by OpenWeather® ")

    await ctx.send(embed=embed)


@bot.command()
async def tags(ctx):
    tags_dict = {
        "- a": "All",
        "- p": "Pressure",
        "- t": "Temperature",
        "- h": "Humidity",
        "- f": "Feels like",
        "- w": "Wind speed",
        "- d": "Description"
    }

    embed = discord.Embed(title="Tags", description="List of tags to parse weather data.")

    for key, value in tags_dict.items():
        embed.add_field(name=value, value=key, inline=True)

    await ctx.send(embed=embed)


@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands",
                          url="https://github.com/cjh232/Discord-Weather-Bot",
                          description="Some useful commands and formatting information",
                          color=discord.Color.purple())
    embed.add_field(name="$weather <city name> - <space separated tags>",
                    value="Gets weather data for the given city.",
                    inline=False)
    embed.add_field(name="$tags", value="Returns list of tags.", inline=True)
    embed.add_field(name="$commands", value="Returns list of commands.", inline=True)

    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run(secrets.token)
