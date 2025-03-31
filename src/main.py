from colorama import Fore, Style
from scraping import scraping

def options():
    print('\n1. Executar Scraping')
    print('2. Executar transformação de dados')


def options_run():
    options()
    input_option_run = input('\nEscolha um projeto para executar:')

    if input_option_run == '1':
        print(f'\n{Fore.CYAN}nexecutando scraping{Style.RESET_ALL}')
        scraping.process_downloads()

    elif input_option_run == '2':
        print(f'\n{Fore.CYAN}executando transformação de dados{Style.RESET_ALL}')

def main():
    options_run()

if __name__ == '__main__':
    main()