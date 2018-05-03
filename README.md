# BioChain2Bot
Telegram bot for the Bio Chain 2 Group

## How to run the bot

Create a file private.py:

TOKEN="Your token"

CHATID=1234

Run in a terminal ./botserver.py
This will open a sock server on port 12345
If you want to send commands to the bot, run in another terminal ./bot.py CMD [ARG1, ARG2, ...]

## How to add commands

Just edit commands.py using the format explained in the file
Those commands are going to be executed when called by the chat or by bot.py

## Big TODO

core.py should contain all the important and difficul things
