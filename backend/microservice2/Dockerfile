FROM python:3.10-slim

COPY ./ms2.py /microservice2/

COPY ./requirements.txt /microservice2/

WORKDIR /microservice2

RUN pip install -r requirements.txt

EXPOSE 1314

CMD ["python3", "ms2.py"]