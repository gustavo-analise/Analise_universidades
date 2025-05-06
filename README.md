# Análise de Universidades da América do Norte

Este projeto realiza uma análise exploratória de dados sobre universidades nos Estados Unidos e Canadá, utilizando Python, Pandas, Plotly Express e Streamlit. O objetivo é fornecer insights sobre o custo de mensalidades, número de alunos, corpo docente e outros fatores relevantes, permitindo comparações e visualizações interativas.
## **Acesse o Dashboard Interativo:** [https://mpexpxu7fweqgknmhrpjge.streamlit.app/](https://mpexpxu7fweqgknmhrpjge.streamlit.app/)
## Visão Geral

O projeto consiste em duas partes principais:

1.  **Limpeza e Preparação dos Dados:**
    * O script `limpeza_dados.py` realiza a limpeza e transformação dos dados brutos do arquivo `NorthAmericaUniversities.csv`.
    * As etapas incluem tratamento de valores ausentes, conversão de tipos de dados e formatação de valores numéricos.
    * O resultado é um arquivo limpo `NorthAmericaUniversities_limpo.csv`, pronto para análise.

2.  **Dashboard Interativo com Streamlit:**
    * O aplicativo `app.py` cria um dashboard interativo usando Streamlit.
    * Permite aos usuários filtrar os dados por país, número de alunos e custo de mensalidade.
    * Apresenta visualizações como gráficos de barras, dispersão e linhas, utilizando Plotly Express.
    * Inclui uma tabela interativa para explorar os dados em detalhes.

## Aqui estão alguns dos gráficos gerados pela aplicação:
![Screenshot dos Gráficos da Análise de Universidades](https://github.com/user-attachments/assets/37fd97d2-2af2-4ef5-aee9-783ae0e72fd1)

## A tabela permite visualizar os dados brutos com filtros aplicados:
![Screenshot da Tabela Interativa do Dashboard](https://github.com/user-attachments/assets/ba7ea0be-7146-4933-9c46-c3592271de39)

## Funcionalidades

* **Filtros Interativos:** Permitem aos usuários explorar os dados com base em critérios específicos.
* **Visualizações Dinâmicas:** Gráficos interativos que fornecem insights sobre os dados.
* **Tabela Interativa:** Exibe os dados em formato tabular, com formatação de valores numéricos.
* **Comparação de Universidades:** Compara as top 10 universidades dos EUA e Canadá.
* **Análise de Tendências:** Visualiza o tamanho da universidade por década de fundação.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Pandas:** Manipulação e análise de dados.
* **Plotly Express:** Criação de gráficos interativos.
* **Streamlit:** Desenvolvimento de aplicativos web interativos.
* **Git/GitHub:** Controle de versão e hospedagem do código.

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/gustavo-analise/Analise_universidades.git](https://github.com/gustavo-analise/Analise_universidades.git)
    cd Analise_universidades
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run app.py
    ```

5.  **Execute o script de limpeza de dados (se necessário):**
    ```bash
    python limpeza_dados.py
    ```

## Estrutura do Projeto
Analise_universidades/
├── app.py                      # Aplicativo Streamlit
├── limpeza_dados.py            # Script de limpeza de dados
├── NorthAmericaUniversities.csv # Dados brutos
├── NorthAmericaUniversities_limpo.csv # Dados limpos
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação do projeto

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou correções de bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

* Gustavo

## Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).
