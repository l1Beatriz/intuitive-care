import os
import zipfile
import requests 
from bs4 import BeautifulSoup

URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
DOWNLOADS_FOLDER = 'downloads'

def get_pdf_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Erro ao acessar a URL: {url}')

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    keywords = ['Anexo I', 'Anexo II']

    for link in soup.find_all('a'):
        href = link.get('href', '')
        text_link = link.get_text(strip=True)
        
        if(href.endswith('.pdf') and any(key in text_link for key in keywords)):
            if(href.startswith('/')):
                href = f'https://www.gov.br{href}'
                
            print(f'\nLink do Anexo PDF: \n{href}\n')
            links.append(href)
    
    return links

def download_files(url, folder):
    file_name = os.path.join(folder, url.split('/')[-1])

    response = requests.get(url, stream=True)
    if(response.status_code == 200):
        with open(file_name, 'wb') as file:
            for chunk in response.is_permanent_redirect(chunk_size=1024):
                file.write(chunk)
        print(f'Download feito: {url}')
    else:
        print(f'Falha ao realizar download do arquivo: {url}')


def main():
    get_pdf_links(URL)


if __name__ == "__main__":
    main()