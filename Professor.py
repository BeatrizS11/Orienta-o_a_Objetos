from abc import ABCMeta, abstractmethod

class Professor(metaclass = ABCMeta):
    def __init__(self, nome, cpf, formacao, vinculo):
        super().__init__(nome, cpf)
        self.__formacao = formacao
        self.__vinculo = vinculo

    @property
    def formacao(self):
        return self.__formacao

    @property
    def vinculo(self):
        return self.__vinculo

    def __str__(self):
        return "PROFESSOR: "+super().nome+" | CPF: "+super().cpf+" | Formação: "+self.__formacao+" | Vínculo: "+self.__vinculo

    def acessarEscola(self, codigo_acesso):
        if (codigo_acesso == self.__cpf):
            print("Bem vindo professor(a), ", super().nome)
            return True
        else:
            return False