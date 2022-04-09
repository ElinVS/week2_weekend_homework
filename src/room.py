class Room:
    def __init__(self,name, play_list, guest_list,max_capacity, entry_fee):
        self.name = name
        self.rooms_playlist = play_list
        self.guest_list = guest_list
        self.max_capacity = max_capacity
        self.entry_fee = entry_fee
        self.add_to_queue = []


    def add_song_to_rooms_playlist(self,new_song):
        self.rooms_playlist.append(new_song)
        
    def add_guest_to_room(self, new_guest):
        self.guest_list.append(new_guest)

        if len(self.guest_list) > self.max_capacity:
            self.add_to_queue.append(new_guest)
        if len(self.add_to_queue) > 0:
            return "Whilst you are waiting for a new room would you like a drink?"


    def remove_guest_3_from_room(self,specific_guest):
        self.guest_list.remove(specific_guest)

    def find_song_by_title(self,song_title):
        for song in self.rooms_playlist:
            if song == song_title:
                return True
        
        return False

    def guest_can_afford_entry(self,guest):
        return guest.wallet >= self.entry_fee

    def find_favourite_song(self, song, guest):
        for loop in self.rooms_playlist:
            if loop == song and guest:
                return "I love this song!"

        return "I refuse to sing in this room!"












        


        
