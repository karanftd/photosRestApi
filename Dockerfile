FROM python:3.7-alpine

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

# Copy all our files into the image.
RUN mkdir /code
WORKDIR /code
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps


ENV LIBRARY_PATH=/lib:/usr/lib
COPY requirements.txt /code/requirements.txt
COPY . /code/

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt


# start our service
CMD gunicorn photosRestApi.wsgi:application --bind 0.0.0.0:$PORT
