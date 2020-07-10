import urllib.parse

from pyrogram import Client, Filters, Message

from main import prefixes


@Client.on_message(Filters.user("self") & Filters.command("qr", prefixes=prefixes))
def qr(c: Client, msg: Message):
    if msg.reply_to_message:
        text = msg.reply_to_message.text or msg.reply_to_message.caption
        if not text:
            msg.edit_text("Not a valid message!")
    elif len(msg.command) > 1:
        text = msg.text[len("/qr"):]
    else:
        msg.edit_text("Please reply to a message or specify the text like <code>/qr GodSaveTheDoge</code>")
        return 1
    msg.delete()
    c.send_photo(
        msg.chat.id,
        "https://chart.googleapis.com/chart?chs=500x500&cht=qr&chl={}".format(urllib.parse.quote(text))
    )
