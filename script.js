fetch("wrapped_data.json")
  .then(res => res.json())
  .then(data => {
    // Minutes listened
    document.getElementById("minutes").textContent =
      `${data.time.minutes.toLocaleString()} minutes`;

    // Top artists
    const artistList = document.getElementById("artists");
    data.topArtists.forEach(a => {
      const li = document.createElement("li");
      li.textContent = a.artist;
      artistList.appendChild(li);
    });

    // Top songs
    const songList = document.getElementById("songs");
    data.topSongs.forEach(s => {
      const li = document.createElement("li");
      li.textContent = `${s.track} — ${s.artist}`;
      songList.appendChild(li);
    });
  });
