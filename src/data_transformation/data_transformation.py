import pdfplumber
import os

PATH_PDF = os.path.abspath('Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')
print(f'{os.path.exists(PATH_PDF)}')

def extract_data_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_pages = []

        for i, page in enumerate(pdf.pages):
            print(f'\nVerificando página {i + 1}...')
            table = page.extract_table()
            if table:
                print(f'Tabela encontrada na página{i + 1}')
                all_pages.extend(table)
    return all_pages


data_extrated = extract_data_from_pdf(PATH_PDF)
for line in data_extrated[:5]:  # Exibe apenas as 5 primeiras linhas
    print(f'\n{line}\n')