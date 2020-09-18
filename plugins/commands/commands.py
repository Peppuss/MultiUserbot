import json
import os

from pyrogram import Client, filters

from main import prefixes


@Client.on_message(
    filters.user("self")
    & (
            filters.command("commands", prefixes=prefixes)
            | filters.command("help", prefixes=prefixes)
    )
)
def commands_command(c, msg):
    page = 0
    if len(msg.command) > 1:
        try:
            page = int(msg.command[1]) - 1
        except ValueError:
            msg.edit_text("Not a valid page.")
    try:
        msg.edit_text(commands_pages[page])
    except IndexError:
        msg.edit_text("There are only {} pages!".format(len(commands_pages)))


def loadcommands():
    commands = []
    for (dirpath, _, filenames) in os.walk("plugins"):
        for filename in filenames:
            if "".join(os.path.splitext(filename)[-2:]) == "command.json":
                j = json.load(open(dirpath + "/" + filename))
                for i in j:
                    commands.append(i)

    return commands


commands = loadcommands()
command_list = [
    "<b>" + d["command"] + "</b> - <pre>" + d["description"] + "</pre>"
    for d in commands
]

commands_pages = []
cnt = 0
while True:
    text = "Avaiable Commands:\n\n"
    for command in command_list[cnt:]:
        if len(text) > 1500:
            break
        text += command + "\n"
        cnt += 1
    else:
        text += f"\n\nPrefixes: {' '.join(prefixes)}\n"
        commands_pages.append(text)
        break
    text += (
        f"\n\nPrefixes: {' '.join(prefixes)}\n"
        f"Use <code>/help {len(commands_pages) + 2}</code> for the next page"
    )
    commands_pages.append(text)
