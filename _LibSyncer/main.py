import spotify_self_written as spotify
import pandas
from interface import *

def save_playlist_to_csv(dict):
    data = pandas.DataFrame(dict.items(), columns=['artist', 'song'])
    data.index += 1
    data.to_csv("current_spotify_library.csv")




if __name__ == '__main__':
    # spotify_saved_tracks = spotify.get_saved_tracks()
    # save_playlist_to_csv(spotify_saved_tracks)
    window.mainloop()