from core import *
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
    return ""
    
def cmd_memberLeft(bot, update=False, args=[]):
    return ""

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
        reply(update, "Command Unknown")

### Testing Commands

def cmd_getbio(bot, update=False, args=[]):
    if update is False and len(args) == 1:
        return str(getBioUsernames(args[0]))
    return "Error"

def cmd_sendmessage(bot, update=False, args=[]):
    if update is False and len(args) == 1:
        return str(sendMessage(bot.bot, args[0]))
    return "Error"

def cmd_editmessage(bot, update=False, args=[]):
    if update is False and len(args) == 2:
        return str(editMessage(bot.bot, int(args[0]), args[1]))
    return "Error"

def cmd_test(bot, update=False, args=[]):
    if update is not False:
        print update
        reply(update, "OK!")
    print "OK!"
    return "OK!"


