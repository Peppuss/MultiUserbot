import time

from pyrogram import Client, Message, Filters, Emoji

from main import prefixes
from methods.GetExt import getname


@Client.on_message(Filters.me & Filters.reply & Filters.command("download", prefixes=prefixes))
def download(c: Client, msg: Message):
    starttime = time.time()

    fname = "Downloads/" + getname(c, msg)

    try:
        msg.reply_to_message.download(file_name=fname, progress=download_update,
                                      progress_args=(msg, fname))
    except Exception as e:
        msg.edit_text("Something went wrong:\n" + str(e))

    msg.edit_text(
        "{} <b>Downloaded</b>\n"
        "{} <b>Saved to:</b> <code>{}</code>\n"
        "{} <b>Time needed:</b> {:.1f}\n".format(Emoji.DOWN_ARROW, Emoji.FILE_FOLDER, fname,
                                                 Emoji.HOURGLASS_DONE,
                                                 time.time() - starttime)
    )


def download_update(progress, progress_total, msg, fname):
    percent = progress / progress_total * 100
    bar = "=" * (int(percent / 10) - 1) + ">"
    full_bar = "[{}]".format(bar + " " * (10 - len(bar)))
    msg.edit_text(
        "{} <b>Downloading...</b>\n"
        "{} <b>Saved to:</b> <code>{}</code>\n"
        "<code>{} {:.1f}%</code>".format(Emoji.DOWN_ARROW, Emoji.FILE_FOLDER, fname, full_bar, percent)
    )
