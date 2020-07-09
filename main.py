# MultiUserbot by GodSaveTheDoge
# Github: https://github.com/GodSaveTheDoge/MultiUserbot

import sys

if sys.version_info.minor < 7:
    print("You should use python 3.7 or higher.\n")

from pyrogram import Client
import os
import configparser

ubot = Client(
    "MultiUserbot",
    config_file="config.ini")

config = configparser.ConfigParser()
config.read("config.ini")
prefixes = list(config["prefixes"].keys())
# This is an easy way to have the prefixes in the config file
# Later prefixes will be imported in the plugins

if not os.path.exists("MultiUserbot.session"):
    print("Write /commands in a chat to see the commands avaiable!")

if os.path.exists("tmp"):
    os.removedirs("tmp")

if __name__ == "__main__":
    ubot.start()
