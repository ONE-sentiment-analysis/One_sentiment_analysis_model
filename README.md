# One_sentiment_analysis_model
This repo is dedicated to host all files related to the training and use of our ML model.

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


# Como este repositorio esta organizado
```
.
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── data
    │   └── NoThemeTweets.csv
    ├── environment.yml
    ├── models
    │   ├── dtrUCV_model.pkl
    │   ├── dtrUIDF_model.pkl
    │   ├── mnbUCV_model.pkl
    │   ├── rfcUCV_model.pkl
    │   └── rfcUIDF_model.pkl
    ├── notebooks
    │   └── 00_One_sentiment_analysis_model.ipynb
    ├── One_sentiment_analysis_model
    └── scripts
        └── string_analysis.py
```

Os arquivos relacionados ao projeto em si estao organizados na pasat `src`, arquivos de documentacao e adjacentes devem estar em um nivel acime fora da do diretorio `src`.

#### .src/notebooks
Neste diretorio estao os notebooks utilizados para tratar os dados(ETL) e treinar o nosso modelo.

#### .src/data
Este diretorio contem os arquivos fontes (datasets) utilizados no treinamento do modelo.

-**[IMPORTANT]** *este diretorio esta exluido do versionamento pelo `.gitignore` pois os aruivos raw do dataset sao muito grandes para serem salvos no github. Voce deve baixar o dataset direto do [kaggle](https://www.kaggle.com/datasets/augustop/portuguese-tweets-for-sentiment-analysis/data) e extrair o dataset `NoThemeTweets.csv` neste diretorio.

#### .src/models
Este diretorio contem os arquivos serializados resultado do treinamento dos modelos.

#### .src/scripts
Este diretorio contem qualquer scripts utilizados no projeto.

#### .src/One_sentiment_analysis_model
Este diretorio é o diretorio `main` do projeto, onde deve estar os arquivos principais do projeto que utilizarao o modelo treinado.

---
# TO-DO

* Notebook (Jupyter/Colab) do time de Data Science contendo:
 
* Exploração e limpeza dos dados (EDA);
 
* ~~Transformação dos textos em números com TF-IDF;~~
 
* ~~Treinamento de modelo supervisionado (ex.: Logistic Regression, Naive Bayes);~~
 
* Métricas de desempenho (Acurácia, Precisão, Recall, F1-score);

* ~~Serialização do modelo (joblib/pickle).~~

#### Time de Data Science

Cada equipe deve escolher ou montar seu próprio conjunto de dados de comentários, avaliações ou postagens que possam ser usados para análise de sentimento (ex.: reviews públicos, tweets, avaliações de produtos etc.).

* use Python, Pandas para ler/limpar dados;

* crie um modelo simples (TF-IDF + LogisticRegression do scikit-learn);

* salve o pipeline e o modelo com joblib.dump.

* Coloque tudo em um notebook bem comentado.

#### Contrato de integração (definido entre DS e BE)

Recomendamos definir desde o início o formato JSON de entrada e saída. Segue um exemplo:

```
{"text": "…"} →

{

"previsao":"Positivo",

"probabilidade":0.9

} 
```

---

Para referencia de que padrao este repositorio segue veja aqui: [How to organize your Python data science project](https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510)