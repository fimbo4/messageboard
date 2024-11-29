FROM python:3.10-slim

COPY ./api.py /api/

COPY ./db.py /api/

COPY requirements.txt /api/

WORKDIR /api

RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["python3", "api.py"]