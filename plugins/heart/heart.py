import time

from pyrogram import Client, Filters, Emoji

from main import prefixes

HEARTS = [
    Emoji.RED_HEART,
    Emoji.ORANGE_HEART,
    Emoji.YELLOW_HEART,
    Emoji.GREEN_HEART,
    Emoji.PURPLE_HEART,
    Emoji.BLUE_HEART,
    Emoji.BLACK_HEART,
]
TIMEOUT = 0.3
NUM = 50  # 10 seconds, should be good
SPACE = b"\xe2\x80\x8c".decode()


@Client.on_message(Filters.me & Filters.command("heart", prefixes=prefixes))
def heart(c, msg):
    for _ in range(NUM):
        msg.edit_text(SPACE + HEARTS[_ % len(HEARTS)])
        time.sleep(TIMEOUT)
