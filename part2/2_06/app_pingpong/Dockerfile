FROM python:3.10-slim

ENV FLASK_APP=pingpong.py

WORKDIR /usr/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]