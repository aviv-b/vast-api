FROM python:3.9

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install -r /code/requirements.txt

EXPOSE 8000

COPY ./src /code/src

