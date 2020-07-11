import PIL.Image
import PIL.ImageOps
from pyrogram import Client, Filters, Message

from main import prefixes
from methods.image import get_image, save_image


@Client.on_message(Filters.user("self") & Filters.reply & Filters.command("invert", prefixes=prefixes))
def invert(c: Client, msg: Message):
    targetmsg: Message = msg.reply_to_message

    if not (targetmsg.photo or targetmsg.sticker):
        msg.edit_text("Please reply to a photo or a sticker!")
        return 1

    msg.delete()

    image: PIL.Image.Image = get_image(targetmsg)

    image = PIL.ImageOps.invert(image)

    c.send_photo(
        msg.chat.id,
        save_image(image),
        caption="<b>Inverted</b>",
        reply_to_message_id=targetmsg.message_id
    )
