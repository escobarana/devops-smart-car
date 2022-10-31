FROM python:3.8.1

COPY ./smart_carapi ./smartcar

WORKDIR /smartcar

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -v -r requirements.txt

RUN rm requirements.txt

CMD ["python", "flask_app.py"]