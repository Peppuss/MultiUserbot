from pyrogram import Client, Filters

from main import prefixes
from methods.Wiki import Wikipedia

wiki = Wikipedia()
language = "en"


@Client.on_message(
    Filters.user("self") & Filters.command("wikipedia", prefixes=prefixes)
)
def wikipedia_command(c, msg):
    global language
    if len(msg.command) < 2:
        msg.edit_text("Please use <code>/wikipedia Doge</code>")
        return 0
    elif len(msg.command) > 2:
        page = "_".join(msg.command[1:])
    else:
        page = msg.command[1]

    if wiki.exists(page):
        text = wiki.getpage(page, lang=language)
        if text:
            msg.edit_text(text)
        else:
            msg.edit_text("Could not get the page <code>{}</code>".format(page))
    else:
        msg.edit_text("The page <code>{}</code> does not exist.".format(page))


@Client.on_message(
    Filters.user("self") & Filters.command("wikipedialang", prefixes=prefixes)
)
def wikipedialang_command(c, msg):
    global language
    if len(msg.command) < 2:
        msg.edit_text("Please use <code>/wikipedialang en</code>")
    language = msg.command[1]
