# Hang_an

A simple hangman game designed in Django, using the Jinja template language.

## Docker

```bash
docker build . -t webapp
docker run -it -p 8000:8000 webapp python3 manage.py runserver 0.0.0.0:8000
```
