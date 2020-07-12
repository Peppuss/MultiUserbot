from typing import Optional

from pyrogram import Message


def ArgumentOrReply(msg: Message, offset: int = 0) -> Optional[str]:
    if len(msg.command) > 1:
        return " ".join(msg.command[1:]) if not offset else msg.text[offset:]
    elif msg.reply_to_message:
        return msg.reply_to_message.text or msg.reply_to_message.caption
    else:
        return None  # this final else is not really needed but I prefer to make it explicit
