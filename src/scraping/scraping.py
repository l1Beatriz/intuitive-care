import os
import zipfile
import requests 
from bs4 import BeautifulSoup
from colorama import Fore, Style

URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
DOWNLOADS_FOLDER = 'downloads'

def get_pdf_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'{Fore.RED}Erro ao acessar a URL: {url}{Style.RESET_ALL}')

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    keywords = ['Anexo I', 'Anexo II']

    for link in soup.find_all('a'):
        href = link.get('href', '')
        text_link = link.get_text(strip=True)
        
        if href.endswith('.pdf') and any(key.lower() in text_link.lower() for key in keywords):
            if href.startswith('/'):
                href = f'https://www.gov.br{href}'
                
            links.append(href)
    
    return links

def download_files(url, folder):
    if not os.path.exists(DOWNLOADS_FOLDER):
        os.makedirs(DOWNLOADS_FOLDER)

    file_name = os.path.join(folder, url.split('/')[-1])

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f'{Fore.CYAN}Download concluído com sucesso do anexo:\n{Style.RESET_ALL}{url}\n')
    else:
        print(f'{Fore.RED}Falha ao realizar download do arquivo: {url}{Style.RESET_ALL}')

def zip_files(folder, output_file_name='anexos_pdf.zip'):
    zip_path = os.path.join(folder, output_file_name)
    
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    if output_file_name in files:
        files.remove(output_file_name)

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files:
            file_path = os.path.join(folder, file)
            zipf.write(file_path, os.path.basename(file_path))
               

    print(f'{Fore.MAGENTA}Arquivos compactados em: {Style.RESET_ALL}{zip_path}')

def process_downloads():
    try:
        links_pdf = get_pdf_links(URL)
        print(f'Encontrados {len(links_pdf)} arquivos PDF para download\n')

        if not links_pdf:
            print('Nenhum arquivo disponível')
            return

        for link in links_pdf:
            download_files(link, DOWNLOADS_FOLDER)

        zip_files(DOWNLOADS_FOLDER)

    except Exception as error:
        print(f'{Fore.RED}Erro{Style.RESET_ALL}', error)


def main():
   process_downloads()


if __name__ == "__main__":
    main()