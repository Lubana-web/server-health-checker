FROM python:3.12

WORKDIR /app

COPY . .

CMD ["python", "health_monitor.py"]
