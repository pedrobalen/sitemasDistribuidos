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

def sem_threads():
    nomes = gerar_lista_nomes(1000000)
    
    comecar_arquivo = time.time()
    with open('nomes_sem_thread.txt', 'w') as f:
        for nome in nomes:
            f.write(nome + '\n')
    fim_arquivo = time.time()

    nomes_copia = nomes[:]
    comecar_sort = time.time()
    nomes_copia.sort()
    fim_sort = time.time()

    nomes_copia_pente = nomes[:]
    comecar_pente = time.time()
    ordenar_pente(nomes_copia_pente)
    fim_pente = time.time()

    print(f"Tempo para salvar em arquivo: {fim_arquivo - comecar_arquivo:.2f} segundos")
    print(f"Tempo para ordenar com sort: {fim_sort - comecar_sort:.2f} segundos")
    print(f"Tempo para ordenar com pente: {fim_pente - comecar_pente:.2f} segundos")

if __name__ == '__main__':
    sem_threads()
