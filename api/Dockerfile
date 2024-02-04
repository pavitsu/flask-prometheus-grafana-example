FROM python:3.7-slim

# COPY . /api
# WORKDIR /api
RUN --mount=type=bind,source=./requirements.txt,target=requirements.txt \
 pip install -r requirements.txt 
# ENV FLASK_APP /api/server.py
EXPOSE 5000
# ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:5000" ,"wsgi:api"]
ENTRYPOINT [ "gunicorn", "-c", "gunicorn_conf.py"  , "--bind", "0.0.0.0:5000" ,"server:api"]
# gunicorn -c gunicorn_conf.py  --bind 0.0.0.0:5000 server:api
