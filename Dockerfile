# Use a imagem oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY . .

# Cria um ambiente virtual
RUN python -m venv /venv

# Ativa o ambiente virtual
SHELL ["/bin/bash", "-c"]
RUN source /venv/bin/activate

# Atualiza o pip dentro do ambiente virtual
RUN pip install --upgrade pip

# Instala as dependências do Flask
RUN pip install flask

# Expõe a porta 8000
EXPOSE 8000

# Define o comando padrão para executar a aplicação
CMD ["python", "main.py"]
