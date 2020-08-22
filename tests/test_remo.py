import unittest

from champakraja import remo

class TestCharacterRemo(unittest.TestCase):

    def setUp(self):
        self.actor = remo('Remo the Playboy')
    
    def test_books(self):
        books = self.actor.books()
        self.assertGreater(len(books), 1)

    def test_hobbies(self):
        hobbies = self.actor.hobbies()
        self.assertTrue('modelling' in hobbies)

    def test_activities(self):
        acts = self.actor.activities()
        self.assertEqual(len(acts),3)

    def test_hairstyle(self):
        style = self.actor.hairstyle()
        self.assertTrue('long hair with stylish combed' == style[0])


    def test_nature(self):
        nature = self.actor.nature()
        self.assertTrue('romantic' in nature)