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
    python3

# Configure Python/pip
RUN ln -sf python3 /usr/bin/python \
    && python3 -m ensurepip \
    && pip3 install --no-cache --upgrade pip setuptools minify-html

# Copy blog script and configs
COPY ./mublog.py ./mublog.py
COPY ./mublog.ini ./mublog.ini

# Copy blog data
COPY ./src ./src

# Execute blog generation
RUN python3 mublog.py

# Set workdir to the generated blog folder
WORKDIR /app/dst

# run the folder as a small webserver
EXPOSE 8000 8000
ENTRYPOINT ["python", "-m", "http.server", "8000"]