from .base import character

class ravan(character):

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    def books(self):
        return ('garuda puranam', 'papaala puranam', 'dhandaka Grandham')

    def hobbies(self):
        return ('punishing people', 'gets irritated with wrongs', 'riding buffaloe', 'moving eyes right to left')

    def activities(self):
        return ('scavenging on people', 'respecting the righteous person', 'self irriated guy', 'martial arts',)

    def hairstyle(self):
        return ('long hair falling over face',)

    def nature(self):
        return ('extremely violent', 'dangerous',)