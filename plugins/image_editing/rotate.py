import PIL.Image
from pyrogram import Client, filters
from pyrogram.types import Message

from main import prefixes
from methods.image import get_image, save_image


@Client.on_message(
    filters.user("self") & filters.reply & filters.command("rotate", prefixes=prefixes)
)
def rotate(c: Client, msg: Message):
    targetmsg = msg.reply_to_message

    if not (targetmsg.photo or targetmsg.sticker):
        msg.edit_text("Reply to a sticker or photo!")
        return 1

    msg.delete()

    rotation = (
        180  # If rotation is 90, 180 or 270 there are constants like Image.ROTATE_180
    )

    if len(msg.command) > 1:
        try:
            rotation = int(msg.command[1])
        except ValueError:  # ValueError: invalid literal for int() with base 10
            pass

    image = get_image(targetmsg)

    rotated = image.rotate(rotation, PIL.Image.BICUBIC)

    c.send_photo(
        msg.chat.id,
        save_image(rotated),
        caption="<b>Rotated {} degrees</b>".format(rotation),
        reply_to_message_id=targetmsg.message_id,
    )
