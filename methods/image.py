import random
import string

import PIL.Image
from pyrogram import Message


def get_image(msg: Message, name="".join(random.choices(string.ascii_letters, k=50))) -> PIL.Image.Image:
    path = f"tmp/{name}"
    msg.download(file_name=path)
    image = PIL.Image.open(path)
    return image


def save_image(image: PIL.Image.Image, name="".join(random.choices(string.ascii_letters, k=50))) -> str:
    path = f"tmp/{name}.png"
    image.save(path, format="PNG")
    return path
