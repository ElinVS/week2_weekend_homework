import unittest
# from classes.guest import Guest
# from classes.room import Room
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Little Talks")
       
    
    def test_song_1_has_name(self):
        self.assertEqual("Little Talks",self.song_1.song_title)