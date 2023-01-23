#OpenAI GPT3 Assisted Code

import csv
import os

path = 'project/'
with open('100MostStreamedSongs.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row
    for row in reader:
        artist = row[3] # Get the artist name from the 4th column of the row
        song = row[1] # Get the song name from the 2nd column of the row
        artist_path = os.path.join(path, artist) # Get the path of the artist folder
        os.makedirs(artist_path, exist_ok=True)  # Create a directory with the artist name
        song_file = os.path.join(artist_path, song + ".txt")  # Get the path of the song file
        if not os.path.exists(song_file): #Check if the file already exists
            open(song_file, 'a').close() # Create the blank text file
    print("Program finished")