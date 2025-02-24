import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Carrega o DataFrame
@st.cache_data #cache data to improve performance
def load_data():
    return pd.read_csv('NorthAmericaUniversities_limpo.csv')

df = load_data()

# Inicializa st.session_state (mantido e organizado)
# O st.session_state é usado para manter o estado do aplicativo entre as execuções.
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Tabela Interativa'  # Página inicial
if 'country' not in st.session_state:
    st.session_state.country = 'All'  # País inicial (todos)
if 'students_min' not in st.session_state:
    st.session_state.students_min = int(df['Number of Students'].min())  # Número mínimo de alunos
if 'students_max' not in st.session_state:
    st.session_state.students_max = int(df['Number of Students'].max())  # Número máximo de alunos
if 'tuition_min' not in st.session_state:
    st.session_state.tuition_min = int(df['Minimum Tuition cost'].min())  # Custo mínimo da mensalidade
if 'tuition_max' not in st.session_state:
    st.session_state.tuition_max = int(df['Minimum Tuition cost'].max())  # Custo máximo da mensalidade

# Título do dashboard
st.title('Análise das Universidades do Estados Unidos e Canadá')

# Sidebar com filtros e botões (organizado)
with st.sidebar:
    st.title('Filtros')

    col1, col2, = st.columns(2)  # Divide a sidebar em duas colunas

    if col1.button('Tabela 📊'):
        st.session_state.current_page = 'Tabela Interativa'  # Botão para a tabela
    if col2.button('Gráficos 📈'):
        st.session_state.current_page = 'Gráficos'  # Botão para os gráficos

    country_options = ['All'] + list(df['Country'].unique())  # Opções de país
    st.session_state.country = st.selectbox('País', country_options)  # Seleção de país

    # Sliders para número de alunos e custo da mensalidade
    st.session_state.students_min, st.session_state.students_max = st.slider(
        'Número de Alunos',
        min_value=int(df['Number of Students'].min()),
        max_value=int(df['Number of Students'].max()),
        value=(int(df['Number of Students'].min()), int(df['Number of Students'].max()))
    )

    st.session_state.tuition_min, st.session_state.tuition_max = st.slider(
        'Custo da Mensalidade',
        min_value=int(df['Minimum Tuition cost'].min()),
        max_value=int(df['Minimum Tuition cost'].max()),
        value=(int(df['Minimum Tuition cost'].min()), int(df['Minimum Tuition cost'].max()))
    )


# Função para aplicar filtros
def apply_filters(dataframe):
    """Aplica filtros ao DataFrame com base no estado da sessão."""
    if st.session_state.country != 'All':
        dataframe = dataframe[dataframe['Country'] == st.session_state.country]  # Filtra por país
    dataframe = dataframe[
        (dataframe['Number of Students'] >= st.session_state.students_min) &  # Filtra por número de alunos
        (dataframe['Number of Students'] <= st.session_state.students_max) &
        (dataframe['Minimum Tuition cost'] >= st.session_state.tuition_min) &  # Filtra por custo da mensalidade
        (dataframe['Minimum Tuition cost'] <= st.session_state.tuition_max)
    ]
    return dataframe


# Função para criar o gráfico de custo de mensalidade por universidade
def create_tuition_bar_chart(df_filtered):
    fig_tuition = px.bar(df_filtered, x='Name', y='Minimum Tuition cost', title='Custo de Mensalidade por Universidade')
    return fig_tuition

# Função para criar o gráfico de relação aluno/professor
def create_students_teachers_scatter_chart(df_filtered):
    fig_students_teachers = px.scatter(df_filtered, x='Number of Students', y='Academic Staff', title='Relação entre Número de Alunos e Corpo Docente')
    return fig_students_teachers

# Função para criar o gráfico de tamanho da universidade por década
def create_decade_product_line_chart(df_filtered):
    df_filtered['Established'] = pd.to_numeric(df_filtered['Established'], errors='coerce')
    df_filtered['Product'] = df_filtered['Number of Students'] * df_filtered['Minimum Tuition cost']
    decade_product = df_filtered.groupby('Established').agg({'Product': 'mean'}).reset_index()
    decade_product = decade_product.sort_values('Established')
    decade_product = pd.merge(decade_product, df_filtered[['Established', 'Rank']], on='Established', how='left')
    fig_decade_product = px.line(decade_product, x='Established', y='Product',
                                 hover_data={'Rank': True, 'Established': True, 'Product': True},
                                 title='Tamanho da Universidade (Alunos x Custo) por Década de Fundação (com Ranking)')
    return fig_decade_product

# Função do 4 with/ grafico
# Filtra os dados
def create_compare_top_10_bar_chart(df_filtered):
    """Compara as top 10 universidades dos EUA e do Canadá usando df_filtered."""

    # Filtra as top 10 universidades dos EUA
    df_usa = df_filtered[df_filtered['Country'] == 'us'].sort_values('Rank').head(10)

    # Filtra as top 10 universidades do Canadá
    df_canada = df_filtered[df_filtered['Country'] == 'ca'].sort_values('Rank').head(10)

    # Combina os DataFrames
    df_top10 = pd.concat([df_usa, df_canada])

    # Prepara os dados para o gráfico
    df_top10['Product'] = df_top10['Number of Students'] * df_top10['Minimum Tuition cost']

    fig = px.bar(
        df_top10,
        x='Name',
        y='Product',
        hover_data=['Rank', 'Established', 'Product', 'Academic Staff'],
        color='Country',
        barmode='group',
        title='Comparação das Top 10 Universidades nos EUA e Canadá',
        labels={
            'Rank': 'Ranking',
            'Name': 'Universidade',
            'Established': 'Fundação',
            'Product': 'Alunos x Custo',
            'Academic Staff': 'Corpo Docente',
        },
    )
    return fig

# Conteúdo principal
if st.session_state.current_page == 'Tabela Interativa':
    st.title('Tabela Interativa')
    df_filtered = apply_filters(df.copy())  # Aplica os filtros
    # Formata a exibição das colunas numéricas
    numeric_cols = ['Number of Students', 'Minimum Tuition cost', 'Endowment']
    df_display = df_filtered.copy()
    for col in numeric_cols:
        if col in df_display.columns:
            df_display[col] = df_display[col].apply(lambda x: '{:.2f}'.format(x) if pd.notnull(x) else x)
    st.dataframe(df_display.style.format(thousands=".", decimal=","))  # Exibe a tabela formatada

elif st.session_state.current_page == 'Gráficos':
    st.title('Gráficos')
    df_filtered = apply_filters(df.copy())  # Aplica os filtros

    # Layout dos gráficos
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.plotly_chart(create_tuition_bar_chart(df_filtered))

    with col2:
        st.plotly_chart(create_students_teachers_scatter_chart(df_filtered))

    with col3:
        st.plotly_chart(create_decade_product_line_chart(df_filtered))

    with col4: 
        st.plotly_chart(create_compare_top_10_bar_chart(df_filtered))
      







