import spotify_self_written as spotify
import pandas
from interface import *

# def save_playlist_to_csv(dict):
#     data = pandas.DataFrame(dict.items(), columns=['artist', 'song'])
#     data.index += 1
#     data.to_csv("current_spotify_library.csv")
#
#
#
#
# if __name__ == '__main__':
#     # spotify_saved_tracks = spotify.get_saved_tracks()
#     # save_playlist_to_csv(spotify_saved_tracks)
#     window.mainloop()

https://oauth.yandex.com/authorize?
   response_type=code
 & client_id=<app ID>
[& device_id=<device ID>]
[& device_name=<device name>]
[& redirect_uri=<redirect URL>]
[& login_hint=<username or email address>]
[& scope=<requested required rights>]
[& optional_scope=<requested optional rights>]
[& force_confirm=yes]
[& state=<arbitrary string>]