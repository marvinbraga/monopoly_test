# coding=utf-8
"""
Monopoly Game Project
Marcus Vinicius Braga, set 2021.

Abstract Observer Module.
"""
from abc import ABCMeta, abstractmethod


class AbstractObserver(metaclass=ABCMeta):
    """
    Abstract class to observer pattern.
    """
    _subject = None

    def set_subject(self, subject):
        """
        This method must be used right after associating the observer with the subject.
        :param subject: AbstractSubject Object.
        :return: Self.
        """
        self._subject = subject
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._subject:
            self._subject.detach(self)

    @abstractmethod
    def update(self, value):
        """
        Method to update the informations.
        :param value:
        :return:
        """
        pass


class AbstractSubject(metaclass=ABCMeta):
    """
    Class to observers manager.
    """
    _observers = set()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()

    def attach(self, observer: AbstractObserver):
        """
        Add observer to be notified.
        :param observer: AbstractObserver Object.
        :return: Self.
        """
        self._observers |= {observer}
        observer.set_subject(self)
        return self

    def detach(self, observer: AbstractObserver):
        """
        Turn off the observer object.
        :param observer: AbstractObserver Object.
        :return: Self.
        """
        self._observers -= {observer}
        return self

    def notify(self, value):
        """
        Update all managed observer instances.
        :param value:
        :return: Self.
        """
        for observer in self._observers:
            observer.update(value)
        return self
