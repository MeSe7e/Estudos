# Baseado no vídeo do youtube de FutPythonTrader "tutorial de criacao de um web app de football data utilizando python"

# Import das Bibliotecas
import streamlit as st
import pandas as pd
import numpy as np

# Criar título para a nossa App
st.title("Web App Football Data")

# Criar a barra lateral
st. sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League', ['England', 'Germany', 'Italy', 'Spain', 'France'])

st. sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season', ['2022/2021', '2021/2020', '2020/2019'])

# Webscrapping Football Data
## Criar função para obter a Liga e a Temporada de acordo com o que nós selecionarmos
def load_data(league, season):
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selectd_season) 

# Para ver como está o nosso dashboard
## 1. Salvar o nosso dashboard -> "Commit changeg"
## 2. Para testar precisamos de criar um novo arquivo dentro desta pasta, com o nome requeriments.txt
## 3. Dentro do arquivo temos de colocar as bibliotecas que necessitamos que sejam instaladas
## 4. Ir para o site do streamlit -> "streamlit.io"
## 5. Fazer login com a conta do Gitub

