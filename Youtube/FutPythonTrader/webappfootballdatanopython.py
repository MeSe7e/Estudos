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
selected_season = st.sidebar.selectbox('Season', ['2021/2022', '2020/2021', '2019/2020'])

# Webscrapping Football Data
## Criar função para obter a Liga e a Temporada de acordo com o que nós selecionarmos
def load_data(league, season):
  # Converter o nome que se escolhe na app para a liga, no que equivale no football data a essa liga
  if selected_league == 'England' :
    league = 'E0'
  if selected_league == 'Germany' :
    league = 'D1'
  if selected_league == 'Italy' :
    league = 'I1'
  if selected_league == 'Spain' :
    league = 'SP1'
  if selected_league == 'France' :
    league = 'F1'
  # Converter a season que se escolhe na app para a liga, no que equivale no football data a essa season
  if selected_season == '2021/2022' :
    season = '2122'
  if selected_season == '2020/2021' :
    season = '2021'
  if selected_season == '2019/2020' :
    season = '1920'
   
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season) 

# Para ver como está o nosso dashboard
## 1. Salvar o nosso dashboard -> "Commit changeg"
## 2. Para testar precisamos de criar um novo arquivo dentro desta pasta, com o nome requeriments.txt
## 3. Dentro do arquivo temos de colocar as bibliotecas que necessitamos que sejam instaladas
## 4. Ir para o site do streamlit -> "streamlit.io"
## 5. Fazer login com a conta do Github
## 6. Crate app
## 7. Deploy a public app from Github
## 8. Past Github URL - basta abrir o código no Github e copiar o link que está na barra de address "https://github.com/MeSe7e/Estudos/blob/main/Youtube/FutPythonTrader/webappfootballdatanopython.py"

st.subheader('Dataframe: '+selected_league)
st.dataframe(df)
