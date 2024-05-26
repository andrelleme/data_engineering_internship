import os
import pandas as pd

class ExcelToCSVConverter:
    def __init__(self, excel_dir, csv_dir):
        self.excel_dir = excel_dir
        self.csv_dir = csv_dir
        os.makedirs(self.csv_dir, exist_ok=True)

    def convert_all(self):
        for filename in os.listdir(self.excel_dir):
            if filename.endswith('.xlsx'):
                excel_path = os.path.join(self.excel_dir, filename)
                csv_path = os.path.join(self.csv_dir, filename.replace('.xlsx', '.csv'))
                self.convert_file(excel_path, csv_path)

    def convert_file(self, excel_path, csv_path):
        xls = pd.ExcelFile(excel_path)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            if not df.empty and len(df.columns) > 1:  # Ignorar abas sem dados
                df.to_csv(csv_path.replace('.csv', f'_{sheet_name}.csv'), index=False)
                print(f'Conversão Finalizada! Arquivo salvo em {csv_path.replace(".csv", f"_{sheet_name}.csv")}')
