# Creat una clase Persona con atributo nombre
# Despues instanciar un objeto de tipo persona

class Persona:
    nombre = None
    def __init__(self, un_nombre):
        self.nombre = un_nombre
        print("Mi nombre es " + str(self.nombre) + "!\n")

nina = Persona("Ernestina")