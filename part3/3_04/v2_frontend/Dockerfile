FROM python:3.10-slim

ENV FLASK_APP=todo_frontend.py
ENV BACKEND_URL=$BACKEND_URL

WORKDIR /usr/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]