# syntax=docker/dockerfile:1

FROM amd64/alpine:latest
WORKDIR /app

# Labels for the image
LABEL source="mublog"
LABEL mublog.author "766F6964"
LABEL blog.url "https://zeh-almeida.olamundo.org/"
LABEL maintainer='Zeh Almeida <zeca_16@hotmail.com>'

# Environment Variables
ENV PYTHONUNBUFFERED=1

# Install all necessary packages
RUN apk add --update --no-cache \
    pandoc \
    python3 \
    7zip

# Configure Python/pip
RUN ln -sf python3 /usr/bin/python \
    && python3 -m ensurepip \
    && pip3 install --no-cache --upgrade pip setuptools

# Copy blog script
COPY ./mublog.py ./mublog.py

# Copy blog data
COPY ./src ./src

# Execute blog generation
RUN python3 mublog.py

# zip blog generated data for output
RUN 7z a build ./dst/*