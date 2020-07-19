import requests
from bs4 import BeautifulSoup


class Wikipedia:
    def __init__(self) -> None:

        """You can use this class to look up a page on wikipedia"""

        self.__author__ = "GodSaveTheDoge"
        self.selector = "#mw-content-text li , p"
        self.url = "https://{}.wikipedia.org/wiki/{}"
        self.apiurl = (
            "https://en.wikipedia.org/w/api.php?action=query&titles={}&format=json"
        )

    def exists(self, page: str) -> bool:

        """
        Check if a page exists
        :param page: url of the page
        :return:
        """

        if "-1" in requests.get(self.apiurl.format(page)).json()["query"]["pages"]:
            return False
        return True

    def getpage(self, page: str, limit: int = 5, lang: str = "en") -> str:

        """
        Get the content of a page
        :param page: url of the page
        :param limit: max number of <p> taken
        :param lang: language to use
        :return:
        """

        tags = BeautifulSoup(
            requests.get(self.url.format(lang, page)).text, "lxml"
        ).select(self.selector)
        res = ""
        for i in range(min(limit, len(tags))):
            res += tags[i].text + "\n\n"
        return res
