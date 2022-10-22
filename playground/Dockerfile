
FROM python:3.8-slim

WORKDIR /app
RUN pip install Flask gunicorn
COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]
