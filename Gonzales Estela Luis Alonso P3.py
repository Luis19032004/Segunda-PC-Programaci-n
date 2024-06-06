def Ingreso_nota(nota_num):
    while True:
        nota = float(input(f"Ingrese la nota {nota_num} (0 a 20): "))
        if 0 <= nota <= 20:
            return nota
        else:
            print("La nota debe estar entre 0 y 20. Inténtelo de nuevo.")

def Imprimir(estudiantes):
    for estudiante in estudiantes:
        print(f"Código: {estudiante["Código"]}, Nombre: {estudiante["Nombre"]}")
        print(f"Nota 1: {estudiante["Nota_1"]}, Nota 2: {estudiante["Nota_2"]}")
        print(f"Nota 3: {estudiante["Nota_3"]}, Promedio: {estudiante["Promedio"]:.2f}")

while True:
    Alumnos = []
    N = int(input("Ingrese la cantidad de estudiantes (Pulse 0 para cerrar el programa): "))

    if N == 0:
        break
    
    else:

        for i in range(N):
            Código = int(input("Ingrese el código del estudiante (solo números): "))

            Nombre = input("Ingrese el nombre del estudiante: ")
        
            Nota_1 = Ingreso_nota(1)
            Nota_2 = Ingreso_nota(2)
            Nota_3 = Ingreso_nota(3)

            Promedio = (Nota_1 + Nota_2 + Nota_3) / 3
            estudiante = {"Código": Código,"Nombre": Nombre,"Nota_1": Nota_1,"Nota_2": Nota_2,"Nota_3": Nota_3,"Promedio": Promedio}
            Alumnos.append(estudiante)

        desaprobados = sum(1 for estudiante in Alumnos if estudiante["Promedio"] < 10.5)

        print("\nPromedios de los estudiantes:")
        Imprimir(Alumnos)

        print(f"\nCantidad de estudiantes desaprobados: {desaprobados}")

        Alumnos.sort(key=lambda x: x["Promedio"], reverse=True)

        print("\nEstudiantes ordenados por promedio:")
        Imprimir(Alumnos)