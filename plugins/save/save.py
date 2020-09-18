from pyrogram import Client, filters

from main import prefixes


@Client.on_message(
    filters.reply & filters.user("self") & filters.command("save", prefixes=prefixes)
)
def save_command(c, msg):
    msg.reply_to_message.forward("self")
    msg.delete()
