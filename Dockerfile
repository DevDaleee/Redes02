# Usa uma imagem base Python
FROM python:3.9-slim

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia os arquivos do diretório atual para o diretório de trabalho do contêiner
COPY . .

# Instala as dependências
RUN pip install flask

# Expõe a porta 8000 para que o contêiner possa ser acessado externamente
EXPOSE 8000

# Comando para executar o aplicativo Flask quando o contêiner for iniciado
CMD ["python", "main.py"]
