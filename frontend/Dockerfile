FROM python:3.10-slim

COPY ./app.py /frontend/

COPY ./formatter.py /frontend/

ADD static /frontend/static/

ADD templates /frontend/templates/

COPY requirements.txt /frontend/

WORKDIR /frontend

RUN pip install -r requirements.txt

EXPOSE 5001

WORKDIR /frontend

CMD ["python3", "app.py"]