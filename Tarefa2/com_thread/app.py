import threading
import random
import string
import time

def gerar_nome(tamanho=8):
    return ''.join(random.choices(string.ascii_uppercase, k=tamanho))

def gerar_lista_nomes(qtd):
    return [gerar_nome() for _ in range(qtd)]

def ordenar_pente(lista):
    tamanho = len(lista)
    gap = tamanho
    troca = True

    while gap > 1 or troca:
        gap = max(1, int(gap / 1.3))
        i = 0
        troca = False
        while i + gap < tamanho:
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                troca = True
            i += 1

def gerar_nomes_thread(nomes_lista):
    nomes_lista.extend(gerar_lista_nomes(1000000))

def salvar_arquivo_thread(nomes_lista):
    with open('nomes_com_thread.txt', 'w') as f:
        for nome in nomes_lista:
            f.write(nome + '\n')

def com_threads():
    nomes = []

    t1 = threading.Thread(target=gerar_nomes_thread, args=(nomes,))
    t1.start()
    t1.join()  

    t2 = threading.Thread(target=salvar_arquivo_thread, args=(nomes,))
    t2.start()
    t2.join()  

    nomes_copia = nomes[:]
    comecar_sort = time.time()
    nomes_copia.sort()
    fim_sort = time.time()

    nomes_copia_pente = nomes[:]
    comecar_pente = time.time()
    ordenar_pente(nomes_copia_pente)
    fim_pente = time.time()

    print(f"Tempo para ordenar com sort: {fim_sort - comecar_sort:.2f} segundos")
    print(f"Tempo para ordenar com pente: {fim_pente - comecar_pente:.2f} segundos")

if __name__ == '__main__':
    com_threads()
