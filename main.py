# MultiUserbot by GodSaveTheDoge
# Github: https://github.com/GodSaveTheDoge/MultiUserbot

import sys

if sys.version_info.minor < 7:
    print("You should use python 3.7 or higher.\n")

from pyrogram import Client
import os
import configparser
import shutil
import logging

ubot = Client(
    "MultiUserbot",
    config_file="config.ini")

config = configparser.ConfigParser()
config.read("config.ini")
prefixes = list(config["prefixes"].keys())
# This is an easy way to have the prefixes in the config file
# Later prefixes will be imported in the plugins

if os.path.exists("tmp"):
    shutil.rmtree("tmp", ignore_errors=True)

if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s %(asctime)s] In module %(module)s, function %(funcName)s at line %(lineno)d -> %("
               "message)s",
        datefmt="%d/%m/%Y %H:%M:%S %p", level=logging.WARN)
    ubot.start()

if not os.path.exists("MultiUserbot.session"):
    logging.warning("Write /commands in a chat to see the commands available!")
