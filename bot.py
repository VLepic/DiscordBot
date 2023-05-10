import discord
import Timer
from discord.ext import commands
import datetime


def run_discord_bot(BOTTOKEN):
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='.', intents=intents)
    global stopky
    stopky = Timer.Timer()

    @bot.event
    async def on_ready():
        print('Bot ready')
        print('-----------------------')


    async  def send_message(message, user_message, is_private):
        try:
            response = "null"
            await message.author.send(response) if is_private else await message.channel.send(response)

        except Exception as e:
            print(e)

    @bot.command()
    async def hello(ctx):
        await ctx.send('Hello')

    @bot.command()
    async def say(ctx, arg):
        await ctx.send(arg)


    @bot.command()
    async def ts(ctx):
        global stopky
        stopky.tstart()
        print(f'{datetime.datetime.now()} Uživatel {ctx.author} spustil stopky.')
        await ctx.send("Stopky spuštěny!")

    @bot.command()
    async def te(ctx):
        global stopky
        print(f'{datetime.datetime.now()} Uživatel {ctx.author} zastavil stopky.')
        await ctx.send(stopky.tend())


    @bot.command(pass_context=True)
    async def join(ctx):
        if (ctx.author.voice):
            channel = ctx.author.voice.channel
            print(f'{datetime.datetime.now()} Uživatel {ctx.author} nařídil připojit se.')
            vc = await channel.connect()
        else:
            await ctx.send("You are not in a voice channel.")


    @bot.command(pass_context=True)
    async def jointo(ctx, channel: discord.VoiceChannel):
        print(f'{datetime.datetime.now()} Uživatel {ctx.author} nařídil připojení do: {channel}.')
        vc = await channel.connect()



    @bot.command(pass_context=True)
    async def leave(ctx):
        if (ctx.guild.voice_client):
            await ctx.guild.voice_client.disconnect()
            print("Disconnected")
        else:
            await ctx.send("Not in a voice channel.")


    @bot.command(pass_context=True)
    async def abuse(ctx, member: discord.Member, targetchannel1: discord.VoiceChannel, targetchannel2: discord.VoiceChannel):
        await ctx.send(f"Abusing {member.mention}!")
        originchannel = member.voice.channel
        """Move a member to a voice channel."""
        number = 4

        print(f'{datetime.datetime.now()} Uživatel {ctx.author} proházel {member.mention}!')
        for i in range(number):
            try:
                await member.move_to(targetchannel1)

            except discord.errors.HTTPException as e:
                await ctx.send("An error occurred while attempting to move the member.")
            try:
                await member.move_to(targetchannel2)

            except discord.errors.HTTPException as e:
                await ctx.send("An error occurred while attempting to move the member.")
        await member.move_to(originchannel)

    bot.run(BOTTOKEN)
