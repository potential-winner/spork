import sys

from telegram import Bot
from telegram.ext import Updater, CommandHandler

from spork.commands.hello import HelloCommand
from spork.spork import Spork

PROXY = 'https://telegg.ru/orig/bot'


def main(access_token: str):
    spork = Spork(access_token, PROXY)
    spork.addCommand(HelloCommand)
    spork.run()

if __name__ == "__main__":
    access_token = sys.argv[1]
    main(access_token)
