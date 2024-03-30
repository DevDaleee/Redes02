FROM python:3.9-slim

WORKDIR /app

COPY tcp_client.py .

CMD ["python", "tcp_client.py"]
