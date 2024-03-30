FROM python:3.9-slim

WORKDIR /app

COPY tcp_server.py .

CMD ["python", "tcp_server.py"]
