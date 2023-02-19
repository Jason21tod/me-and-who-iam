FROM python:3.8-slim-buster 
WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "flask", "--app", "api/app", "run", "--host=0.0.0.0"]