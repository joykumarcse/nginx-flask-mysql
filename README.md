# Python(Flask+nginx+mysql) Project deploy using Docker

Prerequisite on the environment:
1. Docker
2. Docker compose

Clone this project on your local environment:
```
git clone https://github.com/joykumarcse/nginx-flask-mysql.git
```
go to the project directory
```
cd nginx-flask-mysql
```
run the command
```
docker compose -f docker-compose.yml up --build -d
```

Check from browser
```
http://localhost/
```

