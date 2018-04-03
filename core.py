from private import *
import requests
import re

### Messagging functions ###

def reply(update, text):
    return update.message.reply_text(text, parse_mode='Markdown')

def sendMessage(bot, text):
    return bot.sendMessage(
        chat_id=CHATID,
        text=text,
        parse_mode='markdown'
    )

def editMessage(bot, messageID, text):
    return bot.editMessageText(
        chat_id=CHATID,
        message_id=messageID,
        text=text
    )

### Bio Function ###

RE_SCRAPE_BIO = re.compile(r'<meta +property="og:description" +content="(.+?)".*>')
RE_USERNAME = re.compile(r'@([a-zA-Z][\w\d]{4,31})')

def getBioUsernames(username):
    r = requests.get("http://t.me/" + username)
    if not r.ok:
        print("Networking Error: " + r.status_code)
        return []
    bio = RE_SCRAPE_BIO.findall(r.text)
    return RE_USERNAME.findall(bio[0])
