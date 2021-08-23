from abc import ABCMeta, abstractmethod

class Aluno(metaclass = ABCMeta):
    def __init__(self, nome, cpf, cgm, turno):
        super().__init__(nome, cpf)
        self.__cgm = cgm
        self.__turno = turno

    @property
    def cgm(self):
        return self.__cgm

    @property
    def turno(self):
        return self.__turno

    def __str__(self):
        return "ALUNO: "+super().nome+" | CPF: "+super().cpf+\
               " | CGM: "+self.__cgm+" | Turno: "+self.__turno

    def acessarEscola(self, codigo_acesso):
        if(codigo_acesso == self.__cgm):
            print("Bem vindo aluno(a), ", super().nome)
            return True
        else :
            return False