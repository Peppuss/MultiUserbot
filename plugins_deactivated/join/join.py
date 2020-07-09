from pyrogram import Client, Filters

from main import prefixes


@Client.on_message(Filters.user("self") & Filters.command("join", prefixes=prefixes))
def join_command(c, msg):
    if len(msg.command) < 2:
        msg.edit_text("Please use: <code>/join CHAT</code>")
        return 0
    try:
        c.join_chat(msg.command[1])
    except Exception as e:
        msg.edit_text("Could not join chat.\n{}".format(e))
    else:
        msg.edit_text("Joined.")
