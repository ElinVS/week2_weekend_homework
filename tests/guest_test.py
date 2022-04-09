import unittest
from src.guest import Guest
# from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):

        self.guest_1 = Guest("Charlotte", 22, 50, "Brass in pocket", 4.00)
        self.guest_2 = Guest("Bob", 51, 100, "More Than This", 2.00)
        
        self.song_1 = Song("Brass in pocket", 3.00)
        

### tests starts here:

    def test_guest_has_name(self):
        self.assertEqual("Bob",self.guest_2.name)

    def test_guest_has_age(self):
        self.assertEqual(51, self.guest_2.age)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_2.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("More Than This", self.guest_2.favourite_song)

    def test_if_guest_has_stamina_to_sing(self):
        self.assertEqual(2, self.guest_2.stamina_to_sing)

    def test_if_guest_will_run_out_of_stamina__false(self):
        self.assertEqual("Take a Break", self.guest_2.has_enough_stamina_for_song(self.song_1.length_of_song))

    def test_if_guest_will_run_out_of_stamina__true(self):
        self.assertEqual("Just keep singing", self.guest_1.has_enough_stamina_for_song(self.song_1.length_of_song))