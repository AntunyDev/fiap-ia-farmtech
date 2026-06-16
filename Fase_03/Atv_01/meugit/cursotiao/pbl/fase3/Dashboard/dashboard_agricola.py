import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração de layout limpo no browser
st.set_page_config(
    page_title="FarmTech - Dashboard Agrícola", layout="wide", page_icon="🌱"
)


# 1. Carregamento e Processamento Limpo dos Dados
@st.cache_data
def load_data():
    df = pd.read_csv("Dados_Clima_ESP32.csv")

    # Regra lógica condicional para Sugestão de Irrigação
    def sugerir_irrigacao(row):
        if row["umidade"] < 26.0 and row["precipitacao"] < 60:
            return "Recomendado Irrigar 💧"
        elif row["precipitacao"] >= 80:
            return "Chuva Suficiente 🌧️"
        else:
            return "Condição Adequada ✅"

    df["sugestao_irrigacao"] = df.apply(sugerir_irrigacao, axis=1)
    df["leitura_id"] = df.index + 1
    return df


df = load_data()

# 2. Cabeçalho Minimalista
st.title("🌱 FarmTech — Dashboard Agrícola")
st.subheader("Visualização em tempo real de sensores de Solo, Clima e Irrigação.")

st.divider()

# 3. Métricas Principais (Overview dos números de forma limpa)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Umidade Média do Solo", f"{df['umidade'].mean():.1f} %")
col2.metric("pH Médio do Solo", f"{df['ph'].mean():.2f}")
col3.metric("Precipitação Média", f"{df['precipitacao'].mean():.1f} mm")
irrigados = df["irrigacao"].sum()
col4.metric("Status Irrigação (Ativas)", f"{irrigados} de {len(df)}")

st.divider()

# 4. Gráficos de Linha 1 (Umidade e pH)
st.subheader("📈 Níveis de Umidade e pH do Solo")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    fig_umidade = px.line(
        df,
        x="leitura_id",
        y="umidade",
        title="Variação de Umidade (%)",
        labels={"leitura_id": "ID de Leitura", "umidade": "Umidade (%)"},
        template="plotly_dark",
    )
    # Adicionando uma linha de limite crítico de seca
    fig_umidade.add_hline(
        y=25.0, line_dash="dot", line_color="red", annotation_text="Limite Crítico"
    )
    st.plotly_chart(fig_umidade, use_container_width=True)

with col_graf2:
    fig_ph = px.scatter(
        df,
        x="leitura_id",
        y="ph",
        color="ph",
        color_continuous_scale="Viridis",
        title="Distribuição do pH",
        labels={"leitura_id": "ID de Leitura", "ph": "Valor de pH"},
        template="plotly_dark",
    )
    st.plotly_chart(fig_ph, use_container_width=True)

st.divider()

# 5. Gráficos de Linha 2 (Nutrientes e Irrigação)
st.subheader("🧪 Presença de Nutrientes (N, P, K) e Status de Irrigação")
col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    # Preparação de dados de NPK para o gráfico de barras
    nutrientes = pd.DataFrame(
        {
            "Nutriente": ["Nitrogênio (N)", "Fósforo (P)", "Potássio (K)"],
            "Detecções Positivas": [df["n"].sum(), df["p"].sum(), df["k"].sum()],
        }
    )
    fig_nutrientes = px.bar(
        nutrientes,
        x="Nutriente",
        y="Detecções Positivas",
        color="Nutriente",
        title="Contagem de Presença de Nitrogênio (N), Fósforo (P) e Potássio (K)",
        template="plotly_dark",
    )
    st.plotly_chart(fig_nutrientes, use_container_width=True)

with col_graf4:
    fig_irrigacao = px.pie(
        df,
        names="irrigacao",
        title="Proporção do Histórico de Irrigação",
        color_discrete_sequence=["#4C78A8", "#E45756"],
        template="plotly_dark",
    )
    st.plotly_chart(fig_irrigacao, use_container_width=True)

st.divider()

# 6. Tabela Dinâmica com Filtro Interativo
st.subheader("🌦️ Recomendações de Irrigação Baseadas em Clima")
st.markdown(
    "A regra lógica abaixo cruza a umidade do solo e a precipitação para sugerir a ativação das bombas:"
)
st.markdown("* *Regra: Irrigar se Umidade < 26% E Precipitação < 60mm.*")

# Filtro interativo simples
filtro_sugestao = st.radio(
    "Filtrar tabela por recomendação:",
    ["Todos"] + list(df["sugestao_irrigacao"].unique()),
    horizontal=True,
)


if filtro_sugestao != "Todos":
    df_filtrado = df[df["sugestao_irrigacao"] == filtro_sugestao]
else:
    df_filtrado = df

# Exibição de colunas limpas na tabela
colunas_exibicao = [
    "leitura_id",
    "umidade",
    "ph",
    "precipitacao",
    "irrigacao",
    "sugestao_irrigacao",
]
colunas_amigaveis = {
    "leitura_id": "ID Leitura",
    "umidade": "Umidade (%)",
    "ph": "pH do Solo",
    "precipitacao": "Precipitação (mm)",
    "irrigacao": "Bomba Ligada?",
    "sugestao_irrigacao": "Sugestão / Status",
}

df_tabela = df_filtrado[colunas_exibicao].rename(columns=colunas_amigaveis)
st.dataframe(df_tabela, use_container_width=True, hide_index=True)
