import unittest

from champakraja import ravan


class TestCharacterRavan(unittest.TestCase):

    def setUp(self):
        self.actor = ravan('aparichitudu')

    def test_books(self):
        books = self.actor.books()
        self.assertTrue('garuda puranam' in books)

    def test_hobbies(self):
        hobbies = self.actor.hobbies()
        self.assertGreater(len(hobbies), 1)

    def test_activities(self):
        acts = self.actor.activities()
        self.assertEqual(len(acts),4)

    def test_hairstyle(self):
        style = self.actor.hairstyle()
        self.assertEqual('long hair falling over face', style[0])

    def test_nature(self):
        nature = self.actor.nature()
        self.assertTrue('dangerous' in nature)