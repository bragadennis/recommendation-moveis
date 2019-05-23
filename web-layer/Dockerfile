FROM ubuntu:16.04

ARG port=8000

LABEL Dennis Braga "bragadennis.dev@gmail.com"

RUN apt-get update -y && apt-get install -y python-pip python-dev

# For Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "flask", '--host', 'localhost', '--port', $port ]

CMD [ "mainapp.py" ]