# syntax=docker/dockerfile:1
FROM python:3.8-alpine

RUN mkdir "smartcar"
COPY . /smartcar
WORKDIR /smartcar

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -v -r requirements.txt

RUN rm requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]