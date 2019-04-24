# Creat una clase Persona con atributo nombre
# Despues instanciar un objeto de tipo persona

# Modificar la clase persona, agregarle un atributo edad
# y un metodo cumple_anos

class Persona:
    nombre = None
    edad = None
    def __init__(self, un_nombre, una_edad):
        self.nombre = un_nombre
        self.edad = una_edad
        print("Mi nombre es " + str(self.nombre) + " y tengo " + str(self.edad) + " anos!\n")
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def cumple_anos(self):
        self.edad += 1

nina = Persona("Ernestina", 19)
