class Fecha():
    def __init__(self):
        self.__dia = 1
        return None

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print("Error 0-31")
        return None