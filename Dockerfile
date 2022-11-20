FROM python:3.8.5-slim-buster
RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN apt install gcc -y
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]