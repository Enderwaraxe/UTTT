# Dockerfile
FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r ./requirements.txt
COPY src .
COPY data/* .
CMD ["gunicorn"  , "-b", "0.0.0.0:8888", "app:app"]
# CMD ["python" , "app.py"]