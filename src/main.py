import os
from converter import ExcelToCSVConverter
from downloader import IBGEDownloader

def main():
    # Caminhos
    excel_dir = 'IBGE_downloads'
    csv_dir = 'csv_data'  # Ajustado para estar na mesma estrutura de pastas

    # Garantir que os diretórios existem
    os.makedirs(csv_dir, exist_ok=True)

    # Baixar arquivos do IBGE
    base_url = 'https://servicodados.ibge.gov.br/api/v1/downloads/estatisticas?caminho=Acesso_a_internet_e_posse_celular/2015/Coeficientes_de_Variacao/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade&nivel=1'
    downloader = IBGEDownloader(base_url, excel_dir)
    downloader.download_all_files()

    # Converter arquivos Excel para CSV
    converter = ExcelToCSVConverter(excel_dir, csv_dir)
    converter.convert_all()

if __name__ == '__main__':
    main()
