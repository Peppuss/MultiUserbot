import os.path
import random
import string
from typing import Optional

from pyrogram import Client
from pyrogram.types import Message


def getext(c: Client, msg: Message) -> Optional[str]:
    """Get the extension of a document in a message"""

    if msg.reply_to_message.photo:
        return ".jpeg"

    elif msg.reply_to_message.sticker:
        return ".webp"

    for media_type in ("document", "audio", "video", "animation", "voice", "videonote"):
        if hasattr(msg.reply_to_message, media_type):

            if msg.reply_to_message[media_type].file_name:
                return c.guess_extension(
                    c.guess_mime_type(msg.reply_to_message[media_type].file_name)
                ) or os.path.splitext(msg.reply_to_message[media_type].file_name)[-1]

            if msg.reply_to_message[media_type].mime_type:
                return c.guess_extension(msg.reply_to_message[media_type].mime_type)


def getname(c: Client, msg: Message) -> str:
    """Get the name to download a file"""

    for media_type in ("document", "audio", "video", "animation", "voice", "videonote"):
        if (
            hasattr(msg.reply_to_message, media_type)
            and getattr(msg.reply_to_message, media_type)
            and msg.reply_to_message[media_type].file_name
        ):

            if not os.path.exists(msg.reply_to_message[media_type].file_name):
                return msg.reply_to_message[media_type].file_name

            name_ext = os.path.splitext(msg.reply_to_message[media_type].file_name)
            cnt = 1
            while True:
                possible_name_ext = list(name_ext)
                possible_name_ext[0] += str(cnt)

                if not os.path.exists("".join(possible_name_ext)):
                    return "".join(possible_name_ext)

                cnt += 1

    ext = getext(c, msg)
    fname = "".join(random.choices(string.ascii_letters, k=10)) + ext

    while os.path.exists(fname):
        fname = "".join(random.choices(string.ascii_letters, k=10)) + ext

    return fname
