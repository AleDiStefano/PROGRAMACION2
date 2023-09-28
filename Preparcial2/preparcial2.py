'''Definir una función primeros_tres(lista) que reciba como parámetro la siguiente lista y retorne
una nueva lista con los primeros 3 elementos.
lista = ["ho", 3.16, "la", 81, 6, 42]'''

def primerosTres(lista):
    primerosTresElementos = []
    primerosTresElementos.append(lista[0])
    primerosTresElementos.append(lista[1])
    primerosTresElementos.append(lista[2])
    return print(primerosTresElementos)

lista = ["ho", 3.16, "la", 81, 6, 42] 
primerosTres(lista)

'''Definir una función concatena(string1, string2, nro) que reciba como parámetro dos strings y un
número y los devuelva concatenados. '''

def concatena(string1, string2, nro):
    retorna = string1 + string2 + str(nro)
    return print(retorna)

concatena("hola ","que tal? " , 123)

'''Suponga que tiene que desarrollar un sistema para un estacionamiento.
 1. Crear una clase llamada Vehiculo con atributos patente, y descripcion(opcional vacio por
defecto)
 Implementar los siguientes métodos:
 1. Un constructor
 2. mostrar(): muestra los datos del vehiculo
 3. validarPatente(): Valida que la patente tenga 6 u 8 caracteres
 2. Crear una clase llamada Estadia con atributos Vehiculo, hora de entrada y salida.
Implementar los siguientes métodos:
 1. Un constructor
 2. mostrar(): Debera mostrar TODOS los datos de la Estadia
 3. calcularTarifaTotal(tarifaPorHora): Deberá retornar el valor de la tarifa total en pesos
teniendo encuenta la entrada y salida y la tarifa por hora. Si la patente es invalida o la entrada más
reciente que la salida deberá informar un error.'''

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
# print(auto.validarPatente())