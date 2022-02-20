FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY src /app

CMD ["python", "main.py"]
