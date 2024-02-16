from connect_vpn import conectar_vpn
import time

caminho_arquivo = '.\\vpns.txt'

# Abrir o arquivo para leitura
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    # Ler todas as linhas do arquivo e armazenar em uma lista
    lista_de_nomes = arquivo.read().splitlines()



for nome in lista_de_nomes:
    conectar_vpn(nome)
    time.sleep(1)