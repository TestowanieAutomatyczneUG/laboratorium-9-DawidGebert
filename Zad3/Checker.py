from Player import Player

class Checker:
    def __init__(self):
        self.env = Player()
        self.was_played = False

    def remainder(self):
        if self.env.getTime().hour >= 17:
            self.env.playWavFile('file')
            self.wavWasPlayed()

    def wavWasPlayed(self):
        self.was_played = True

    def resetWav(self):
        self.was_played = False

    def returnWav(self):
        return self.was_played