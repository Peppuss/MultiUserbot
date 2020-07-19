from pyrogram import Client, Filters, Emoji

from main import prefixes
from methods.Bing import Bing

Bing = Bing()


@Client.on_message(Filters.me & Filters.command("search", prefixes=prefixes))
def search_command(c, msg):
    msg.edit_text("Searching...")
    if len(msg.command) < 2:
        msg.edit_text("Please use <code>/search Your Keywords</code>")
        return 0
    results = Bing.search(" ".join(msg.command[1:]))
    if results:
        message = "{} Search {}\n\n".format(
            Emoji.GLOBE_WITH_MERIDIANS, Emoji.GLOBE_WITH_MERIDIANS
        )
        for r in results:
            message += f'{Emoji.HEAVY_MINUS_SIGN} <a href="{r[0]}">{r[1]}</a>\n'
        msg.edit_text(message, disable_web_page_preview=True)
    else:
        msg.edit_text("Nothing Found")
