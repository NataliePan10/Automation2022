class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for x in self.lyrics:
            print(x)
song = ["Happy birthday to you", "Happy birthday to you", "Happy birthday","happy birthday","Happy birthday to you"]

abc=Song(song)
abc.sing_me_a_song()

