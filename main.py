import discord
from discord.ext import commands
import secrets
import weather
import polls
import server_info

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)
embed_color = discord.Color.dark_gold()

# Commands


@bot.command(name="weather")
async def _weather(ctx, *args):
    await weather.handle_weather_request(ctx, *args, embed_color=embed_color)


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

    embed = discord.Embed(title="Tags",
                          description="List of tags to parse weather data.",
                          color=embed_color
                          )

    for key, value in tags_dict.items():
        embed.add_field(name=value, value=key, inline=True)

    await ctx.send(embed=embed)


@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands",
                          url="https://github.com/cjh232/Discord-Weather-Bot",
                          description="Some useful commands and formatting information",
                          color=embed_color)
    embed.add_field(name="$weather <city name> - <space separated tags>",
                    value="Gets weather data for the given city.",
                    inline=False)
    embed.add_field(name="$tags", value="Returns list of tags.", inline=True)
    embed.add_field(name="$commands", value="Returns list of commands.", inline=True)

    await ctx.send(embed=embed)


@bot.command()
async def math(ctx, arg1: int, op, arg2: int):
    valid_ops = ['/', '+', '-', '*']

    if op not in valid_ops:
        await ctx.send('Invalid operation.')
        return

    print(f'{arg1}{op}{arg2}')

    loc = {}
    exec(f'res = {arg1}{op}{arg2}', globals(), loc)

    await ctx.send(loc["res"])


@bot.command()
async def poll(ctx, *args):
    await polls.create_poll(ctx, *args, embed_color=embed_color)


@bot.command()
async def stfu(ctx, *, name):
    await ctx.send(f'Shut the FUCK up, {name}')


@bot.command()
async def server(ctx, *args):
    await server_info.get_server_info(ctx, embed_color=embed_color, *args)


# Events


bot.run(secrets.token)
