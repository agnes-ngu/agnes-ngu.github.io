import json
from collections import defaultdict

FILES = [
    "StreamingHistory_music_0.json.json",
    "StreamingHistory_music_1.json.json",
    "StreamingHistory_music_2.json.json"
]

def total_listening_time(files):
    total_ms = 0
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                total_ms += entry.get("msPlayed", 0)

    minutes = total_ms / 60000
    return {
        "minutes": round(minutes),
        "hours": round(minutes / 60),
        "days": round(minutes / 60 / 24),
        "years": round(minutes / 60 / 24 / 365, 4)
    }

def top_artists(files, top_n=5):
    artist_time = defaultdict(int)

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                artist = entry.get("artistName")
                if artist:
                    artist_time[artist] += entry.get("msPlayed", 0)

    return sorted(
        artist_time.items(),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]

def top_songs(files, top_n=5):
    song_time = defaultdict(int)

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                track = entry.get("trackName")
                artist = entry.get("artistName")
                ms = entry.get("msPlayed", 0)
                if track and artist:
                    song_time[(track, artist)] += ms

    return [
        {
            "track": track,
            "artist": artist,
            "min": round(ms / 60000),
            "hr": round(ms / 3600000)
        }
        for (track, artist), ms in sorted(
            song_time.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_n]
    ]

def total_unique_artists(files):
    artists = set()

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                if entry.get("artistName"):
                    artists.add(entry["artistName"])

    return len(artists)

def top_artist_stats(files):
    artist_time = defaultdict(int)
    daily_playtime = defaultdict(int)
    
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                artist = entry.get("artistName")
                if artist:
                    artist_time[artist] += entry.get("msPlayed", 0)
                
    artist, total_ms = max(artist_time.items(), key=lambda x: x[1])

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                if entry.get("artistName") == artist:
                    date = entry["endTime"].split(" ")[0]
                    daily_playtime[date] += entry.get("msPlayed", 0)

    peak_day, peak_ms = max(daily_playtime.items(), key=lambda x: x[1])

    return {
        "artist": artist,
        "msPlayed": total_ms,
        "minutes": round(total_ms / 60000),
        "hours": round(total_ms / 3600000),
        "peakDate": peak_day,
        "peakMin": round(peak_ms / 60000),
        "peakHour": round(peak_ms / 3600000)
    }

def top_song_stats(files):
    song_total = defaultdict(int)
    daily_song_time = defaultdict(lambda: defaultdict(int))

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                track = entry.get("trackName")
                artist = entry.get("artistName")
                ms = entry.get("msPlayed", 0)

                if track and artist:
                    song_key = (track, artist)
                    song_total[song_key] += ms

                    day = entry["endTime"].split(" ")[0]
                    daily_song_time[song_key][day] += ms

    # Identify top song overall
    (track, artist), total_ms = max(
        song_total.items(),
        key=lambda x: x[1]
    )

    # Find peak day for that song
    peak_day, peak_day_ms = max(
        daily_song_time[(track, artist)].items(),
        key=lambda x: x[1]
    )

    return {
        "track": track,
        "artist": artist,
        "peakDay": peak_day,
        "peakMin": round(peak_day_ms / 60000),
        "peakHr": round(peak_day_ms / 3600000, 2),
        "totalMin": round(total_ms / 60000),
        "totalHours": round(total_ms / 3600000, 2)
    }



if __name__ == "__main__":
    output = {
        "time": total_listening_time(FILES),
        "topArtists": [
            {"artist": a, "msPlayed": ms}
            for a, ms in top_artists(FILES)
        ],
        "topSongs": top_songs(FILES),
        "totalArtists": total_unique_artists(FILES),
        "topArtistStats": top_artist_stats(FILES),
        "topSongStats": top_song_stats(FILES)
    }

    with open("wrapped_data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print("✅ wrapped_data.json created")
