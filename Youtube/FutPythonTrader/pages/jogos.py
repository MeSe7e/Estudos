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
