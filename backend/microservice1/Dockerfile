FROM python:3.10-slim

COPY ./ms1.py /microservice1/

COPY ./requirements.txt /microservice1/

WORKDIR /microservice1

RUN pip install -r requirements.txt

EXPOSE 1313

CMD ["python3", "ms1.py"]

