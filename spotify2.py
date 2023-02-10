
#Spotify API
import requests
import base64
import json
from secrets import clientId, clientSecret
from autho_flow import get_access_token

#Step 1 Authorization

url = "https://accounts.spotify.com/authorize?"
headers = {}
data = {}

playlistId = "2a765mFBKp3GYoC3F5cSMn"
# playlistUrl = "https://api.spotify.com/v1/tracks?ids=0yLdNVWF3Srea0uzk55zFn%2C4Dvkj6JhhA12EX05fT7y2e%2C4uUG5RXrOk84mYEfFvj3cK%2C5ww2BF9slyYgNOk37BlC4u%2C0WtM2NBVQNNJLh6scP13H8"
playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}/tracks?limit=20"
token= get_access_token()
headers = {"Authorization": "Bearer " + token}

# res = requests.get(url=playlistUrl, headers=headers)
# print(f"The returned data: {res.json()}")
# with open("myfile.json","w") as file:
#     file.write(json.dumps(res.json()))
# print(json.dumps(res.json(), indent=2))

# my_playlistURL= "https://api.spotify.com/v1/users/31uikk4e2d2hwgfq74sxwnpuq76a/playlists"
# post_headers = {"Authorization": "Bearer " + "BQAF2mxJ1Mkt9WWp2J933xire5FAb2NXIDKpjgRGeudhON6GBk0anAdxdy2Rm9y13gFaEidzSRLt3I4bR5gbn4237-LgSuOOmTIzfmqylX4ZSlBaJZI9NbkNPG-0NqlNn7_hspObdKHED_n-GfhyTgO2jelJYj62nGQIJUkmzt-6Hsqalfv0lR1-l8ZyACoI5pHRm8X4dUpkVW-YDE3_5QYXq6fGY2ArCkB3OP7T2Lml6sOCe8tvciMfU1Ww0NbS-gxxfwSM9jdDmBmudLlWndKnyK73EjjcQWK978v3Elm5HzNAuDFs_wUrbu878wwu3FkzzP54mLahAg"}

# my_databody= {"name":"my_playlist","description":"New playlist description","public":False}
# res = requests.post(url=my_playlistURL,json=my_databody, headers=post_headers)
# print(json.dumps(res.json(), indent=2))


# add_trackURL="https://api.spotify.com/v1/playlists/2a765mFBKp3GYoC3F5cSMn/tracks?uris=spotify%3Atrack%3A0yLdNVWF3Srea0uzk55zFn%2Cspotify%3Atrack%3A1Qrg8KqiBpW07V7PNxwwwL%2C"

# res = requests.post(url=add_trackURL,headers=post_headers)
# print(json.dumps(res.json(), indent=2))


USA_playlist_id = "37i9dQZEVXbLp5XoPON0wI"
global_playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
global_top_50_playlist = f"https://api.spotify.com/v1/playlists/{global_playlist_id}/tracks?limit=5"
USA_top_50_playlist = f"https://api.spotify.com/v1/playlists/{USA_playlist_id}/tracks?limit=5"

global_response = requests.get(url=global_top_50_playlist, headers=headers)
USA_response = requests.get(url=USA_top_50_playlist, headers=headers)

my_track_ids = []

global_response_json = global_response.json()
my_global_tracks_list = global_response_json["items"]
for track in my_global_tracks_list:
    track_info_id = track["track"]["id"]
    my_track_ids.append(track_info_id)

USA_response_json = USA_response.json()
my_USA_tracks_list = USA_response_json["items"]
for track in my_USA_tracks_list:
    track_info_id = track["track"]["id"]
    my_track_ids.append(track_info_id)

list_of_track_uris = ""
for track_id in my_track_ids:
    list_of_track_uris = list_of_track_uris + f"spotify%3Atrack%3A{track_id}%2C"

print(list_of_track_uris)

playlist_id = "2a765mFBKp3GYoC3F5cSMn"
posts_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={list_of_track_uris}"
save_track_response = requests.post(url=posts_url, headers=headers)
print(json.dumps(save_track_response.json()))



