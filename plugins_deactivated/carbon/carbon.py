import importlib.util
import logging
import os
import random
import string
import urllib.parse

from pyrogram import Client, filters
from pyrogram.types import Message
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from main import prefixes
from methods.ArgumentOrReply import ArgumentOrReply

_path = os.path.dirname(__file__)
_selenium_path = os.path.join(_path, "../_selenium/_selenium.py")

if not os.path.exists(_selenium_path):
    raise Exception("The _selenium plugin needs to be enabled to work")

spec = importlib.util.spec_from_file_location("driverWrapper", _selenium_path)
_selenium = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_selenium)
driverWrapper = getattr(_selenium, "driverWrapper")

CSS_SELECTOR = ".bg"
OPTIONS = Options()
OPTIONS.headless = True


@Client.on_message(filters.me & filters.command("carbon", prefixes=prefixes))
def carbon(c: Client, msg: Message):
    code = ArgumentOrReply(msg, len("/carbon "))
    if not code:
        msg.edit_text("Please reply to a message or use <code>/carbon My Text</code>")

    _params = {
        "bg": "rgba(57, 70, 79, 1)",
        "t": "seti",
        "wt": "none",
        "l": "auto",
        "ds": "true",
        "dsyoff": "20px",
        "dsblur": "68px",
        "wc": "true",
        "wa": "true",
        "pv": "56px",
        "ph": "56px",
        "ln": "false",
        "fl": "1",
        "fm": "Hack",
        "fs": "14px",
        "lh": "133%",
        "si": "false",
        "es": "2x",
        "wm": "false",
        "code": code,
    }

    params = "&".join(
        ["{}={}".format(i, urllib.parse.quote(j)) for i, j in _params.items()]
    )

    msg.edit_text("Initializing driver...")

    try:
        driver: Firefox = driverWrapper(options=OPTIONS)
    except Exception as e:
        logging.error(f"An exception occurred -> {type(e).__name__}: {e}")
        msg.edit_text("Something went wrong!")
        return 1

    msg.edit_text("Reaching https://carbon.now.sh/...", disable_web_page_preview=True)

    driver.get("https://carbon.now.sh/?" + params)

    element = driver.find_element_by_css_selector(CSS_SELECTOR)

    if not element:
        msg.edit_text("Something went wrong!")
        return 1

    if not os.path.exists("tmp"):
        os.mkdir("tmp")

    path = "tmp/" + "".join(random.choices(string.ascii_letters, k=40)) + ".png"
    open(path, "wb").write(element.screenshot_as_png)

    driver.quit()
    msg.edit_text("Sending photo...")

    if msg.reply_to_message:
        c.send_photo(
            msg.chat.id, path, reply_to_message_id=msg.reply_to_message.message_id
        )
    else:
        c.send_photo(msg.chat.id, path)

    msg.delete()
