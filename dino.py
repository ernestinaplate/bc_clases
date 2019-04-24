class Dino: # Por convencion, con mayuscula
    patas = 4 # Estos son los atributos de la clase
    nombre = None 
    # METODO = Funcion para objetos, no funciona sin usar el objeto

    def __init__(self, cant_patas, un_nombre): # METODO CONSTRUCTOR
        # METODO para inicializar la clase, no importa el contenido, si importa el nombre
        self.patas = cant_patas
        self.nombre = un_nombre
        print("Hola soy un dinosaurio, me llamo " + str(self.nombre) + " y tengo " + str(cant_patas) + " patas.")
    
    def get_patas(self):
        return self.patas
    
    def set_patas(self, cantidad):
        self.patas = cantidad
    
    def cortar_pata(self):
        self.patas = self.patas - 1
    
pepito = Dino(7, "Pepito") # Aca instanciamos el objeto

# HOLA