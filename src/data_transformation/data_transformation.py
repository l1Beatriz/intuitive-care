import os
import pdfplumber
import pandas as pd
from zipfile import ZipFile
from colorama import Fore, Style


PATH_PDF = r'data_transformation\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
print(f'{os.path.exists(PATH_PDF)}')

abreviations = {
    'OD': 'Outros Departamentos',
    'AMB': 'Ambulatório'
}

FOLDER_ZIP_CSV = 'Teste_beatriz.zip'

def extract_data_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_pages = []

        for i, page in enumerate(pdf.pages):
            print(f'\nVerificando página {i + 1}...')
            table = page.extract_table()
            if table:
                print(f'{Fore.GREEN}Tabela encontrada na página {i + 1}{Style.RESET_ALL}')
                all_pages.extend(table)
            else:
                print(f'{Fore.YELLOW}Nenhuma tabela foi encontrada na página {i + 1}{Style.RESET_ALL}')
    return all_pages

def format_to_csv(data, file_name='rol_de_procedimentos_e_eventos_em_saude.csv'):
    if not data:
        print(f'{Fore.RED}Nenhum dado extraido{Style.RESET_ALL}')
        return
    
    columns = data[0] if data else []
    rows = data[1:] if len(data) > 1 else []

    df = pd.DataFrame(rows, columns=columns)
    df.replace(abreviations, inplace=True)

    df = df.dropna().applymap(lambda x: x.strip() if isinstance(x, str) else x)

    df.to_csv(file_name, index=False, encoding='utf-8')
    print(f'{Fore.GREEN}Arquivo CSV salvo com sucesso!\n{Fore.MAGENTA}{file_name}{Style.RESET_ALL}')

def compact_csv(file, folder=FOLDER_ZIP_CSV):


def process_transformation():
    data_extrated = extract_data_from_pdf(PATH_PDF)
    format_to_csv(data_extrated)
    for line in data_extrated[:5]: 
        print(f'\n{line}\n')

