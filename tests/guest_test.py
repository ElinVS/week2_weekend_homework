import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Bob", 51, "More Than This" )

# tests starts here:

    def test_guest_has_name(self):
        self.assertEqual("Bob",self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(51, self.guest_1.age)