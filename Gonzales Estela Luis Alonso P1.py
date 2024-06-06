from random import choice

def Creación_Matriz():
    global Sintomatologías
    Sintomatologías = [[choice([0,1]) for i in range(10) ] for j in range (10)]

Síntomas = ["fiebre","tos","dolor de cabeza","malestar general","migraña","mareos","pérdida del apetito","insomnio","locura","hiperactividad"]
Enfermedades = ["Gripe","Indigestión","Catarro","Cáncer","Diabetes","Pulmonía","Asma","Autismo","Clamidia","Gonorrea"]
Paciente = []

print("Escriba 1 si presenta dicho síntoma, caso contrario, escriba 0:")

def Diagnóstico():
    Valor = False 
    for i in range(10):
        X = int(input(f"Ingrese si padece {Síntomas[i]}: "))

        while X not in [0,1]:

            print("Error: opción no válida.")
            X = int(input(f"Ingrese si padece {Síntomas[i]}: "))

        Paciente.append(X)

    for i in range(10):
        if Paciente == Sintomatologías[i]:
            print(f"Usted padece de {Enfermedades[i]}")
            Valor = True

    if Valor == False:
        print("Sin coincidencias, no se puede emitir un diagnóstico confiable.")

Creación_Matriz()
Diagnóstico()