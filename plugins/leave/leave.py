from pyrogram import Client, filters

from main import prefixes


@Client.on_message(filters.user("self") & filters.command("leave", prefixes=prefixes))
def leave_command(c, msg):
    msg.delete()
    msg.chat.leave()
