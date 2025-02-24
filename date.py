import pandas as pd
import numpy as np

# Carrega o DataFrame
df = pd.read_csv('NorthAmericaUniversities.csv', encoding='latin1')

# Informações iniciais e valores ausentes
df.info()  # Exibe informações sobre o DataFrame, como tipos de dados e valores não nulos
print(df)  # Imprime o DataFrame
print(df.isnull().sum())  # Imprime a contagem de valores ausentes por coluna

# Limpeza inicial (%, ",", "-")
# Substitui %, ",", e "-" por strings vazias para limpar os dados
df = df.replace('%', '', regex=True)
df = df.replace(',', '', regex=True)
df = df.replace('-', '', regex=True)

# Marca valores ausentes para universidades canadenses
# Define 'Volumes in the library' como NaN para universidades canadenses
df.loc[df['Country'] == 'ca', 'Volumes in the library'] = np.nan

# Substitui NaN por "N/D" para universidades do Canadá na coluna 'Volumes in the library'
# Preenche os valores NaN com "N/D" para indicar que não há dados disponíveis
df.loc[df['Country'] == 'ca', 'Volumes in the library'] = df.loc[df['Country'] == 'ca', 'Volumes in the library'].fillna('N/D')

# Percentual de valores ausentes (e remoção de colunas se > 50%)
# Calcula o percentual de valores ausentes por coluna
missing_percentage = (df.isnull().sum() / len(df)) * 100
# Filtra as colunas com mais de 50% de valores ausentes
missing_percentage = missing_percentage[missing_percentage > 0].sort_values(ascending=False)
print(missing_percentage)

# Remoção de linhas com valores ausentes (antes da conversão de tipos)
# Define as colunas para remover linhas com valores ausentes
colunas_para_dropna = ['Academic Staff', 'Number of Students', 'Endowment', 'Minimum Tuition cost']
# Remove as linhas com valores ausentes nas colunas especificadas
df = df.dropna(subset=colunas_para_dropna)

# Verifica valores ausentes após remoção
print(df.isnull().sum())  # Imprime a contagem de valores ausentes por coluna após a remoção

# Conversão de tipos
# Limpa a coluna 'Name', removendo aspas e caracteres especiais
df['Name'] = df['Name'].astype(str).str.replace('"', '').str.replace('ï¿½', '')
# Converte a coluna 'Country' para string
df['Country'] = df['Country'].astype(str)

# Converte colunas numéricas para o tipo Int64 (inteiro com suporte a NaN)
colunas_numericas = ['Academic Staff', 'Number of Students']
for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce').astype('Int64')

# Função para converter valores de texto para float, lidando com abreviações (B)
def converter_para_float(valor):
    """
    Converte valores de texto para float, lidando com abreviações (B) e removendo símbolos monetários.

    Args:
        valor (str): O valor a ser convertido.

    Returns:
        float: O valor convertido, ou NaN se a conversão falhar.
    """
    valor = valor.replace('$', '').replace(',', '.')  # Remove $, e substitui , por .

    if 'B' in valor:
        valor = valor.replace('B', '')
        multiplicador = 10**9  # Bilhões
    else:
        multiplicador = 1  # Sem abreviação

    valor = ''.join(c for c in valor if c.isdigit() or c == '.')  # Mantém apenas dígitos e .
    try:
        return float(valor) * multiplicador  # Converte para float e multiplica
    except ValueError:
        return np.nan  # Lida com valores inválidos
# Aplica a função de conversão para as colunas 'Endowment' e 'Minimum Tuition cost'
# Aplica a função de conversão e mantém o tipo numérico (float)
df['Endowment'] = df['Endowment'].apply(converter_para_float)
df['Minimum Tuition cost'] = df['Minimum Tuition cost'].apply(converter_para_float)

# Converter colunas para numérico (redundante, mas incluído para garantir a conversão)
df['Number of Students'] = pd.to_numeric(df['Number of Students'], errors='coerce')
df['Minimum Tuition cost'] = pd.to_numeric(df['Minimum Tuition cost'], errors='coerce')
df['Academic Staff'] = pd.to_numeric(df['Academic Staff'], errors='coerce')
df['Endowment'] = pd.to_numeric(df['Endowment'], errors='coerce')

# Informações e primeiras linhas após limpeza e conversão
print(df.dtypes)  # Imprime os tipos de dados das colunas
print(df.head())  # Imprime as primeiras linhas do DataFrame

# Salva o DataFrame limpo
df.to_csv('NorthAmericaUniversities_limpo.csv', index=False)

print("Arquivo salvo com sucesso!")  # Imprime uma mensagem de confirmação





