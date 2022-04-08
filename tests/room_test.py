import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        play_list = []
        guest_list = []
        self.room_1 = Room("Karaoke Kan",play_list, guest_list)
        

        #if full in room 1 add guest to room 2 if also full add to room 3
# /////////////////////////////////////////////////
    def test_room_1_has_name(self):
        self.assertEqual("Karaoke Kan",self.room_1.name)

    def test_can_add_guest_to_room(self):
        self.guest_1 = ("Charlotte", 22)
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_number_of_songs_in_playlist(self):
        self.assertEqual(0,len(self.room_1.rooms_playlist))

    def test_can_add_song_to_rooms_playlist(self):
        self.song_1 = "More Than This"
        self.room_1.add_song_to_rooms_playlist(self.song_1)
        self.assertEqual(1, len(self.room_1.rooms_playlist))

    # def test_can_find_song_in_rooms_playlist(self):
