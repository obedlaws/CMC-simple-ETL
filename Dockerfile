FROM python:latest

RUN pip install requests

WORKDIR /app

COPY main.py  ./
COPY config.py ./
COPY load.py ./ 

CMD [ "python3", "./main.py" ]