import unittest
from classes.guest import Guest
# from classes.room import Room
# from classes.song import Song

#guest add song to room playlist



class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Bill Murray", 51)


    def test_guest_1_has_name(self):
        self.assertEqual("Bill Murray",self.guest_1.name)