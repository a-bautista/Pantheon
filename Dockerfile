# Base Image
FROM python:3.6.9

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
# $PORT is set by Heroku
ENV PORT=8888

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# EXPOSE 8888
CMD gunicorn madlibs.wsgi:application --bind 0.0.0.0:$PORT
