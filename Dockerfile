FROM ubuntu:18.10
LABEL maintainer="premanuj <mesubedianuj@gmail.com>"
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-dev apt-utils
RUN apt-get update 
RUN apt-get install -y pip3
RUN apt-get install -y nginx
RUN pip3 install uwsgi
RUN pip3 install pipenv
COPY ./ ./flask_restful_structure
WORKDIR ./app
RUN pipenv install
COPY ./nginx.conf /etc/nginx/sites-enabled/default
CMD service nginx start && uwsgi -s /tmp/uwsgi.sock --chmod- socket=666 --manage-script-name --mount /=app:app
