from telegram import Bot
from telegram.ext import Updater

class Spork(object):
    def __init__(self, access_token: str, proxy: str):
        bot = Bot(
            token=access_token,
            base_url=proxy,  # delete it if connection via VPN
        )
        self._updater = Updater(bot=bot, use_context=True)

    def run(self):
        self._updater.start_polling()
        self._updater.idle()

    def updater(self) -> Updater:
        return self._updater
