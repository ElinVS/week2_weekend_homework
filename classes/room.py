class Room:
    def __init__(self,input_name, play_list, guest_list):
        self.name = input_name
        self.rooms_playlist = play_list
        self.guest_list = guest_list


    def add_song_to_rooms_playlist(self,new_song):
        self.rooms_playlist.append(new_song)
        
    def add_guest_to_room(self, new_guest):
        self.guest_list.append(new_guest)

        
