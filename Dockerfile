FROM python:3.8-alpine

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY pandulce.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP pandulce.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
