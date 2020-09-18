import logging
import random
import string

from pyrogram import Client, filters
from pyrogram.types import Message

from main import prefixes
from methods.ImageUpscale import ImageUpscaler, InternalServerError

imu = ImageUpscaler()


@Client.on_message(filters.me & filters.reply & filters.command("upscale", prefixes=prefixes))
def upscale(c: Client, msg: Message):
    if not (msg.reply_to_message.photo or msg.reply_to_message.document):
        msg.edit_text("Please reply to a photo or document")
        return 1
    if msg.reply_to_message.document:
        logging.warning("Documents aren't always upscalable.")

    fname = "tmp/" + "".join(random.choices(string.ascii_letters, k=30)) + ".jpeg"  # Photos are sent as jpeg
    msg.reply_to_message.download(file_name=fname, progress=download_update, progress_args=(msg,))

    msg.edit_text(
        "Upscaling...\n"
        "[{s}????{s}] ??%".format(s=" " * 8)
    )

    try:
        ufname = "tmp/" + "".join(random.choices(string.ascii_letters, k=30)) + ".png"  # Photos are recived in .png
        open(ufname, "wb").write(imu.upscale(fname))
    except InternalServerError:
        msg.edit_text("Document not valid!")
        return 1

    msg.edit_text(
        "Uploading...\n"
        "[{s}????{s}] ??%".format(s=" " * 8)
    )
    c.send_photo(msg.chat.id,
                 ufname,
                 reply_to_message_id=msg.reply_to_message.message_id,
                 caption="<b>Upscaled</b>"
                 )
    msg.delete()


def download_update(progress, progress_total, msg):
    percent = progress / progress_total * 100
    bar = "=" * (int(percent / 10) - 1) + ">"
    msg.edit_text(
        "Downloading\n"
        "<code>[{}] {:.1f}%</code>".format(bar + " " * (10 - len(bar)), percent)
    )
