from typing import Union

import requests


class Nekobin:
    def __init__(self):
        """This class is used to paste things using nekobin.com"""
        self.__author__ = "GodSaveTheDoge"
        self.baseurl = "https://nekobin.com/"
        self.session = requests.session()

    def paste(self, text: str) -> Union[str, Exception]:

        """
        Paste things with nekobin.com
        :param text: Text to paste
        :return:
        """

        r = self.session.post(self.baseurl + "api/documents", data={"content": text})
        try:
            return r.json()["result"]["key"]
        except Exception as e:
            return e
