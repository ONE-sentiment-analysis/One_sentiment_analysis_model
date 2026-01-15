FROM python:3.13.11-trixie

WORKDIR /app

# Instala dependências de sistema necessárias para pacotes como scikit-learn
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Baixa as stopwords do NLTK
RUN python -m nltk.downloader stopwords

# Copia os diretórios (usando a estrutura do seu repo)
COPY src/One_sentiment_API/ ./api/
COPY src/models/ ./models/

# Define o caminho de busca do Python
ENV PYTHONPATH=/app

EXPOSE 8585

CMD ["python", "api/main.py"]