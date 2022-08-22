from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')
# YTMusic.setup('headers_auth.json')
playlists = ytmusic.get_library_playlists(30)
for p in playlists:
    print(p['title'])
playlistName = input("What playlist do you want to find the total time of?: ")
while not (playlistName.lower() == "quit" or playlistName.lower() == "q"):
    for p in playlists:
        if p['title'] == playlistName:
            print(ytmusic.get_playlist(p['playlistId'])['duration'])
    if playlistName.lower() == "all":
        for p2 in playlists:
            if p2['title'] != "Your Likes":
                print(f"{p2['title']}: {ytmusic.get_playlist(p2['playlistId'])['duration']}")
    playlistName = input("What playlist do you want to find the total time of?: ")