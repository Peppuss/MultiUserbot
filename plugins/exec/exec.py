import html
import io
import sys
import traceback

from pyrogram import Client, filters

from main import prefixes


@Client.on_message(filters.user("self") & filters.command("exec", prefixes=prefixes))
def exec_command(c, msg):
    if len(msg.command) < 2:
        msg.edit_text(
            "Please use: <code>/exec msg.reply(some python code)</code>\nNote: Client = c, Message = msg"
        )
        return 0
    code = msg.text.html[len("/exec "):]

    old_stdout = sys.stdout
    redirected_stdout = sys.stdout = io.StringIO()

    try:
        exec(code)
    except Exception as e:
        tb = "".join(traceback.format_exception(e, e, sys.exc_info()[2])).rstrip("\n ")
    else:
        tb = ""

    sys.stdout = old_stdout
    stdout_value = redirected_stdout.getvalue().rstrip("\n ")
    result = stdout_value + ("\n" + tb if tb else "")

    try:
        msg.edit_text(
            "<b>Code:</b>\n<code>{}</code>\n\n<b>Result:</b>\n<code>{}</code>".format(
                html.escape(str(code)[:1000]), html.escape(str(result)[:2000])
            ),
            parse_mode="html",
        )
    except Exception as e:
        msg.edit_text(str(e))
