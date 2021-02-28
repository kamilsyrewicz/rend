FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
ENV FLASK_CONF /var/www/app/config/dev_config
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt