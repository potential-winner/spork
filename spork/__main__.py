from spork.hello import hello_to
from telegram import Bot
from telegram.ext import Updater, CommandHandler
import sys

PROXY = 'https://telegg.ru/orig/bot'

def hello(update, context):
    hello_message = hello_to(update.message.from_user.first_name)
    update.message.reply_text(hello_message)


def main(access_token: str):
    bot = Bot(
        token=access_token,
        base_url=PROXY,  # delete it if connection via VPN
    )
    updater = Updater(bot=bot, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    access_token = sys.argv[1]
    main(access_token)
