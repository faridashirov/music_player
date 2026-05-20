# 🎵 Music Player

A Django-based CRUD web application for uploading and listening to music tracks.

## Features

- Upload music files with cover images
- Play tracks directly in the browser
- Create, read, update, and delete songs
- Clean, responsive interface built with HTML/CSS

## Tech Stack

- **Backend:** Python, Django 6.0
- **Frontend:** HTML, CSS
- **Image handling:** Pillow
- **Database:** SQLite (default)

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

git clone https://github.com/faridashirov/music_player.git
cd music_player

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

Open `http://127.0.0.1:8000` in your browser.

## Dependencies

asgiref==3.11.0
Django==6.0
pillow==12.0.0
sqlparse==0.5.5

## Project Structure

music_player/
├── music/          # Main app (models, views, urls, templates)
├── requirements.txt
└── .gitignore
