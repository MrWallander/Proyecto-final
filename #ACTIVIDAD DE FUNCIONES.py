#ACTIVIDAD DE FUNCIONES
#De Raziel Wallander
#PRIMERO LAS FUNCIONES
def saludarnombres(nombres):
    for nombre in nombres:
        if nombre == "Tadeo":
            print("menos tu Tadeo")
        elif nombre =="wallander":
            print("suicidate por favor")
        elif nombre == "samantha":
            print("hola rata")
        else:
            print("hola ", nombre)

            #Programa Principal
            nombres = ["samantha", "lucy" , "diego", "wallander", "oscar","tadeo"]
            saludarnombres(nombres)
            
            