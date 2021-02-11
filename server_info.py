import discord


async def get_server_info(ctx: discord.Guild, embed_color, *args):

    get_all_stats = 'all' in args or len(args) == 0

    guild = ctx.guild

    info = {
        "owner": guild.owner,
        "members": len([m for m in guild.members if not m.bot]),  # Member count excluding bots
        "channels": len(guild.channels),
        "region": guild.region,
        "text-channels": len(guild.text_channels),  # Number of text channels
        "voice-channels": len(guild.voice_channels),  # Number of voice channels
    }

    server_name = guild.name
    server_icon = guild.icon_url

    embed = discord.Embed(title=f'{server_name} Server Information',
                          description=f'Description: {guild.description}',
                          color=embed_color,
                          )
    embed.set_thumbnail(url=server_icon)

    for key, value in info.items():
        if key in args or get_all_stats:
            embed.add_field(name=key.capitalize(),
                            value=value,
                            inline=True)

    await ctx.send(embed=embed)
