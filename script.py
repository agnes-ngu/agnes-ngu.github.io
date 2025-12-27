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
        "hours": round(minutes / 60, 2),
        "days": round(minutes / 60 / 24, 2),
        "years": round(minutes / 60 / 24 / 365, 4)
    }

def top_artists(files, top_n=3):
    artist_time = defaultdict(int)

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                artist = entry.get("artistName")
                ms = entry.get("msPlayed", 0)
                if artist:
                    artist_time[artist] += ms

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
        {"track": t, "artist": a, "msPlayed": ms}
        for (t, a), ms in sorted(
            song_time.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_n]
    ]

if __name__ == "__main__":
    output = {
        "time": total_listening_time(FILES),
        "topArtists": [
            {"artist": a, "msPlayed": ms}
            for a, ms in top_artists(FILES)
        ],
        "topSongs": top_songs(FILES)
    }

    with open("wrapped_data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print("✅ wrapped_data.json created")
