from abc import ABC, abstractmethod
from telegram.ext import Updater, CommandHandler, CallbackContext


class BaseCommand(ABC):
    commands = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.commands.append(cls)

    @abstractmethod
    def __call__(self, update: Updater, context: CallbackContext):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError
