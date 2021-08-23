from aluno import Aluno
from funcionario import Funcionario
from professor import Professor

alunoDaniel = Aluno("Daniel de Oleveira", "778.092.117.45", "3° B", "manhã")
print(alunoDaniel)

funcionario = Funcionario ("Rodrigo Soares", "993.308.452-09", "proteiro", "07h00 ás 23h00")
print(funcionario)

professorJosé = Professor("José de Oliveira", "111.990.749-45", "Biologia", "concursado");
print(professorJosé)

def acessarEscola(self, codigo_acesso):
    if (codigo_acesso == self.__cpf):
        print("Bem vindo professor(a), ", super().nome)
        return True
    else:
        return False