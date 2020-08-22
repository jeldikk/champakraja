from .base import character


class ramu(character):

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    def books(self):
        return ('chandamama', 'swathi', 'ramayanam', 'Mahabharatham',)

    def hobbies(self):
        return ('respecting', 'worship god',)

    def activities(self):
        return ('job', 'early namaskara', 'orthodox rituals')

    def hairstyle(self):
        return ('long hair with a pony tail',)

    def nature(self):
        return ('cowardice', 'responsible',)