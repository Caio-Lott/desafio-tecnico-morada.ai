import streamlit as st
import pandas as pd
import json

# Função para carregar os dados JSON
def carregar_dados(caminho_json):
    with open(caminho_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return pd.DataFrame(dados)

# Caminho para o arquivo JSON de resultados
caminho_json = 'results/resultados.json'

# Carrega os dados
try:
    df = carregar_dados(caminho_json)
except FileNotFoundError:
    st.error("Arquivo resultados.json não encontrado. Execute o script principal primeiro.")
    st.stop()

# Título da aplicação
st.title("Análise de Leads Imobiliários")

# Exibe os dados brutos
st.subheader("Dados Brutos")
st.dataframe(df)

# Análises e Insights
st.subheader("Análises e Insights")

# 1. Distribuição de Tipos de Imóveis
st.write("### Distribuição de Tipos de Imóveis")
tipo_imovel_counts = df['tipo_imovel'].value_counts()
st.bar_chart(tipo_imovel_counts)

# 2. Distribuição de Cidades
st.write("### Distribuição de Cidades")
cidade_counts = df['cidade'].value_counts()
st.bar_chart(cidade_counts)

# 3. Orçamento Médio por Tipo de Imóvel
st.write("### Orçamento Médio por Tipo de Imóvel")
orcamento_medio = df.groupby('tipo_imovel')['orcamento'].mean()
st.bar_chart(orcamento_medio)

# 4. Interesses por Região
st.write("### Interesses por Região")
regiao_counts = df['regiao'].value_counts()
st.bar_chart(regiao_counts)

# 5. Intenções dos Leads
st.write("### Intenções dos Leads")
intencao_counts = df['intencao'].value_counts()
st.bar_chart(intencao_counts)

# 6. Características Adicionais Mais Comuns
st.write("### Características Adicionais Mais Comuns")
caracteristicas = df['caracteristicas'].dropna().str.split(', ', expand=True).stack()
caracteristicas_counts = caracteristicas.value_counts()
st.bar_chart(caracteristicas_counts)

# 7. Disponibilidade de Visita
st.write("### Disponibilidade de Visita")
disponibilidade_counts = df['disponibilidade'].value_counts()
st.bar_chart(disponibilidade_counts)

# 8. Número de Quartos
st.write("### Distribuição de Número de Quartos")
quartos_counts = df['quartos'].value_counts()
st.bar_chart(quartos_counts)