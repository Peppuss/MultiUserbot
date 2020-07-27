# MultiUserbot

A [Telegram](https://telegram.me) Userbot to do cool stuff

[![Python 3.6](https://img.shields.io/badge/Python-3.6%20or%20newer-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dec3fe46191d47fc8a5155406eef49af)](https://www.codacy.com/manual/GodSaveTheDoge/MultiUserbot)
![GitHub repo size](https://img.shields.io/github/repo-size/GodSaveTheDoge/MultiUserbot)
[![HitCount](http://hits.dwyl.com/GodSaveTheDoge/MultiUserbot.svg)](http://hits.dwyl.com/GodSaveTheDoge/MultiUserbot)
[![Contact Me](https://img.shields.io/badge/Telegram-Contact%20Me-informational)](https://t.me/DogeSaveTheGod)


## Getting started with heroku

### Requirements

-   ```bash
    $ python -V
    Python 3.x.y
    ```

-   A [Heroku](http://heroku.com/) account
-   Pyrogram installed
  
      ```bash
      pip install pyrogram tgcrypto
      ```

#### Get your api id and api hash

Go to [Telegram Site](https://my.telegram.org) and login, then go to the [apps page](https://my.telegram.org/apps).

If needed, compile the form and make an app.

#### Get your session string

Either download [generate_session.py](generate_session.py) or run

```bash
python -c 'from pyrogram import Client as c; b=c(":memory", api_id=YOURAPIID, api_hash="YOURAPIHASH");b.start();print("Your session string ->", b.export_session_string());b.stop()'#### Deploy
```

replace `YOURAPIID` with, well, you api id and `YOURAPIHASH` with your api hash.

the output will be something like:

```bash
$ python -c 'from pyrogram import Client as c; b=c(":memory", api_id=123456, api_hash="abcdef1gh93");b.start();print("Your session string ->", b.export_session_string());b.stop()'
Pyrogram v0.17.1, Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
Licensed under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+)

Enter phone number or bot token: +11234567890
Is "+11234567890" correct? (y/N): y
The confirmation code has been sent via Telegram app
Enter confirmation code: 123456
Your session string -> 5ckRLf2ZM4WioP1TSyS4G1xWGCzHKVu0di2Sqsehsqih4wwvQcAor/VQo+LjPHXoweqitSXzUaDeRqyILaR0by+Bpmb8uCIrfNuutKsqcsgOh0YEPr0GaEjHzDavEuYOIpWEhQ==
$
```

where `5ckRLf2ZM4WioP1TSyS4.....WEhQ==` is your session string

#### Deploy to heroku

Click this button and, if needed, login.

Then put the session_string in the form, click deploy and it should be running!

Not that it takes a minute or so.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Getting started with your hosting (or your pc)

### Requirements

-   Python 3.6.0 or higher (3.8.2 suggested)
  
    ```bash
    $ python -V
    Python 3.x.y
    ```

#### Clone this repository (or download the zip and unzip it)

`git clone https://github.com/GodSaveTheDoge/MultiUserbot.git`

##### Change directory

 `cd MultiUserbot `

#### Install libraries

`pip install -r requirements.txt`

#### Get your api id and api hash

Go to [Telegram Site](https://my.telegram.org) and login, then go to the [apps page](https://my.telegram.org/apps).

If needed, compile the form and make an app.

#### Modify the config file

Open config.ini with your favourite editor and put your api id and api hash (line 2 and 3)

#### Read [How To Use Plugins](plugins/HowToUsePlugins.md)

#### Run the bot
```bash
python main.py 
```

## Contact me

-   [Telegram profile](https://t.me/GodSaveTheDoge) (Currently unactive, I'm more active [here](https://t.me/DogeSaveTheGod))
-   [Telegram channel](https://t.me/GodSaveTheBots)