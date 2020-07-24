from typing import Union

import requests


class InternalServerError(Exception):
    pass


class ImageUpscaler:
    """Class to upscale images."""

    def __init__(self):

        """Initialize the class"""

        self.__author__ = "GodSaveTheDoge <https://github.com/GodSaveTheDoge>"
        self._SCHEME = "https"
        self._HOST = "ai.generated.photos"
        self.base_url = "{}://{}".format(self._SCHEME, self._HOST)

    def upscale(self, image: Union[str, bytes]) -> bytes:

        """
        Upscale an image
        :param image: Path to the image or the image
        :return: The image as bytes
        """

        if isinstance(image, str):
            photo: bytes = open(image, "rb").read()
        elif isinstance(image, bytes):
            photo: bytes = image
        else:
            raise TypeError("Expected a string or bytes, received {} instead.".format(type(image)))

        file = {
            "file": ("GodSaveTheDoge_is_a_cool_dev", photo)
        }

        r = requests.post(
            self.base_url + "/super-res/v1/enhance",
            files=file
        )

        if r.status_code == 500:
            raise InternalServerError("Recived 500 Interal Server Error")

        return r.content
