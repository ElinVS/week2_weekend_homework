import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Brass in pocket")
        
### tests starts here:

    def test_song_1_has_name(self):
         self.assertEqual("Brass in pocket",self.song_1.song_title)

    