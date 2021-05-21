import pandas as pd
from yandex_music.client import Client
from yandex_music.client import YandexMusicObject
from yandex_music.client import Feed
from yandex_music.client import Playlist
from yandex_music.client import YandexMusicObject
from yandex_music.utils.request import Request
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

import logging
logger = logging.getLogger('yandex_music')
logger.setLevel(logging.ERROR)

# token = 'AgAAAAAdd1wnAAG8XmKtK_OilUrLnbVALguNrUc'
client = Client.from_credentials('AlexandrKornilov84@yandex.ru', '123456qwerty')
# client = Client.from_token(token=token)
for i in client.genres():
    for j in i['sub_genres']:
        print(j['title'])

userid = client.users_settings().uid

user_playlists = client.usersPlaylistsList()
target_pl = user_playlists[0].playlist_id


# feed = client.feed()
# personal_pl = client.landing(blocks = 'personalplaylists').blocks[0].entities
# personal_pl = personal_pl[1]
# personal_pl = personal_pl.id


day_playlist = client.feed().generated_playlists[1].data.tracks
day_playlist = client.tracks([i.id for i in day_playlist])
gen_playlist = [(track.title, track.artists[0].name) for track in day_playlist]



from yandex_music import playlist
from yandex_music import YandexMusicObject
playlist.PlaylistRecommendations
# Add all disliked tracks in Favorites
disliked = [track.track for track in disliked.tracks]
client.users_likes_tracks_add(track_ids = [i.track_id for i in disliked], user_id=userid )
# Remove tracks from disliked
client.users_dislikes_tracks_remove([i.track_id for i in disliked], user_id=userid)

[i.playlist_id for i in user_playlists]
for i in user_playlists:
    client.Playlist


kinds = [i.kind for i in user_playlists]
[i.description for i in client.usersPlaylists(kinds[0])]





# Delete playlists with name 'disliked'
# playlists = client.users_playlists_list()
# playlists = [(i.kind, i.title) for i in playlists]
# for i in playlists:
#     if i[1] == 'disliked':
#         client.users_playlists_delete(kind = i[0], user_id = userid)
#     else:
#         pass

# tracks = [i.track for i in playlist.tracks]
#
#
# all = [track.to_dict() for track in tracks]
# all = [i['artists'] for i in all]
# all_names = []
# for i in all:
#     for p in i:
#         all_names.append(p['name'])
#
# df = pd.DataFrame(i.to_dict() for i in tracks)
# df = df.set_index('id_').sort_index()









# titles = [i['title'] for i in df['_track']]
# artists = [i['artists'] for i in df['_track']]
# names = [i[:] for i in artists]
# # df['artists'] = artists
# df['titles'] = titles
#
# df.to_excel('123.xlsx')
# PersonalPlaylistBlocks =  client.landing(blocks=['personalplaylists']).blocks[0];
# DailyPlaylist = next(x.data.data for x in PersonalPlaylistBlocks.entities if x.data.data.generated_playlist_type == 'playlistOfTheDay')
#