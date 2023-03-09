# Django playground

Django Lets Go! :rocket: :rocket: :rocket:

## Pre-requisites

- Docker
- brew install postgresql

## Local Development

- `docker-compose up -d`
- If you changed the requirements.txt file you need to rebuild the image using `docker-compose up --build -d`
- Watching the logs for the web app `docker-compose logs web -f`
- Running compose in the container `docker-compose exec -it  web bash` (Windows) or `docker-compose exec -it  web sh`(MacOS)
