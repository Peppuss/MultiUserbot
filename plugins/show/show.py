import time

from pyrogram import Client, filters

from main import prefixes


@Client.on_message(filters.user("self") & filters.command("show", prefixes=prefixes))
def show_command(c, msg):
    if len(msg.command) < 2:
        msg.edit_text("Please use <code>/show your text</code>")
        return 0
    text = msg.text[len("/show "):]
    for i, j in enumerate(text, start=0):  # i = index, j = value
        if j in (" ", "\n"):  # space and new line
            time.sleep(0.15)
            continue
        msg.edit_text(text[: i + 1])
        time.sleep(0.3)
