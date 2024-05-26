import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def load_and_clean_data(self):
        """Carrega e limpa os dados do arquivo CSV fornecido."""
        df = pd.read_csv(self.csv_path, skiprows=5)  # Pular as primeiras linhas que contêm descrições
        df.columns = df.iloc[0]  # Definir a primeira linha como cabeçalho
        df = df[1:]  # Remover a linha do cabeçalho duplicado
        df.columns = df.columns.str.strip()  # Remover espaços em branco dos nomes das colunas
        df = df.dropna(how='all')  # Remover linhas completamente vazias
        df = df.dropna(axis=1, how='all')  # Remover colunas completamente vazias
        return df

    def prettify_data(self, df):
        """Ajusta o DataFrame para uma forma mais legível."""
        # Implementar ajustes específicos conforme necessário
        return df

    def analyze_data(self):
        """Carrega, limpa e analisa os dados."""
        df = self.load_and_clean_data()
        df = self.prettify_data(df)
        self.visualize_data(df)

    def visualize_data(self, df):
        """Gera visualizações para analisar os dados."""
        if not df.empty:
            plt.figure(figsize=(12, 8))
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
            plt.title('Correlation Matrix')
            plt.show()

            # Exemplo de visualização: Gráfico de distribuição de uma coluna numérica
            # Verificar se a coluna existe antes de tentar visualizar
            if 'Pessoas de 10 anos ou mais de idade (%)' in df.columns:
                plt.figure(figsize=(10, 6))
                sns.histplot(df['Pessoas de 10 anos ou mais de idade (%)'], kde=True)
                plt.title('Distribution of Pessoas de 10 anos ou mais de idade (%)')
                plt.show()

if __name__ == '__main__':
    csv_path = '/mnt/data/01_Utilizacao_da_Internet_cv_Tab 1.1.1.1 e 1.1.1.2.csv_Tab 1.1.1.1 e 1.1.1.2.csv'
    analyzer = DataAnalyzer(csv_path)
    analyzer.analyze_data()
