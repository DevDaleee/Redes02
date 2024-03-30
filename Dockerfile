FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o código fonte para o diretório de trabalho
COPY main.py /app/main.py

# Cria e ativa o ambiente virtual
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Instala o Flask dentro do ambiente virtual
RUN pip install math

# Expõe a porta 8000 para o mundo exterior
EXPOSE 8000

# Comando para executar o servidor quando o contêiner for iniciado
CMD ["python", "main.py"]
