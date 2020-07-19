import urllib.parse
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup


class Bing:
    def __init__(self, useragent: str = b"\xf0\x9f\xa5\x94".decode("utf-8")) -> None:
        """
        This class is used to search things on bing.com
        :param useragent: The useragent to use. Default to a potato as a joke
        """

        self.__author__ = "GodSaveTheDoge"
        self.selector = ".b_algo h2 a"
        self.url = "https://www.bing.com/search?q={}&form=QBLH"
        self.headers = {
            "IAmAPotato": "Yes".encode("utf-8"),
            "User-Agent": useragent.encode("utf-8"),
        }

    def search(self, keyword: str) -> List[Tuple[str, str]]:
        """
        Search something on bing.com
        :param keyword: Keywords for the search
        :return:
        """

        tags = BeautifulSoup(
            requests.get(
                self.url.format(urllib.parse.quote(keyword)), headers=self.headers,
            ).text,
            "lxml",
        ).select(self.selector)
        results = []
        for t in tags:
            results.append((t.get_attribute_list("href")[0], t.text))
        return results
