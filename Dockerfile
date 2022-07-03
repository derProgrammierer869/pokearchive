FROM python:3.10.2-alpine
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt