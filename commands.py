import core
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

def cmd_error(bot, update=False, args=[]):
    if update is False or args is []:
        return "This command is reserved for the telegram bot"
    else:
        print "Update: ", str(update)
        print "Error: ", str(args[0])
    
def cmd_unknown(bot, update=False, args=[]):
    if update == False:
        return "Command unknown"
    else:
        core.send_message(bot.bot, update, "Command Unknown")
        
def cmd_test(bot, update=False, args=[]):
    if update is not False:
        update.message.reply_text("OK!")
    print "OK!"
    return "OK!"
