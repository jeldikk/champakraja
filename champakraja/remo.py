
from .base import character

class remo(character):
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    def books(self):
        return ('50 shades of grey', 'How to make life easier', '10 perks of spending time with girls',)

    def hobbies(self):
        return ('romanticizing', 'flirting girls', 'modelling', 'partying',)

    def activities(self):
        return ('modelling', 'loves naandi', 'fashioning',)

    def hairstyle(self):
        return ('long hair with stylish combed',)

    def nature(self):
        return ('romantic', 'love arrow thrower')