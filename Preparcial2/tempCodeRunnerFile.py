class Vehiculo():
    def __init__(self,patente,descripcion = '') -> None:
        self.patente = patente
        self.descripcion = descripcion

    def mostrar(self):
        print(f'La patente es: {self.patente} con la descripcion: {self.descripcion}')

    def validarPatente(self):
        if (len(self.patente) == 6) or (len(self.patente) == 8):
            return True
        return False
    
class Estadia(Vehiculo):
    def __init__(self,patente,descripcion,entrada,salida) -> None:
        super().patente = patente
        super().descripcion = descripcion
        self.entrada = entrada
        self.salida = salida
        
    def mostrar(self):
        super().mostrar()
        print(f'El Horario de entrada es: {self.entrada} y el Horario de salida es: {self.salida}')
        
    def calcularTarifaTotal(self,tarifaPorHora):
        if (super().validarPatente(self.patente)):
            if (self.salida >= self.entrada):
                return (self.salida - self.entrada) * tarifaPorHora
            else:
                return print("Hora de entrada mayor a la hora de salida")
        else:
            return print("Patente invalida")
        
auto = Vehiculo('ALE123','Auto re copado')
'''print(auto.patente)
print(auto.descripcion)'''

# auto.mostrar()
print(auto.validarPatente())