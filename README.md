# MultiUserbot
A [Telegram](https://telegram.me) Userbot to do cool stuff

[![Python 3.6](https://img.shields.io/badge/Python-3.6%20or%20newer-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dec3fe46191d47fc8a5155406eef49af)](https://www.codacy.com/manual/GodSaveTheDoge/MultiUserbot)
![GitHub repo size](https://img.shields.io/github/repo-size/GodSaveTheDoge/MultiUserbot)
[![HitCount](http://hits.dwyl.com/GodSaveTheDoge/MultiUserbot.svg)](http://hits.dwyl.com/GodSaveTheDoge/MultiUserbot)

## Getting started

### You need to have python 3.5 or higher (3.7 / 3.8 suggested)

-   Clone this repository (or download the zip and unzip it) `git clone https://github.com/GodSaveTheDoge/MultiUserbot.git`
-   Change directory `cd MultiUserbot `
-   Install wheel `pip install wheel`
-   Install libraries `pip install -r requirements.txt`
-   Go to [Telegram api page](https://my.telegram.org/apps) and get your api id and api hash
-   Open config.ini with your favourite editor and put your api id and api hash (line 2 and 3)
-   Read [How To Use Plugins](plugins/HowToUsePlugins.md)
-   Run the bot `python main.py `

## Common error

One of the most common errors is caused by the wrong version of python. Please check with `python -V` the version you have installed.
(Before trying to install another version of python try using `python3` instead of `python` and `python3 -m pip` instead of `pip`)

## Notes

-   This code is still buggy and not optimized at all, I'm still developing this. I'd suggest to wait until a "stable" release.
-   Some plugins will create and use a "tmp" folder, you can delete it (when the bot is not running). If you do not do this it'll be delete on the startup anyway.

## Contact me

-   [Telegram profile](https://t.me/GodSaveTheDoge)
-   [Telegram channel](https://t.me/GodSaveTheBots)