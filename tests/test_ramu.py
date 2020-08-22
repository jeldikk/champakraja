import unittest

from champakraja import ramu



class TestCharacterRamu(unittest.TestCase):

    def setUp(self):
        self.actor = ramu('ramunajam')

    def test_books(self):
        books = self.actor.books()
        self.assertGreater(len(books), 1)

    def test_hobbies(self):
        hobbies = self.actor.hobbies()
        self.assertTrue('worship god' in hobbies)

    def test_activities(self):
        acts = self.actor.activities()
        self.assertEqual(len(acts),3)

    def test_hairstyle(self):
        style = self.actor.hairstyle()
        self.assertTrue(style[0] == 'long hair with a pony tail')
    
    def test_nature(self):
        nature = self.actor.nature()
        self.assertTrue('responsible' in nature)

