import logging

from selenium import webdriver


class driverWrapper(webdriver.Firefox):  # wrapper for the selenium webdriver
    def __getattr__(
            self, attribute: str
    ):  # credits to nocturn9x https://github.com/nocturn9x/BotBase
        """
        This is used to "intercept" function calls / attributes and return a different thing
        :param attribute:
        :return:
        """
        if attribute in self.__dict__:
            return self.__dict__[attribute]
        else:

            def wrapper(*args, **kwargs):
                if hasattr(self.instance, attribute):
                    try:
                        return getattr(self.instance, attribute)(*args, **kwargs)
                    except Exception as e:
                        logging.error(
                            f"An exception occurred -> {type(e).__name__}: {e}"
                        )
                        return e
                else:
                    raise AttributeError(self.instance, attribute)

            return wrapper
