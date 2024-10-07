class Aluno:
    def __init__(self, matricula, nome) -> None:
        self.nome = nome.upper()
        self.matricula = matricula

    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.matricula == other.matricula
        return False

    def __repr__(self):
        return f"{self.matricula}: {self.nome}"