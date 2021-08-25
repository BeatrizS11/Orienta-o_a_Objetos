from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

class Escola():
    def __init__(self):
        self.__nome = "Escola Estadual Jardim Canadá"

        aluno1 = Aluno("Samuel cordeiro", "327.711.603-54", "009-451-69", "tarde")
        aluno = Aluno("Juliana de Oliveira", "445.170.203-17", "554-109-18", "noite")

        professor = Professor("José de Oliveira", "111.990.749-45", "Biologia", "concursado")

        funcionario = Funcionario("Rodrigo Soares", "993.308.452-09", "proteiro", "07h00 ás 23h00")

        self.__pessoas = [aluno1, aluno, professor, funcionario]

    def __getitem__(self, item):
        return self.__pessoas[item]

    def __len__(self):
        return len(self.__pessoas)

    def solicitarAcesso(self):
        codigo_acesso = input("Seu código de acesso: ")

        for pessoa in self.__pessoas:
            if (pessoa.acessarEscola(codigo_acesso)):
                return True

        print("Acesso negado..")
        return False