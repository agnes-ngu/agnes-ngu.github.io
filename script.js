fetch("wrapped_data.json")
  .then(res => res.json())
  .then(data => {
    //Custom Nav bar
    const nav = document.getElementById("morphNav");
    const toggle = document.getElementById("navToggle");

    toggle.addEventListener("click", () => {
      nav.classList.toggle("open");
    });

    // Time listened
    document.getElementById("totMinutes").textContent = 
      `${data.time.minutes.toLocaleString()} minutes`;
    document.getElementById("hours").textContent = 
      `${data.time.hours.toLocaleString()} hours`;
    document.getElementById("days").textContent = 
      `${data.time.days.toLocaleString()} days`;
    document.getElementById("years").textContent = 
      `${data.time.years.toLocaleString()} years`;
  

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

    // Total artists
    document.getElementById("artistsTotal").textContent = 
      `${data.totalArtists} artists`;
      
    // Top artist stats
    document.getElementById("artistTop").textContent =
      data.topArtistStats.artist;
    document.getElementById("artistMin").textContent =
      `${data.topArtistStats.minutes} minutes listened`;
    document.getElementById("artistHour").textContent =
      `That's ${data.topArtistStats.hours} hours`;
    document.getElementById("artistStatTop").textContent =
      data.topArtistStats.artist;
    document.getElementById("artistPeakDay").textContent =
      `Date most streamed: ${data.topArtistStats.peakDate}`;
    document.getElementById("artistPeakTime").textContent =
      `Time streamed on this date: ${data.topArtistStats.peakMin} minutes (${data.topArtistStats.peakHour} hours)`;

    // Top Song stats
    document.getElementById("songTop").textContent =
      `${data.topSongStats.track} - ${data.topSongStats.artist}`;
    document.getElementById("songMin").textContent =
      `${data.topSongStats.totalMin} minutes listened`;
    document.getElementById("songHr").textContent =
      `That's ${data.topSongStats.totalHours} hours`;
    document.getElementById("SongStatName").textContent =
      `${data.topSongStats.track} - ${data.topSongStats.artist}`;
    document.getElementById("songPeakDay").textContent =
      `Day most streamed: ${data.topSongStats.peakDay}`;
    document.getElementById("songPeakTime").textContent =
      `Time streamed on this date: ${data.topSongStats.peakMin} minutes`;
      

    // Scroll to top button
    let mybutton = document.getElementById("scrollBtn");

    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
      } else {
        mybutton.style.display = "none";
      }
    }

    function topFunction() {
      document.body.scrollTop = 0; // For Safari
      document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    }
  });
