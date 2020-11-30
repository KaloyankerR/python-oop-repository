from abc import ABC, abstractmethod


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


def play_instrument(instrument: Instrument):
    return instrument.play()
