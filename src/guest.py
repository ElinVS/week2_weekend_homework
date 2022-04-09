class Guest:
    def __init__(self, name, age, wallet, favourite_song, stamina_to_sing):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.stamina_to_sing = stamina_to_sing   

    def has_enough_stamina_for_song(self,song):
        if self.stamina_to_sing < song:
            return "Take a Break"
        return "Just keep singing"