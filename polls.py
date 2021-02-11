import discord


async def create_poll(ctx, *args, embed_color):
    true_member_count = len([m for m in ctx.guild.members if not m.bot])

    question, *options = args

    embed = discord.Embed(title="POLL",
                          description=f'{question.capitalize()}',
                          embed_color=embed_color
                          )

    for option in options:
        embed.add_field(name=f'{option.capitalize()}',
                        value='o',
                        inline=False)

    msg = await ctx.send(embed=embed)

    emoji = '\N{THUMBS UP SIGN}'
    emoji2 = '\N{THUMBS DOWN SIGN}'

    await msg.add_reaction(emoji)
    await msg.add_reaction(emoji2)





