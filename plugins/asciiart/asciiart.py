import random
import string

import PIL.Image
from pyrogram import Client, Filters
from pyrogram import Message

from main import prefixes

ASCII_CHARSET = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
MAXWIDTH = 80
MAXHEIGHT = 50


def resize_width(image: PIL.Image, mwidth,
                 mheight) -> PIL.Image:  # The limit is 101 characters, in mono on my machine :)
    width, height = image.size
    ratio = min(mwidth / width, mheight / height)
    return image.resize((int(width * ratio), int(height * ratio)))


def convert_grayscale(image: PIL.Image) -> PIL.Image:
    return image.convert("L")


def generate_ascii_art(image: PIL.Image,
                       ascii_charset: list) -> str:  # not only lists works but for the sake of semplicity I'll leave only list as suggested type
    ascii_art = ""
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            ascii_art += ascii_charset[pixel // (255 // len(ascii_charset)) - 1]
        ascii_art += "\n"
    return ascii_art


@Client.on_message(Filters.reply & Filters.user("self") & Filters.command("asciiart", prefixes=prefixes))
def asciiart(c, msg):
    # Check if the message replied to is valid
    targetmsg: Message = msg.reply_to_message
    if not targetmsg.photo or targetmsg.sticker:
        msg.edit_text("Please reply to a photo or a sticker!")

    # if so, download the photo and create image object
    filename = "tmp/" + "".join(random.choices(string.ascii_letters, k=30)) + ".image"
    targetmsg.download(file_name=filename)
    image = PIL.Image.open(filename)

    # resize the image
    image: PIL.Image = resize_width(image, MAXWIDTH, MAXHEIGHT)

    # convert it to grayscale
    image: PIL.Image = convert_grayscale(image)

    # convert pixels to ascii art
    asciiart = generate_ascii_art(image, ASCII_CHARSET)

    # edits the message to the ascii art
    msg.edit_text("<pre>" + asciiart + "</pre>", parse_mode="html")
