import requests


class Nekobin:
    def __init__(self):
        self.__author__ = "GodSaveTheDoge"
        self.baseurl = "https://nekobin.com/"
        self.session = requests.session()

    def paste(self, text):
        r = self.session.post(
            self.baseurl + "api/documents",
            data={"content": text}
        )
        try:
            return r.json()["result"]["key"]
        except Exception as e:
            return e
