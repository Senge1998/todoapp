FROM python:3.10.5

ENV VIRTUAL_ENV=/opt/venv 
RUN python3 -m venv $VIRTUAL_ENV

RUN apt-get update && apt install -y software-properties-common python3-setuptools

RUN apt-get install -y python3-dev default-libmysqlclient-dev libsasl2-dev libldap2-dev libssl-dev

ADD . /srv

WORKDIR /srv

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "todo.wsgi", "--access-logfile", "-", "--error-logfile", "-"]

