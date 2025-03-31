import os
import pdfplumber
from colorama import Fore, Style


PATH_PDF = 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
print(f'{os.path.exists(PATH_PDF)}')

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




data_extrated = extract_data_from_pdf(PATH_PDF)
for line in data_extrated[:5]:  # Exibe apenas as 5 primeiras linhas
    print(f'\n{line}\n')