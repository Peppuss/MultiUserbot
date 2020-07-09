from pyrogram import Client, Filters

from main import prefixes


@Client.on_message(Filters.reply & Filters.user("self") & Filters.command("save", prefixes=prefixes))
def save_command(c, msg):
    msg.reply_to_message.forward("self")
    msg.delete()
