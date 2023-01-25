This is a AlphaZero-like AI for playing Ultimate Tic Tac Toe.

docker build -t uttt_app .
docker run -it -p 8000:8888 uttt_app
docker login
docker tag uttt_app enderwaraxe/uttt_app
docker push enderwaraxe/uttt_app

gcloud services enable containerregistry.googleapis.com
docker pull enderwaraxe/uttt_app
docker tag enderwaraxe/uttt_app gcr.io/ultimate-tic-tac-toe-359401/uttt_app
docker push gcr.io/ultimate-tic-tac-toe-359401/uttt_app

The game is running at
https://uttt.kopibot.net/
