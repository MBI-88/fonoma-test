FROM python:3.11
WORKDIR /app
COPY requirements.txt /app
RUN apt-get update && apt-get install -y 
RUN apt-get install redis-server -y
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
EXPOSE 80
COPY ./ /app
CMD ["python","main.py"]