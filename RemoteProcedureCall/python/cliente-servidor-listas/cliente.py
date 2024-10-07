import xmlrpc.client

def main():
    endereco_servidor = "localhost"
    porta_servidor = 50000
    cliente = xmlrpc.client.ServerProxy("http://" + endereco_servidor + ":" + str(porta_servidor) + "/")

    quantidade_alunos = int(input("Quantos alunos você deseja cadastrar? "))
    
    lista_alunos = cliente.popular_lista_alunos(quantidade_alunos)
    print(f"Lista de alunos cadastrados: {lista_alunos}")

    ordem = input("Você deseja ordenar em ordem crescente ou decrescente? ").strip().lower()
    
    try:
        lista_ordenada = cliente.ordenar_lista(lista_alunos, ordem)
        print(f"Lista de alunos ordenada recebida: {lista_ordenada}")
    except Exception as e:
        print(f"Ocorreu um erro ao ordenar a lista: {e}")

    try:
        lista_exibida = cliente.exibir_lista(lista_ordenada)
        print(f"Lista exibida: {lista_exibida}")
    except Exception as e:
        print(f"Ocorreu um erro ao exibir a lista: {e}")

    print(cliente.dizer_ola())  
if __name__ == "__main__":
    main()
