ScnTron Discord Bot

ScnTron Discord Bot is a Python program that allows users to convert .scn files to other image formats, such as .tif or .jpg, and extract metadata from .scn files directly from a Discord channel.

The bot is built using the Discord.py library and runs as a Python script.
Installation and Setup

To use this bot, you need to have Python 3.x installed on your system, along with the Discord.py and Dotenv libraries.

    Clone or download this repository to your local machine.

    Install the required Python libraries by running:

pip install -r requirements.txt

Set up a new Discord bot and obtain its token. You can follow the steps outlined in this tutorial to set up a new bot.

Create a new file named ".env" in the same directory as the Python script and add the following lines:

makefile

DISCORD_TOKEN=<your Discord bot token>
BFCONVERT_PATH=<path to the ScnTron bfconvert utility>

Replace <your Discord bot token> with the token for your Discord bot, and <path to the ScnTron bfconvert utility> with the file path to the ScnTron bfconvert utility on your system.

Run the Python script to start the bot:

    python scntron_bot.py

Usage

To use the ScnTron Discord Bot, simply invite it to your Discord server and enter the command "!convert" in any channel. This will prompt the bot to download any attached .scn files, convert them to the specified image format, and send the output back to the channel.

You can also use the command "!metadata" to extract metadata from .scn files and "!analyze" to analyze .scn files for various properties.
Examples

Here are a few examples of how to use the ScnTron Discord Bot:

    To convert a .scn file named "example.scn" to a .tif file, attach the .scn file to a message in any channel and enter the command "!convert tif".
    To extract metadata from a .scn file named "example.scn", attach the .scn file to a message in any channel and enter the command "!metadata".
    To analyze a .scn file named "example.scn" for particle tracking, attach the .scn file to a message in any channel and enter the command "!analyze".