import os
import zipfile
import requests 
from bs4 import BeautifulSoup

URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

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

# def download_files():
    # global href
    # for link in anchor_tag:
        # href = link.attrs['href'] 

        # filter links ending in '.pdf'
        # if(href.endswith('pdf')):
        #     url = requests.get(href)
        #     print(url)


def main():
    get_pdf_links(URL)


if __name__ == "__main__":
    main()