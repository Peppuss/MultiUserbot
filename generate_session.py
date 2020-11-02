from pyrogram import Client

c = Client(
    ":memory:",
    api_id=508596,  # EDIT ME in api_id=YOUR_API_ID_HERE,
    api_hash="348c9929974d063d3265010569689ce1",  # EDIT ME in api_hash="YOUR_API_HASH_HERE",
    config_file="no_configuration_files"
)
c.start()
print("Session string ->", c.export_session_string())
c.stop()
