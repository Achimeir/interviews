FROM python:alpine3.7
COPY ./lets_run /app/lets_run
COPY ./requirements.txt /app
WORKDIR /app
EXPOSE 8080
RUN apk add -U g++ gcc
RUN pip install -r requirements.txt
ENV FLASK_APP=lets_run
RUN flask init-db
CMD waitress-serve --call lets_run:create_app