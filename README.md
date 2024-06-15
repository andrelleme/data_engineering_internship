# Projeto de Data Engineering

Projeto de engenharia de dados envolvendo web scraping, exploração e analise de dados 

## Funcionalidades

- **Download de Dados**: Realiza webscraping das tabelas de 2015 sobre pessoas com 10 ou mais anos de idade relacionando-as a seu uso de internet e posse de celular,salvando os downloads em "IBGE_downloads"
- **Conversão de Dados**: Converte arquivos Excel para formato CSV separando cada folha em um arquivo especifico com o nome da folha,salvando os arquivos em "csv_data"
- **Análise Exploratória de Dados**: Script básico para fazer uma limpeza dos dados deixando apenas as informações específicas desejadas.

## Instalação

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/andrelleme/data_engineering_internship.git
    cd data_engineering_internship
    ```

2. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. **Baixar e converter dados**:
    ```
    python src/main.py
    ```

2. **Realizar análise exploratória de dados**:
    ```
    python eda/data_analysis.py
    ```

## Estrutura do Projeto

```plaintext
data_engineering_internship/
├── eda/
│   └── data_analysis.py
├── src/
│   └── main.py
├── requirements.txt
└── README.md
