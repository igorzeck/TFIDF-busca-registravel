import nltk
import glob
import pandas as pd
import numpy as np
# from collections import Counter
# from itertools import chain
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('stopwords')  # Não baixa se já estiver atualizado!
from nltk.corpus import stopwords
from os.path import normpath

#
# Variáveis globais
#
df_metadatasets = pd.DataFrame()  # Acesso aberto a todos arquivos
df_cache = pd.DataFrame()  # Cache de acesso aberto a todos arquivos
# imps.default_params["IdDataSetDefault"] sempre 0
default_params = pd.DataFrame([{"Idioma_padrao": "portuguese",
                                "IdDataSetDefault": 0,
                                "Modo": "Sci-kit"}])

# De estilo
styles = ""
with open(normpath("res/styles.css"), "r", encoding="utf-8") as arq:
    styles = arq.read()


# Salva o estado do metadataset atual
def save_mdt(df_mdt: pd.DataFrame):
    df_mdt.to_csv("save_state/save_principal", index=False)


def _read_params():
    if 'params.json' in glob.glob(""):
        return pd.read_json('params.json')
    else:
        _save_params()


def _save_params(dt_params: pd.DataFrame = default_params):
    dt_params.to_json('params.json')


# Carrega o estado do metadataset atual
def load_mdt(arq = 'save_principal'):
    if normpath('save_state/' + arq) in glob.glob(f"save_state/*"):
        return pd.read_csv(f"save_state/{arq}")
    else:
        print(f"Não há arquivo '{arq}' no diretório 'save_state'")
        return pd.DataFrame()

#
# Vê se tem save para carregar
#
if normpath('save_state/save_principal') in glob.glob("save_state/*"):
    df_metadatasets = load_mdt()
