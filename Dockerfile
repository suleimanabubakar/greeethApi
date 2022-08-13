FROM python:3

ENV PYTHONNONBUFFERED=1

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python3-gdal

COPY ./requirements.txt requirements.txt


RUN pip install -r requirements.txt


EXPOSE 8000

COPY . /usr/src/app



# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "greeeth.wsgi"]