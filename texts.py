import core
###bot is the Bot class in bot.py

def welcome(bot, user):
    last = bot.chain.getLast()
    core.sendMessage(bot.bot, "Welcome! Please add @" + last + " in your bio!")
    
