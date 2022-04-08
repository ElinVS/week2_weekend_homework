import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Bob", 51, 100, "More Than This" )

# tests starts here:

    def test_guest_has_name(self):
        self.assertEqual("Bob",self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(51, self.guest_1.age)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("More Than This", self.guest_1.favourite_song)