import requests 
from bs4 import BeautifulSoup

request = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
response_html = request.text

soup = BeautifulSoup(response_html, 'html.parser')

find_list = soup.find('ol')
anchor_tag = find_list.find_all('a', class_='internal-link' )

for link in anchor_tag:
    href = link.attrs['href'] 

    # filter links ending in '.pdf'
    if(href.endswith('pdf')):
        print(f'\nLink do Anexo PDF: \n{link.attrs['href']}\n\n')
