import os
import subprocess
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
BFCONVERT_PATH = os.getenv('BFCONVERT_PATH')

bot = commands.Bot(intents=intents, command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command()
async def convert(ctx):
    await ctx.send('Message received')
    if len(ctx.message.attachments) == 0:
        await ctx.send('No file attachments found.')
        return

    for attachment in ctx.message.attachments:
        # Download the attachment
        filename = attachment.filename
        await attachment.save(filename)
        await ctx.send(f'Downloaded {filename}')

        # Convert the file using bfconvert
        output_file = os.path.splitext(filename)[0] + '.png'
        print(f"Running bfconvert with the following arguments: [{BFCONVERT_PATH}, {filename}, {output_file}]")
        result = subprocess.run([BFCONVERT_PATH, filename, output_file], capture_output=True, text=True)
        output = f'Ran bfconvert with the following arguments: {result.args}\nbfconvert output:\n{result.stdout}'
        if result.returncode != 0:
            output += f'\nError:\n{result.stderr}'
        await ctx.send(f'```{output}```')

        # Send the output file
        if os.path.exists(output_file):
            with open(output_file, 'rb') as f:
                await ctx.send(file=discord.File(f))

            # Send output to the Discord channel
            await ctx.send(f'Converted file {filename}')

            # Delete the downloaded file
            os.remove(filename)
            await ctx.send(f'Deleted {filename}')

bot.run(DISCORD_TOKEN)
