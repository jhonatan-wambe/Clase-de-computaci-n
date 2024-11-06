class Persona: # Definición de la Clase Persona
    def __init__(self, name="", age=0): # El método __init__ es el constructor de la clase Persona
        self.__name = name # self.__name es un atributo privado (indicado por los dos guiones bajos __). Inicialmente se asigna el valor del parámetro name, que por defecto es una cadena vacía.
        self.age = age  # self.age es un atributo público, y su valor por defecto es 0.
    
    def __str__(self): # El método __str__ define cómo se verá un objeto Persona cuando se imprima.
        return self.__name+" "+str(self.age) # Devuelve una cadena que combina el nombre privado (__name) y la edad (age), separados por un espacio.
    
    def setName(self, name): # El método setName permite cambiar el valor del atributo privado __name.
        self.__name = name
    
    def getName(self): #  método getName permite acceder al valor del atributo privado __name.
        return self.__name

# 2. Creación y Modificación de un Objeto Persona

p = Persona("Pedro",25) # Se crea un objeto Persona, p, con el nombre "Pedro" y la edad 25.
print(p) # print(p) muestra "Pedro 25" gracias al método __str__.

p.__name = "Pablo"
'''Aunque se intenta cambiar el valor de p.__name a "Pablo", 
este cambio no afecta el atributo privado self.__name.
Esto se debe a que __name es privado, y el intento de modificarlo 
en realidad crea un nuevo atributo __name que es independiente del atributo privado original self.__name.'''

p.age = 26 # p.age = 26 cambia el valor de age, ya que este es un atributo público.
print(p.__name)    # print(p.__name) imprime "Pablo" (el nuevo atributo público).
print(p.age)       # print(p.age) imprime 26.
print(p.getName()) # devuelve el nombre original "Pedro" usando el método getName, mostrando que el atributo privado no se alteró con p.__name = "Pablo"
print(p)           #  imprime "Pedro 26", confirmando que el nombre original permanece sin cambios

p.setName("Pablo") # p.setName("Pablo") cambia el atributo privado __name a "Pablo".
print(p) # 
print(p.getName()) # print(p) y print(p.getName()) ahora muestran "Pablo 26".


# Creación de Objetos Persona sin Parámetros
p1 = Persona() # Crea un objeto Persona p1 con los valores por defecto (name="" y age=0).
print(p1) # imprime " 0".

p1 = Persona("Jose") # Crea un objeto Persona p1 con name="Jose" y age=0.
print(p1) # imprime "Jose 0".

p1 = Persona(age=2) # Crea un objeto Persona p1 con age=2 y name=""
print(p1) # imprime " 2".
