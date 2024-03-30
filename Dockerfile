FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o código fonte para o diretório de trabalho
COPY main.py /app/main.py

# Instala o Flask
RUN pip install flask

# Expõe a porta 8000 para o mundo exterior
EXPOSE 8000

# Comando para executar o servidor quando o contêiner for iniciado
CMD ["python", "main.py"]
