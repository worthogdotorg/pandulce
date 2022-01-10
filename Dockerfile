FROM python:3.8-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -U pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY pandulce.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP pandulce.py

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
#RUN useradd appuser && chown -R appuser /app
#USER appuser

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
