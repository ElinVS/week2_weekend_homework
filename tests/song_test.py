import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Brass in pocket", 3.00)
        
### tests starts here:

    def test_song_has_name(self):
         self.assertEqual("Brass in pocket",self.song_1.song_title)

    def test_how_long_the_song_is(self):
        self.assertEqual(3.00, self.song_1.length_of_song)

    