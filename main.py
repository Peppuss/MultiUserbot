# MultiUserbot v 2.1
# Github: https://github.com/GodSaveTheDoge/MultiUserbot

import sys

if sys.version_info.minor < 7:
    print("You should use python 3.7 or higher.\n")

from pyrogram import Client
import os

bot = Client(
    "MultiUserbot",
    config_file="config.ini")

if not os.path.exists("MultiUserbot.session"):
    print("Write /commands in a chat to see the commands avaiable!")

bot.start()
