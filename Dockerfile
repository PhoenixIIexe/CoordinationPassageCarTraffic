FROM python:3.11

WORKDIR /opt/app/


COPY requirements.txt ./

RUN apt-get update

RUN  pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 5000
# run app
CMD ["python", "app.py"]