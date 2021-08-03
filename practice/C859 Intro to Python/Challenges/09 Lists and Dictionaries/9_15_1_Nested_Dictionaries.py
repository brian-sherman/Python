"""
The following example demonstrates a program that uses 3 levels of nested dictionaries to create a simple music library.

The following program uses nested dictionaries to store a small music library. 
Extend the program such that a user can add artists, albums, and songs to the library. 
First, add a command that adds an artist name to the music dictionary. 
Then add commands for adding albums and songs. 
Take care to check that an artist exists in the dictionary before adding an album, and that an album exists before adding a song.

"""

music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

def menu():
    print('Select an option from the menu below')
    print('0: Quit')
    print('1: Add an artist')
    print('2: Add an album')
    print('3: Add a song')
    print('4: Print music')

def add_artist(artist):
    music[artist] = {}
    print(artist, 'has been added')

def add_album(artist,album):
    music[artist][album] = []
    print(album, 'has been added')

def add_song(artist,album,song):
    music[artist][album].append(song)
    print(song, 'has been added')

while True:
    menu()
    selection = input()
    if selection == '0':
        break
    if selection == '1':
        artist = input('Enter an artist\'s name to add: ')
        if artist in music:
            print(artist, 'already exists')
        else:
            add_artist(artist)
    elif selection == '2':
        artist = input('Enter the artist\'s name: ')
        album = input('Enter the album name: ')
        if artist not in music: 
            add_artist(artist)
            add_album(artist,album)
        elif album not in music[artist]:
            add_album(artist,album)
        else:
            print(album, 'already exists')
    elif selection == '3':
        artist = input('Enter the artist\'s name: ')
        album = input('Enter the album name: ')
        song = input('Enter the song name: ')
        if artist not in music:
            add_artist(artist)
            add_album(artist,album)
            add_song(artist,album,song)
        elif album not in music[artist]:
            add_album(artist,album)
            add_song(artist,album,song)
        elif song not in music[artist][album]:
            add_song(artist,album,song)
        else:
            print(song, 'already exists')
    elif selection == '4':
        print(music)

