import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song




class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Yellow Duck")
        

    def test_room_1_has_name(self):
        self.assertEqual("Yellow Duck",self.room_1.name)

   