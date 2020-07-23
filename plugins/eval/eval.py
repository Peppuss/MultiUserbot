import html
import io
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
    old_stdout = sys.stdout
    redirected_stdout = sys.stdout = io.StringIO()

    try:
        eval_result = eval(code)
    except Exception as e:
        eval_result = ""
        tb = "".join(traceback.format_exception(e, e, sys.exc_info()[2])).rstrip("\n ")
    else:
        tb = ""

    sys.stdout = old_stdout
    stdout_value = redirected_stdout.getvalue().rstrip("\n ")
    result = stdout_value + ("\n" + tb if tb else "")

    try:
        if len(code + str(result)) > 2000:
            msg.edit_text("Uploading to nekobin...")
            msg.edit_text(
                "<b>Code:</b>\n{pasted}\n\n<b>Eval Result:</b>\n{pasted}\n\n<b>Result:</b>\n{pasted}".format(
                    pasted='Too long! <a href="https://nekobin.com/{url}">Pasted</a>'.format(
                        url=Nekobin.paste(
                            "Code:\n{}\n\nEval Result:\n{}\n\nResult:\n{}".format(str(code), str(eval_result),
                                                                                  str(result))
                        )
                    )
                )
            )
        else:
            msg.edit_text(
                "<b>Code:</b>\n<code>{}</code>\n\n<b>Eval Result:</b>\n{}\n\n<b>Result:</b>\n<code>{}</code>".format(
                    html.escape(str(code)), html.escape(eval_result), html.escape(str(result))
                ),
                parse_mode="html",
            )
    except Exception as e:
        msg.edit_text(str(e))
