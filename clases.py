class moldeGalleta:
    forma = 'rectangular'
    bordes = 'redondeados'
    sabor = 'dulce'
    relieve = True

galleta1 = moldeGalleta()
print(galleta1.forma) #el. es para acceder a los atributos de la clase
print(galleta1.bordes)
print(galleta1.sabor)
print(galleta1.relieve)

galleta2 = moldeGalleta()
print(galleta2.forma)
print(galleta2.bordes)
print(galleta2.sabor)
print(galleta2.relieve)

#Crear clase para elaborar autos
class auto:
    marca = 'Lamborghini'
    modelo = 'Aventador'
    color = 'blanco'
    caballos = 500
    puertas = 2
    asientos = 4
lambo1 = auto()
lambo2 = auto()
lambo3 = auto()
print(lambo1.marca)
print(lambo1.modelo)
print(lambo2.color)

class persona:
    cant_ojos = 2
    def __init__(self, nombre, apellido, edad, genero):
        self.name = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero #estos son clases con constructor
    def saludosimple(self):
            print('Hola')
persona1 = persona('Juan', 'Aviles', 19, 'Masculino')
persona2 = persona('Maria', 'Aviles', 19, 'Femenino')
persona1.saludosimple()
persona2.telefono = '0999999999' #agregar atributos a un objeto en especifico sin necesidad de crearlo en la clase
persona2.name = 'Mary'
print(persona1.name)
print(persona2.telefono)
print(persona2.name)
#crear clase que me permita crear diferente tipo de perros
class perro:
    cant_patas = 4
    def __init__(self, nombre, raza, edad, color):
        self.name = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
perro1 = perro('Firulais', 'Pitbull', 5, 'Negro')

#clase de suma de 2 numeros
class suma:
    def __init__(self, numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2
    def reso_suma(self):
        print(self.num1 + self.num2)
suma1 = suma('1', '2')
suma1.reso_suma()

