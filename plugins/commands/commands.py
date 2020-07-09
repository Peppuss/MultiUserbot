import json
import os

from pyrogram import Client, Filters

from main import prefixes


@Client.on_message(Filters.user("self") & Filters.command("commands", prefixes=prefixes))
def commands_command(c, msg):
    commands = loadcommands()
    msg.edit_text(f"Avaiable Commands:\n"
                  f"\n" +
                  f"\n".join(["<b>" + d["command"] + "</b> - <pre>" + d["description"] + "</pre>" for d in commands]) +
                  f"\n\nPrefixes: {' '.join(prefixes)}")


def loadcommands():
    commands = []
    for (dirpath, dirnames, filenames) in os.walk("plugins"):
        for filename in filenames:
            if os.path.splitext(filename)[-1] == ".json":
                j = json.load(open(dirpath + "/" + filename))
                commands.append({
                    "command": j["command"],
                    "description": j["description"]
                })

    return commands
