# This might not work all the times.

import configparser

import requests
from pyrogram import Client, Filters, Emoji

config = configparser.ConfigParser()
config.read("config.ini")
prefixes = list(config["prefixes"].keys())


class Nekobin:
    def __init__(self):
        self.__author__ = "GodSaveTheDoge"
        self.baseurl = "https://nekobin.com/"
        self.session = requests.session()

    def paste(self, text):
        r = self.session.post(
            self.baseurl + "api/documents",
            data={"content": text}
        )
        try:
            return r.json()["result"]["key"]
        except Exception as e:
            return e


Nekobin = Nekobin()


@Client.on_message(Filters.user("self") & Filters.command("paste", prefixes=prefixes) & Filters.reply)
def paste_command(c, msg):
    msg.edit_text("Pasting...")
    if not msg.reply_to_message.text:
        if msg.reply_to_message.caption:
            text = msg.reply_to_message.caption
        else:
            msg.edit_text("Please reply to a message with some text")
            return 0
    else:
        text = msg.reply_to_message.text
    msg.edit_text(f"{Emoji.GLOBE_WITH_MERIDIANS} Paste {Emoji.GLOBE_WITH_MERIDIANS}\n"
                  f"\n"
                  f"{Emoji.LINK} Url: https://nekobin.com/{Nekobin.paste(text)}\n"
                  f"{Emoji.INPUT_LATIN_UPPERCASE} Text: {text[0:100]}...\n"
                  f"\n",
                  disable_web_page_preview=True
                  )


print("[MultiUserbot] Loaded \"paste_nekobin.py\" plugin")
