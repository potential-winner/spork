from spork.hello import hello_to
from telegram.ext import Updater, CommandHandler, CallbackContext


def help(update: Updater, context: CallbackContext):
    hello_message = hello_to(update.message.from_user.first_name)
    update.message.reply_text(hello_message)
