import configparser
import json
import os

import requests
from pyrogram import Client, Filters, Emoji

config = configparser.ConfigParser()
config.read("config.ini")
prefixes = list(config["prefixes"].keys())

config.read(os.path.join(os.path.dirname(__file__), "apikey.ini"))
apikey = config["weather"]["api_key"]


@Client.on_message(Filters.user("self") & Filters.command("weather", prefixes=prefixes))
def weather_command(c, msg):
    if len(msg.command) < 2:
        msg.edit_text("Please use <code>/weather Roma</weather>")
        return 0

    target = " ".join(msg.command[1:])
    dirname = os.path.dirname(__file__)
    cities = json.load(open(os.path.join(dirname, "city.json")))

    for city in cities:
        if city["name"].lower() == target.lower():
            cid = city["id"]

    try:
        # noinspection PyUnboundLocalVariable
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}".format(cid, apikey)).json()
        if response["cod"] != 200:
            msg.edit_text("Error while looking up the weather: {}".format(response["message"]))
            return 0
        msg.edit_text(
            "{emoji} <b>Weather</b> {emoji}\n\n"
            "<b>City</b>: {name}\n"
            "<b>Country</b>: {country}\n"
            "<b>Lon</b>: {lon}\n"
            "<b>Lat</b>: {lat}\n"
            "\n"
            "<b>Temp</b>: {temp} (Celsius)\n"
            "<b>Pressure</b>: {pressure}\n"
            "<b>Humidity</b>: {humidity}\n"
            "\n"
            "<b>Wind Speed</b>: {winspeed}\n"
            "\n"
            "<b>Weather</b>: {wmain}\n"
            "<b>Description</b>: {wdescripion}\n".format(emoji=Emoji.SUN_BEHIND_LARGE_CLOUD,
                                                         name=response["name"],
                                                         country=response["sys"]["country"],
                                                         lon=response["coord"]["lon"],
                                                         lat=response["coord"]["lat"],
                                                         temp=round(response["main"]["temp"] - 273.15, 2),
                                                         pressure=response["main"]["pressure"],
                                                         humidity=response["main"]["humidity"],
                                                         winspeed=response["wind"]["speed"],
                                                         wmain=response["weather"][0]["main"],
                                                         wdescripion=response["weather"][0]["description"])
        )
    except NameError:
        msg.edit_text("City <i>{}</i> not found".format(target))
    except Exception as e:
        print(e)
        msg.edit_text("Something went wrong.")


print("[MultiUserbot] Loaded \"weather.py\" plugin")
