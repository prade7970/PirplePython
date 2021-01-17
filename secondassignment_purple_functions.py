
"""
Pirple Assignment 1 - Variables

"""

# Describe a song

song_name = 'Feliz Navidad' #name
song_year= 1988  #year released
song_duration_sec= 180 #duration of the song
song_composer = 'Anonymous' #Composed
song_copyright_owner= 'Public License' #Copyright owners
song_spotify_enabled = False #Availability on Spotify
song_played_number=10  #Number of Times song played
song_genre='Christmas Carol' #Genre of the song
song_favorited_number=20 


def GetSongName(song_name):
    return song_name

def GetSongGenre(song_genre):
    return song_genre

def CheckIfSongOnSpotify(song_spotify_enabled):
    if (song_spotify_enabled==True):
        return "you can listen to this on spotify"
    else:
        return "Sorry!"


print("Song Name is " + GetSongName(song_name) + '\n' +
      "Song Genre is " + GetSongGenre(song_genre) + '\n' +
      "Spotify Availability :" + CheckIfSongOnSpotify(song_spotify_enabled)
     )







    