# Spotify Dummy

A simple Django application that displays a Spotify playlist with song details.

## Installation

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
docker build -t spotify-dummy .
docker run -p 8000:8000 spotify-dummy


