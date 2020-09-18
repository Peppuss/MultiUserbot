import random
import string

from pyrogram import Client, filters, emoji
from pyrogram.types import Message

from main import prefixes
from methods.Nekobin import Nekobin

Nekobin = Nekobin()


@Client.on_message(
    filters.user("self") & filters.command("paste", prefixes=prefixes) & filters.reply
)
def paste_command(c: Client, msg: Message):
    msg.edit_text("Pasting...")
    if msg.reply_to_message.document:

        path = "tmp/{}".format("".join(random.choices(string.ascii_letters, k=30)))
        msg.reply_to_message.download(file_name=path)

        try:
            text = open(path).read()
        except UnicodeDecodeError:
            msg.edit_text("Please reply to a document or a message with some text")
            return 1

    else:
        text = msg.reply_to_message.text or msg.reply_to_message.caption

    if not text:
        msg.edit_text("Please reply to a document or a message with some text")
        return 1

    key = Nekobin.paste(text)
    msg.edit_text(
        f"{emoji.GLOBE_WITH_MERIDIANS} Paste {emoji.GLOBE_WITH_MERIDIANS}\n"
        f"\n"
        f"{emoji.LINK} Url: https://nekobin.com/{key}\n"
        f"{emoji.NEWSPAPER} Raw: https://nekobin.com/raw/{key} \n"
        f"\n",
        disable_web_page_preview=True,
    )
