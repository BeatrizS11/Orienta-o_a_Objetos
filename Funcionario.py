from abc import ABCMeta, abstractmethod

class Funcionario(metaclass = ABCMeta):
    def __init__(self, name, cpf, cargo, horario):
        super().__init__(name, cpf)
        self.__cargo = cargo
        self.__horario = horario

    @property
    def cargo(self):
        return self.__cargo

    @property
    def horario(self):
        return self.__horario

    def __str__(self):
        return "FUNCIONÁRIO: "+super().nome+" | CPF: "+super().cpf+" | Cargo: "+self.__cargo+" | Horário: "+self.__horario


    def acessarEscola(self, codigo_acesso):
        if (codigo_acesso == self.__cgm):
            print("Bom trabalho, ", super().nome)
            return True
        else:
            return False