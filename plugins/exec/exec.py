import html
import sys
import traceback

from pyrogram import Client, Filters

from main import prefixes


@Client.on_message(Filters.user("self") & Filters.command("exec", prefixes=prefixes))
def exec_command(c, msg):
    if len(msg.command) < 2:
        msg.edit_text(
            "Please use: <code>/exec msg.reply(some python code)</code>\nNote: Client = c, Message = msg"
        )
        return 0
    code = msg.text.html[len("/exec "):]
    try:
        result = exec(code)
    except Exception as e:
        result = "".join(traceback.format_exception(e, e, sys.exc_info()[2]))
    try:
        msg.edit_text(
            "<b>Code:</b>\n<code>{}</code>\n\n<b>Result:</b>\n<code>{}</code>".format(
                html.escape(str(code)[:1000]), html.escape(str(result)[:2000])
            ),
            parse_mode="html",
        )
    except Exception as e:
        msg.edit_text(str(e))
