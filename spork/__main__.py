from telegram import Bot
from telegram.ext import Updater, CommandHandler
import sys
from spork.commands.hello import HelloCommand

PROXY = 'https://telegg.ru/orig/bot'


def main(access_token: str):
    bot = Bot(
        token=access_token,
        base_url=PROXY,  # delete it if connection via VPN
    )
    updater = Updater(bot=bot, use_context=True)
    updater.dispatcher.add_handler(HelloCommand)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    access_token = sys.argv[1]
    main(access_token)
