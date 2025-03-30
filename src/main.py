from scraping import scraping

def options():
    print('\n1. Scraping Scraping')
    print('2. Executar transformação de dados')

def options_run():
    options()
    input_option_run = input('\nEscolha um projeto para executar:')

    if input_option_run == '1':
        print('\nexecutando scraping')
        scraping.process_downloads()


def main():
    options_run()

if __name__ == '__main__':
    main()