from pyrogram import Client

c = Client(
    ":memory:",
    api_id=123456,  # EDIT ME in api_id=YOUR_API_ID_HERE,
    api_hash="abcdefgh"  # EDIT ME in api_hash="YOUR_API_HASH_HERE"
)
c.start()
print("Session string ->", c.export_session_string())
c.stop()
