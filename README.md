![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Neovim](https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)


# One_sentiment_analysis_model
This repo is dedicated to host all files related to the training and use of our ML model.

# Como este repositorio esta organizado
```
.
├── LICENSE
├── logs
│   └── execucao.log
├── README.md
├── requirements.txt
└── src
    ├── data
    │   └── olist_order_reviews_dataset.csv
    ├── environment.yml
    ├── logs
    │   ├── execucao_API.log
    │   └── execucao.log
    ├── models
    │   ├── modelo_logistic_regression.joblib
    │   ├── modelo_naive_bayes.joblib
    │   ├── modelo_random_forest.joblib
    │   ├── vectorizer.joblib
    │   └── vectorizer_tfidf.joblib
    ├── notebooks
    │   └── 00_One_sentiment_analysis_model.ipynb
    ├── One_sentiment_API
    │   ├── app
    │   │   ├── app.py
    │   │   ├── predict.py
    │   │   ├── __pycache__
    │   │   │   ├── app.cpython-313.pyc
    │   │   │   ├── predict.cpython-313.pyc
    │   │   │   └── schemas.cpython-313.pyc
    │   │   └── schemas.py
    │   ├── main.py
    │   └── __pycache__
    │       └── main.cpython-313.pyc
    ├── resources
    │   └── img
    │       ├── .
    │       ├── .
    │       └── .
    └── scripts
        └── classificador.py

```

Os arquivos relacionados ao projeto em si estao organizados na pasat `src`, arquivos de documentacao e adjacentes devem estar em um nivel acime fora da do diretorio `src`.

#### .src/notebooks
Neste diretorio estao os notebooks utilizados para tratar os dados(ETL) e treinar o nosso modelo.

#### .src/data
Este diretorio contem os arquivos fontes (datasets) utilizados no treinamento do modelo.

-**[IMPORTANT]** *este diretorio esta exluido do versionamento pelo `.gitignore` pois os aruivos raw do dataset sao muito grandes para serem salvos no github. Voce deve baixar o dataset direto do kaggle na seguinte URL: [https://www.kaggle.com/api/v1/datasets/download/olistbr/brazilian-ecommerce](https://www.kaggle.com/api/v1/datasets/download/olistbr/brazilian-ecommerce).

Apos o download extraia o arquivo `.zip` e coloque o arquivo `olist_order_reviews_dataset.csv` no diretorio `src/data` deste projeto.

O caminho do final do arquivo ficara assim:

```
src/data/olist_order_reviews_dataset.csv
```

#### .src/models
Este diretorio contem os arquivos serializados resultado do treinamento dos modelos.

#### .src/scripts
Este diretorio contem qualquer scripts utilizados no projeto.

#### .src/One_sentiment_API
Este diretorio contem o backend FastAPI para fazer integracao com o backend Java.

# Como inicializar o projeto
Este projeto foi criado usando variaveis de ambiente virtual python, voce deve criar o seu `.venv` e instalar as dependencias necessárias para poder executar este projeto.

### Criar um ambiente virtual python
Na raiz do projeto execute:

```
python3 -m venv venv
```

### Ativar o ambiente virtual
Na raiz do projeto execute:

```
source .venv/bin/activate
```

### Instalar as dependencias do projeto
Na raiz do projeto execute:
```
pip3 install -r requirements.txt
```

### Desativar o ambiente virtual
Na raiz do projeto execute:

```
deactivate
```

# API Python - FastAPI

### Como executar a API com Docker (Recomendado)
Se for a primeira vez, primeiro construa a imagem docker. Na raiz deste projeto execute:

```
docker build -t analisador-sentimento .
```

Agora voce pode executar a imagem com:

```
docker run -p 8585:8585 analisador-sentimento
```

A API estara ouvindo na porta `8585` por padrao.

### Como executar a API Manualmente
O diretorio raiz da api se encontra em `/src/One_sentiment_API`. Navegue até este diretorio e execute o seguinte comando para iniciar a API:

```
python3 main.py
```

## Porta
Por padrao a API esta configurada para ouvir chamadas na porta `8585`.

Se desejar alterar a porta, altere o atributo `port=` no seguinte arquivo:

```
./src/One_sentiment_API/main.py
```

## Endpoints fornecidos pela API

#### /api/docs
Documentacao detalhada da API.

#### /api/models
exemplo de teste:

```
curl -i -X GET http://127.0.0.1:8585/api/models
```

##### Parameters

No parameters

##### Responses

Code|Description
:---:|:---:
200|Successful Response

##### Response Body

```
{
  "available_models": [
    "nb",
    "lr",
    "rf"
  ]
}
```

##### Response headers

```
 content-length: 109  
 content-type: application/json  
 date: Tue,13 Jan 2026 20:26:55 GMT  
 server: uvicorn 
```

#### /api/predict
exemplo de teste:

```
curl -i -X POST -H 'Content-Type: application/json' -d '{"text": "O atendimento foi nao  taobom", "model": "lr"}' http://127.0.0.1:8585/api/predict
```

##### Parameters

No parameters

##### Request body *required

##### Example value
```
{
  "text": "Lorem ipsum dolor sit amet. ",
  "model": "lr"
}
```

O campo "model" é opcional, se deixado em branco a API ira utilizar o modelo padrão(default) que é o modelo "lr" ou seja Regressão Logistica.

##### Responses
Code|Description
:---:|:---:
200|Successful Response

##### Example value
```
{
  "text": "Lorem ipsum dolor sit amet. ",
  "sentiment": "Positive",
  "model": "LogisticRegression",
  "score": 0.99
}
```

Code|Description
:---:|:---:
422|Validation Error

##### Example value
```
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

---
# TO-DO

* Notebook (Jupyter/Colab) do time de Data Science contendo:
* &#x2610; Exploração ~~e limpeza dos dados~~ (EDA);
* &#x2611; ~~Transformação dos textos em números com TF-IDF;~~
* &#x2611; ~~Treinamento de modelo supervisionado (ex.: Logistic Regression, Naive Bayes);~~
* &#x2610; Métricas de desempenho (Acurácia, Precisão, Recall, F1-score);
* &#x2611; ~~Serialização do modelo (joblib/pickle).~~

#### Time de Data Science

Cada equipe deve escolher ou montar seu próprio conjunto de dados de comentários, avaliações ou postagens que possam ser usados para análise de sentimento (ex.: reviews públicos, tweets, avaliações de produtos etc.).

- [x] use Python, Pandas para ler/limpar dados; &check;
- [x] crie um modelo simples (TF-IDF + LogisticRegression do scikit-learn); &check;
- [x] salve o pipeline e o modelo com joblib.dump. &check;
- [x] Coloque tudo em um notebook bem comentado. &check;


---

### Useful resources
- [How to organize your Python data science project](https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510)
- [Empacotando projetos Python](https://packaging.python.org/pt-br/latest/tutorials/packaging-projects/)
- [Solving “The tf-idf vectorizer is not fitted” Error: Troubleshooting Guide](https://mljourney.com/solving-the-tf-idf-vectorizer-is-not-fitted-error-troubleshooting-guide/)
- [Machine Learning 101: CountVectorizer vs TFIDFVectorizer](https://enjoymachinelearning.com/blog/countvectorizer-vs-tfidfvectorizer/)
- [TF-IDF Vectorizer vs CountVectorizer](https://mljourney.com/tf-idf-vectorizer-vs-countvectorizer/)
- [FastAPI Tutorial](https://www.geeksforgeeks.org/python/fastapi-tutorial/)
- [FastAPI documentation](https://fastapi-tutorial.readthedocs.io/en/latest/)
- [Building Web APIs with FastAPI: A Beginner's Guide](https://betterstack.com/community/guides/scaling-python/introduction-to-fastapi/)
- [Build Command-Line Interfaces With Python's argparse](https://realpython.com/command-line-interfaces-python-argparse/)
- [Saving a machine learning Model](https://www.geeksforgeeks.org/machine-learning/saving-a-machine-learning-model/)
- [What is Sentiment Analysis?](https://www.youtube.com/watch?v=5HQCNAsSO-s)
- [
Training a model to recognize sentiment in text (NLP Zero to Hero)](https://www.youtube.com/watch?v=Y_hzMnRXjhI)
