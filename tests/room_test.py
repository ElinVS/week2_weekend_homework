import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        
        self.guest_1 = Guest("Charlotte", 22, 50, "Brass in pocket")
        self.guest_2 = Guest("Bob", 51, 100, "More Than This" )
        self.guest_3 = Guest("Fumihiro", 36, 20, "God save the Queen")
        self.guest_4 = Guest("John", 32, 70, "Lost in Kyoto")

        self.song_1 = Song("Brass in pocket")
        self.song_2 = Song("More Than This")
        self.song_3 = Song("God save the Queen")

        play_list_1 = []
        guest_list_1 = []
        self.room_1 = Room("Karaoke Kan",play_list_1, guest_list_1, 3, 30)

        play_list_2 = []
        guest_list_2 = []
        self.room_2 = Room("Lost in Karaoke", play_list_2, guest_list_2, 4, 40)
        

        
### tests starts here:

    def test_room_has_name(self):
        self.assertEqual("Karaoke Kan" , self.room_1.name)

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

    def test_if_room_has_a_capacity_checker(self):
        self.assertEqual(4, self.room_2.max_capacity)

    def test_room_is_full_add_to_quee(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.room_1.add_guest_to_room(self.guest_4)
        self.assertEqual(1, len(self.room_1.add_to_queue))
        self.assertEqual("Whilst you are waiting for a new room would you like a drink?",self.room_1.add_guest_to_room(self.room_1.add_to_queue))

    def test_check_if_room_has_entry_fee(self):
        self.assertEqual(30, self.room_1.entry_fee)

    def test_can_find_customers_wallet(self):
        self.assertEqual(50, self.guest_1.wallet)

    def test_guest_can_afford_entry_to_room__true(self):
        self.assertEqual(True, self.room_1.guest_can_afford_entry(self.guest_1))

    def test_guest_can_afford_entry_to_room__false(self):
        self.assertEqual(False, self.room_2.guest_can_afford_entry(self.guest_3))


    def test_guests_favourite_song_in_rooms_playlist(self):
        play_list = [self.song_2,self.song_3 ]
        guest_list = [self.guest_1,self.guest_2]
        self.room_3 = Room("Make it Santori Time", play_list, guest_list, 5, 50)
        self.assertEqual("I love this song!", self.room_3.find_favourite_song(self.song_2, self.guest_2))
        self.assertEqual("I refuse to sing in this room!", self.room_3.find_favourite_song(self.song_1, self.guest_1))




