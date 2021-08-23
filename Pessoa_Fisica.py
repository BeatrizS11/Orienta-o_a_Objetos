from abc import ABCMeta, abstractmethod

class PessoaFisica(metaclass = ABCMeta):
    def __init__(self, name, cpf):
        self.__nome = name
        self.__cpf = cpf

def nome(self):
    @property
    def cpf(self):
        return self.__cpf
        return self.__cpf

    @abstractmethod
    def acessarEscola(self, codigo_acesso):
        pass

    def acessarEscola(self, codigo_acesso):
        if (codigo_acesso == self.__cpf):
            print("Bem Vindo, ", super().nome)
            return True
        else:
            return False