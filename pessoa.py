class Pessoa:
    def __init__(self, peso, altura):
        #self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        self.__IMC = None
    
    def calcular_imc(self):
        self.__IMC = round(self.__peso / (self.__altura)**2, 2)
        return self.__IMC 