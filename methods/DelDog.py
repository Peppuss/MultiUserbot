import requests


class DelDog:
    def __init__(self):
        self.__author__ = "GodSaveTheDoge"
        self.url = "https://del.dog/documents?frontend=true"
        self.headers = {
            "Content-Type": "application/json; charset=utf-8"
        }

    def paste(self, text, slug=""):
        r = requests.post(
            self.url,
            headers=self.headers,
            data=f'{{"content":"{text}", "slug":"{slug}"}}'.encode()  # utf-8
        )
        return "https://del.dog/{}".format(r.json()["key"])
