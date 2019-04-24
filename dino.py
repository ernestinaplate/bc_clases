class Dino:
    patas = 4 # Estos son los atributos de la clase
    nombre = None 

    def __init__(self, cant_patas, un_nombre): 
        # Funcion para inicializar la clase, no importa el contenido, si importa el nombre
        self.patas = cant_patas
        self.nombre = un_nombre
        print("Hola soy un dinosaurio, me llamo " + str(self.nombre) + " y tengo " + str(cant_patas) + " patas.")
    
    def get_patas(self):
        return self.patas
    
    def set_patas(self, cantidad):
        self.patas = cantidad
    
pepito = Dino(7, "Pepito")