# syntax=docker/dockerfile:1

####################################################################################################
# Base image for running the blog script
FROM python:3-alpine AS base-image
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
    npm

# Install Terser for minification
RUN npm install terser clean-css-cli -g

####################################################################################################
# Execute the blog generation
FROM base-image AS builder
WORKDIR /app

# Labels for the image
LABEL source="mublog"
LABEL mublog.author "766F6964"
LABEL blog.url "https://zeh-almeida.olamundo.org/"
LABEL maintainer='Zeh Almeida <zeca_16@hotmail.com>'

# Copy blog script and configs
COPY ./mublog.py ./mublog.py
COPY ./mublog.ini ./mublog.ini

# Copy blog data
COPY ./src ./src

# Execute blog generation
RUN python3 mublog.py

# Execute the minifications
WORKDIR /app/dst
RUN terser js/darkmode.js -c ecma=6,drop_console=true,passes=3 -m -o js/darkmode.js
RUN terser js/tags.js -c ecma=6,drop_console=true,passes=3 -m -o js/tags.js
RUN cleancss -O2 --batch --batch-suffix '' css/*.css

####################################################################################################
# run the folder as a small webserver
FROM python:3-alpine AS server

# Labels for the image
LABEL source="mublog"
LABEL mublog.author "766F6964"
LABEL blog.url "https://zeh-almeida.olamundo.org/"
LABEL maintainer='Zeh Almeida <zeca_16@hotmail.com>'

COPY --from=builder /app/dst /app
WORKDIR /app

EXPOSE 8000 8000
ENTRYPOINT ["python", "-m", "http.server", "8000"]