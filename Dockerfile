FROM python:3.9.6
RUN apt-get update -y
WORKDIR /app
#COPY ./src /var/app/
COPY ./app/ .
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#COPY ./app/ .

WORKDIR /var/app/data_volume

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]