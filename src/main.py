from colorama import Fore, Style
from scraping import scraping

def options():
    print('\n1. Scraping Scraping')
    print('2. Executar transformação de dados')


def options_run():
    options()
    input_option_run = input('\nEscolha um projeto para executar:')

    if input_option_run == '1':
        print(f'\n{Fore.CYAN}nexecutando scraping{Style.RESET_ALL}')
        scraping.process_downloads()


def main():
    options_run()

if __name__ == '__main__':
    main()