FROM python:3.7-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY --chown=microblog:microblog app app
COPY --chown=microblog:microblog migrations migrations
COPY --chown=microblog:microblog microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

# Copying with --chown flag is MUCH faster than recursively setting the flag afterwards!
#RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]