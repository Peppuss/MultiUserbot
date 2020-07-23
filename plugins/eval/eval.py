import html
import sys
import traceback

from pyrogram import Client, Filters

from main import prefixes
from methods.Nekobin import Nekobin

Nekobin = Nekobin()


@Client.on_message(Filters.user("self") & Filters.command("eval", prefixes=prefixes))
def eval_command(c, msg):
    if len(msg.command) < 2:
        msg.edit_text(
            "Please use: <code>/eval msg.reply(some python code)</code>\nNote: Client = c, Message = msg"
        )
        return 0
    code = msg.text.html[len("/eval "):]
    try:
        result = eval(code).rstrip("\n ")
    except Exception as e:
        result = "".join(traceback.format_exception(e, e, sys.exc_info()[2]))
    try:
        if len(code + str(result)) > 2000:
            msg.edit_text("Uploading to nekobin...")
            msg.edit_text(
                "<b>Code:</b>\n{pasted}\n\n<b>Result:</b>\n{pasted}".format(
                    pasted='Too long! <a href="https://nekobin.com/{url}">Pasted</a>'.format(
                        url=Nekobin.paste(
                            "Code:\n{}\n\nResult:\n{}".format(str(code), str(result))
                        )
                    )
                )
            )
        else:
            msg.edit_text(
                "<b>Code:</b>\n<code>{}</code>\n\n<b>Result:</b>\n<code>{}</code>".format(
                    html.escape(str(code)[:1000]), html.escape(str(result)[:2000])
                ),
                parse_mode="html",
            )
    except Exception as e:
        msg.edit_text(str(e))
