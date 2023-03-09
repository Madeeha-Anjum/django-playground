FROM python:3.10-slim-bullseye

FROM --platform=linux/amd64 python:3.10-alpine

WORKDIR /app

# Copy requirements.txt to app directory from current directory
COPY requirements.txt requirements.txt


# Install requirements from requirements.txt 
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
 
 


# copy the files into the app directoey 
COPY ./app .

# Set the command to start the Django development server and run the migrations
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
