import os
import zipfile
import requests 
from bs4 import BeautifulSoup


find_list = soup.find('ol')
anchor_tag = find_list.find_all('a', class_='internal-link' )
# https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
def get_pdf_links(url):
    response = requests.get('')
    soup = BeautifulSoup(response, 'html.parser')



def download_files():
    global href
    for link in anchor_tag:
        href = link.attrs['href'] 

        # filter links ending in '.pdf'
        if(href.endswith('pdf')):
            print(f'\nLink do Anexo PDF: \n{href}\n')
            url = requests.get(href)
            print(url)



download_files()