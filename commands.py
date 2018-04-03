import core
import texts
#bot is the class Bot inside botserver
#update is the response from telegram
#args is the array with other arguments
#Dummy function:
'''
def cmd_NAME(bot, update=False, args=[]):
    #stuff
    return "" #string
'''

def cmd_newMember(bot, update=False, args=[]):
    if update is False:
        return "This command is for the Telegram Bot"
    for user in update.message.new_chat_members:
        if user.is_bot:
            continue
        texts.welcome(bot, user)
        bot.chain.add(user)
    
def cmd_memberLeft(bot, update=False, args=[]):
    if update is False:
        return "This command is for the Telegram Bot"
    user = update.message.left_chat_member
    bot.chain.remove(user)
    cmd_updatechain(bot)
    
def cmd_updatechain(bot, update=False, args=[]):
    return "" #TODO

### Ugly Commands

def cmd_error(bot, update=False, args=[]):
    if update is False or args is []:
        return "This command is for the Telegram Bot"
    else:
        print "Update: ", str(update)
        print "Error: ", str(args[0])
    
def cmd_unknown(bot, update=False, args=[]):
    if update == False:
        return "Command unknown: " + str(args[0])
    else:
        core.reply(update, "Command Unknown")

### Testing Commands

def cmd_getbio(bot, update=False, args=[]):
    if update is False and len(args) == 1:
        return str(core.getBio(args[0]))
    return "Error"

def cmd_sendmessage(bot, update=False, args=[]):
    if update is False and len(args) == 1:
        return str(core.sendMessage(bot.bot, args[0]))
    return "Error"

def cmd_editmessage(bot, update=False, args=[]):
    if update is False and len(args) == 2:
        return str(core.editMessage(bot.bot, int(args[0]), args[1]))
    return "Error"

def cmd_test(bot, update=False, args=[]):
    if update is not False:
        print update
        core.reply(update, "OK!")
    print "OK!"
    return "OK!"


