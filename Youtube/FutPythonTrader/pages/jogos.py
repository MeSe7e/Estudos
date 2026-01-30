# Importar as bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

# Título da página
st.title("Jogos do Dia")

# Para escolher o dia que queremos ver dos jogos do dia
dia = st.date_input(
    "Data de Análise",
    date.today())

# Criar a função que vai ao Github buscar o arquivo que tem os jogos da data selecionada, esta função só carrega os jogos, depois temos de pedir para imprimir no ecrã
## escolhemos em csv porque é mais rápido de ler, numa app dinâmica é melhor
def load_data_jogos():
    data_jogos = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/" + str(dia) + "_Jogos_do_Dia_FlashScore.csv?raw=true") # ?raw=true, porque é um arquivo que está no github
    return data_jogos

df_jogos = load_data_jogos()

st.dataframe(df_jogos)
