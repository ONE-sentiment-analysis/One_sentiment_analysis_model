import argparse
import re
import nltk
import logging
from pathlib import Path
from nltk.corpus import stopwords
from joblib import load
import sys

# configuracao de caminhos com pathlib
BASE_DIR = Path(__file__).parent.parent.parent # vai para /src
MODELS_DIR = BASE_DIR / "models"
LOGS_DIR = BASE_DIR / "logs"

# criar a pasta de logs caso ela nao exista
LOGS_DIR.mkdir(exist_ok=True)

# configuracao do logging
logging.basicConfig(
    filename=LOGS_DIR / "execucao_API.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - Modelo: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# configuracao NLTK
nltk.download('stopwords', quiet=True)
stops = set(stopwords.words('portuguese'))

def limpar_texto(texto: str) -> str:
    texto = str(texto).lower()
    texto = re.sub(r'[^a-zA-Záéíóúàèìòùâêîôûãõç\s]', '', texto)
    texto = ' '.join([palavra for palavra in texto.split() if palavra not in stops])
    return texto

def carregar_recursos(nome_modelo: str) -> tuple:
    try:
        modelos_disponiveis = {
            'nb': 'modelo_naive_bayes.joblib',
            'lr': 'modelo_logistic_regression.joblib',
            'rf': 'modelo_random_forest.joblib'
        }
        
        caminho_modelo = MODELS_DIR / modelos_disponiveis[nome_modelo]
        caminho_vetorizador = MODELS_DIR / 'vectorizer_tfidf.joblib'

        return load(caminho_modelo), load(caminho_vetorizador)
    except Exception as e:
        logging.error(f"Erro ao carregar recursos: {e}")
        print(f"Erro crítico: Verifique os logs em {LOGS_DIR}")
        sys.exit(1)

def main(text: str, model: str) -> tuple:
    
    modelo, vectorizer = carregar_recursos(model)
    
    texto_limpo = limpar_texto(text)
    vetorizado = vectorizer.transform([texto_limpo])
    
    predicao = modelo.predict(vetorizado)[0]
    probabilidade = modelo.predict_proba(vetorizado).max()

    # logando a execucao
    log_msg = f"{model.upper()} | Texto: '{text}' | Predição: {predicao} | Confiança: {probabilidade:.2%}"
    logging.info(log_msg)

    # output para o usuario
    print(f"\nResultado ({model.upper()}): {predicao} ({probabilidade:.2%})")
    return predicao, probabilidade


if __name__ == "__main__":
    main()