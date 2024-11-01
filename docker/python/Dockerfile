FROM python:3.14-rc-alpine
ENV TZ Asia/Tokyo

WORKDIR /src
COPY requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /src/worksample
CMD python3 manage.py runserver 0.0.0.0:8000