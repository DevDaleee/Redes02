FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalação do Flask
RUN pip install flask

# Copia o código fonte para o diretório de trabalho
COPY main.py /app/main.py

# Expõe a porta 8000 para o mundo exterior
EXPOSE 8000

# Comando para executar o servidor quando o contêiner for iniciado
CMD ["python", "main.py"]
