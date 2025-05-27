# 🎧 Spotify Dummy

**Spotify Dummy** is a minimalist clone of the Spotify web player, designed to mimic the core layout and styling of Spotify's interface. This project serves as a front-end template for developers looking to build music streaming interfaces or practice UI/UX design.

![Spotify Dummy Screenshot](https://github.com/pringleshowboi/Spotify_Dummy/blob/main/spotify_dummy/screenshot.png?raw=true)

---

## 🛠️ Features

- 🎵 **Home Page**: Showcases featured playlists and albums.
- 🔍 **Search Functionality**: Allows users to search for artists, albums, or tracks.
- 📁 **Your Library**: Displays user's saved playlists and liked songs.
- 🎶 **Now Playing Bar**: Persistent bottom bar showing current track info and playback controls.

---

## 🚀 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) installed on your machine.


### Prerequisites

- Python 3.8+
- Django 4.2+
- Docker (optional)

### Setup

1. Clone the repository
```sh
git clone https://github.com/yourusername/spotify-dummy.git
cd spotify-dummy

To run locally
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

```
2. To run on Docker
```
docker build -t spotify-dummy .
docker run -p 8000:8000 spotify-dummy


