import time

from pyrogram import Client, filters, emoji

from main import prefixes

HEARTS = [
    emoji.RED_HEART,
    emoji.ORANGE_HEART,
    emoji.YELLOW_HEART,
    emoji.GREEN_HEART,
    emoji.PURPLE_HEART,
    emoji.BLUE_HEART,
    emoji.BLACK_HEART,
]
TIMEOUT = 0.3
NUM = 50  # 10 seconds, should be good
SPACE = b"\xe2\x80\x8c".decode()


@Client.on_message(filters.me & filters.command("heart", prefixes=prefixes))
def heart(c, msg):
    for _ in range(NUM):
        msg.edit_text(SPACE + HEARTS[_ % len(HEARTS)])
        time.sleep(TIMEOUT)
