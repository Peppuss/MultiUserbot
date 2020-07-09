from pyrogram import Client, Filters, Emoji

from main import prefixes
from methods.DelDog import DelDog

DelDog = DelDog()


@Client.on_message(Filters.user("self") & Filters.command("paste", prefixes=prefixes) & Filters.reply)
def paste_command(c, msg):
    msg.edit_text("Pasting...")
    if not msg.reply_to_message.text:
        if msg.reply_to_message.caption:
            text = msg.reply_to_message.caption
        else:
            msg.edit_text("Please reply to a message with some text")
            return 0
    else:
        text = msg.reply_to_message.text
    msg.edit_text(f"{Emoji.GLOBE_WITH_MERIDIANS} Paste {Emoji.GLOBE_WITH_MERIDIANS}\n"
                  f"\n"
                  f"{Emoji.LINK} Url: {DelDog.paste(text)}\n"
                  f"{Emoji.INPUT_LATIN_UPPERCASE} Text: {text[0:100]}...\n"
                  f"\n",
                  disable_web_page_preview=True
                  )
