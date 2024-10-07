from xmlrpc.server import SimpleXMLRPCServer
from aluno import Aluno


def popular_lista_alunos(quantidade):
    lista = []
    for i in range(quantidade):
        matricula = f"{i+1:05d}"
        nome = f"Aluno {i+1}"
        aluno = Aluno(matricula, nome)
        if aluno not in lista:
            lista.append(aluno)
    return lista

def ordenar_lista(lista, ordem='crescente'):
    if ordem == 'decrescente':
        return sorted(lista, key=lambda aluno: aluno['matricula'], reverse=True)
    return sorted(lista, key=lambda aluno: aluno['matricula'])

def exibir_lista(lista):
    return [{"matricula": aluno.matricula, "nome": aluno.nome} for aluno in lista]

def dizer_ola():
    return "Olá"

def main():
    endereco_servidor = "localhost"
    porta_servidor = 50000
    servidor = SimpleXMLRPCServer((endereco_servidor, porta_servidor))
    
    print("Servidor em execução na porta", porta_servidor)
    
    servidor.register_function(popular_lista_alunos, "popular_lista_alunos")
    servidor.register_function(ordenar_lista, "ordenar_lista")
    servidor.register_function(exibir_lista, "exibir_lista")
    servidor.register_function(dizer_ola, "dizer_ola")
    
    servidor.serve_forever()

if __name__ == "__main__":
    main()
