import os
import shutil
import pdfplumber
import pandas as pd
from zipfile import ZipFile
from colorama import Fore, Style


PATH_PDF = r'data_transformation\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
CSV_FILE_NAME = 'rol_de_procedimentos_e_eventos_em_saude.csv'
FOLDER_ZIP_CSV = 'Teste_beatriz.zip'
PATH_DIR = r'downloads'

abreviations = {
    'OD': 'Seg. Ondotológica',
    'AMB': 'Seg. Ambulatórial'
}

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

def format_to_csv(data, file_name=CSV_FILE_NAME):
    if not data:
        print(f'{Fore.RED}Nenhum dado extraido{Style.RESET_ALL}')
        return
    
    columns = data[0] if data else []
    rows = data[1:] if len(data) > 1 else []

    df = pd.DataFrame(rows, columns=columns)
    df.replace(abreviations, inplace=True)

    df.to_csv(file_name, index=False, encoding='utf-8')
    print(f'{Fore.CYAN}\nArquivo CSV salvo com sucesso!\n{Fore.MAGENTA}{file_name}{Style.RESET_ALL}')

    return file_name

def compact_csv(csv_file, folder_zip=FOLDER_ZIP_CSV):
    if not os.path.exists(csv_file):
        print(f'{Fore.RED}Erro: O arquivo CSV não foi encontrado!{Style.RESET_ALL}')
        return
    
    with ZipFile(folder_zip, 'w') as zip:
        zip.write(csv_file, os.path.basename(csv_file))

    print(f'{Fore.CYAN}\nArquivo ZIP criado com sucesso!\n{Fore.MAGENTA}{folder_zip}{Style.RESET_ALL}')
    return folder_zip

def move_zip_for_downloads(zip_file, path_dir=PATH_DIR):
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)

    path_dir_move = os.path.join(path_dir, os.path.basename(zip_file))
    shutil.move(zip_file, path_dir_move)

    print(f'\nZIP movido para: {path_dir_move}')

def process_transformation():
    data_extrated = extract_data_from_pdf(PATH_PDF)
    file_csv = format_to_csv(data_extrated)

    if file_csv:
        try:
           zip_file = compact_csv(file_csv)
           move_zip_for_downloads(zip_file)

        except Exception as error:
            print(f'{Fore.RED}\nErro ao compactar: {error}{Style.RESET_ALL}')

