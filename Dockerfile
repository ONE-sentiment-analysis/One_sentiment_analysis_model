# Imagem base oficial do Python
FROM python:3.9-slim

# Definir diretório de trabalho no container
WORKDIR /app

# Instalar dependências
# Certifique-se de que o requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baixar recursos do NLTK (necessário para a limpeza de texto)
RUN python -m nltk.downloader stopwords

# Copiar as pastas necessárias
# Copiamos a pasta da API e a pasta de modelos para o container
COPY src/One_sentiment_API/ ./api/
COPY src/models/ ./models/

# Variável de ambiente para ajudar a API a localizar os modelos
ENV PYTHONPATH=/app

# Expor a porta que a API utiliza (ex: 5000 para Flask)
EXPOSE 8585

# Comando para rodar a API
CMD ["python", "api/main.py"]