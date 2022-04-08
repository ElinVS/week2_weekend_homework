import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        
        self.guest_1 = ("Charlotte", 22)
        self.guest_2 = ("Bob", 51)
        self.guest_3 = ("Fumihiro", 36)

        self.song_1 = "Brass in pocket"
        self.song_2 = "More Than This"
        self.song_3 = "God save the Queen"

        play_list_1 = []
        guest_list_1 = []

        self.room_1 = Room("Karaoke Kan",play_list_1, guest_list_1)

        play_list_2 = []
        guest_list_2 = []

        self.room_2 = Room("Lost in Karaoke", play_list_2, guest_list_2)
        

        #if full in room 1 add guest to room 2 if also full add to room 3
# /////////////////////////////////////////////////
    def test_room_has_name(self):
        self.assertEqual("Karaoke Kan",self.room_1.name)

    def test_number_of_guests_in_room(self):
        self.assertEqual(0, len(self.room_1.guest_list))

    def test_can_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_can_remove_guest_3_from_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.room_1.remove_guest_3_from_room(self.guest_3)
        self.assertEqual(2, len(self.room_1.guest_list))

    def test_number_of_songs_in_playlist(self):
        self.assertEqual(0,len(self.room_1.rooms_playlist))

    def test_can_add_song_to_rooms_playlist(self):
        self.room_1.add_song_to_rooms_playlist(self.song_1)
        self.assertEqual(1, len(self.room_1.rooms_playlist))
        
    def test_can_find_song_by_title_name_in_rooms_playlist(self):
        self.room_1.add_song_to_rooms_playlist(self.song_1)
        self.room_1.add_song_to_rooms_playlist(self.song_2)
        self.room_1.add_song_to_rooms_playlist(self.song_3)
        self.assertEqual(True, self.room_1.find_song_by_title(self.song_2))
        self.assertEqual(False, self.room_1.find_song_by_title("Hello Darkness"))

    def test_if_room_is_at_capacity(self):
        self.assertEqual(0, self.room_2.max_capacity)

    # def test_room_has_reached_max_capacity_in_room(self):
    #     self.room_1.add_guest_to_room(self.guest_1)
    #     self.room_1.add_guest_to_room(self.guest_2)
    #     self.room_1.add_guest_to_room(self.guest_3)
    #     self.assertEqual(3, self.room_1.check_max_capacity(self.room_1))


