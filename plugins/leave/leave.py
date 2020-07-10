from pyrogram import Client, Filters

from main import prefixes


@Client.on_message(Filters.user("self") & Filters.command("leave", prefixes=prefixes))
def leave_command(c, msg):
    msg.delete()
    msg.chat.leave()
