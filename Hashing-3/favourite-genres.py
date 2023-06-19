# TC: O(U*S + U*G) | SC: O(S + G) where U: number of users, S: number of songs, G: number of genres
def favorite_genre(userMap, genreMap):
    res = {}
    song_to_genre = {}

    for genre in genreMap:
        for song in genreMap[genre]:
            song_to_genre[song] = genre

    for user in userMap:
        count = {}
        max_count = 0
        res[user] = []

        for song in userMap[user]:
            genre = song_to_genre.get(song, None)
            if genre is not None:
                count[genre] = count.get(genre, 0) + 1
                max_count = max(count[genre], max_count)

        for genre, genre_count in count.items():
            if genre_count == max_count:
                res[user].append(genre)
    return res


if __name__ == "__main__":
    user_songs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"],
    }

    song_genres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"],
    }

    res = favorite_genre(user_songs, song_genres)
    print(res)
