import importlib.util
import io
import logging
import os
import random
import string

import PIL.Image
from pyrogram import Client, filters
from pyrogram.types import Message
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from main import prefixes

_path = os.path.dirname(__file__)
_selenium_path = os.path.join(_path, "../_selenium/_selenium.py")

if not os.path.exists(_selenium_path):
    raise Exception("The _selenium plugin needs to be enabled to work")

spec = importlib.util.spec_from_file_location("driverWrapper", _selenium_path)
_selenium = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_selenium)
driverWrapper = getattr(_selenium, "driverWrapper")

SEND_PHOTO = False  # set to True to recive the photo in png format too

OPTIONS = Options()
OPTIONS.headless = True

CSS_SELECTOR = "div.tgme_widget_message.js-widget_message"


@Client.on_message(
    filters.me & filters.reply & filters.command("msg2sticker", prefixes=prefixes)
)
def msg2sticker(c: Client, msg: Message):
    targetmsg = msg.reply_to_message

    if not targetmsg.chat.username:
        msg.edit_text("Not supported in private chats!")
        return 1

    msg.edit_text("Initializing driver...")

    try:
        driver: Firefox = driverWrapper(options=OPTIONS)
    except Exception as e:
        logging.error(f"An exception occurred -> {type(e).__name__}: {e}")
        msg.edit_text("Something went wrong!")
        return 1

    msg.edit_text("Reaching https://telegram.me/...", disable_web_page_preview=True)

    driver.get(
        "https://t.me/{}/{}?embed=1".format(
            targetmsg.chat.username, targetmsg.message_id
        )
    )

    element = driver.find_element_by_css_selector(CSS_SELECTOR)

    if not element:
        msg.edit_text("Something went wrong!")
        return 1

    image: PIL.Image.Image = PIL.Image.open(io.BytesIO(element.screenshot_as_png))

    path = "tmp/" + "".join(random.choices(string.ascii_letters, k=40)) + ".webp"
    image.save(path, "webp")

    driver.quit()
    msg.edit_text("Sending sticker...")

    c.send_sticker(msg.chat.id, path, reply_to_message_id=targetmsg.message_id)

    if SEND_PHOTO:
        path = "tmp/" + "".join(random.choices(string.ascii_letters, k=40)) + ".png"

        image.save(path, "png")

        c.send_photo(msg.chat.id, path, reply_to_message_id=targetmsg.message_id)

    msg.delete()
