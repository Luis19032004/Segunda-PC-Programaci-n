
def Registrar_Alumno(estudiantes):

    Código = str(input("Ingrese el codigo del alumno: "))
    Nombre = str(input("Ingrese el nombre del alumno: "))
    Género = str(input("Ingrese el género del alumno (M o F): "))

    Edad = int(input("Ingrese la edad del alumno: "))
    Curso_1 = float(input("Ingrese la nota del curso 1: "))
    Curso_2 = float(input("Ingrese la nota del curso 2: "))
    Curso_3 = float(input("Ingrese la nota del curso 3: "))

    Promedio = (Curso_1 + Curso_2 + Curso_3)/3
    Estudiante = {"codigo": Código,"nombre": Nombre,"genero": Género,"edad": Edad,"curso1": Curso_1,"curso2": Curso_2,"curso3": Curso_3,"promedio": Promedio}
    estudiantes.append(Estudiante)

def Imprimir_Estudiantes(estudiantes):
    for estudiante in estudiantes:
        print(f"Codigo: {estudiante["codigo"]},   Nombre: {estudiante["nombre"]},   Género: {estudiante["genero"]},   Edad: {estudiante["edad"]} ")

def Imprimir_Notas(estudiantes):
    for estudiante in estudiantes:
        print(f"Codigo: {estudiante["codigo"]},   Nombre: {estudiante["nombre"]},   Curso 1: {estudiante["curso1"]},   Curso 2: {estudiante["curso2"]},    Curso 3: {estudiante["curso3"]}")

def Imprimir_Prom(estudiantes):
    for estudiante in estudiantes:
        print(f"Codigo: {estudiante["codigo"]},   Nombre: {estudiante["nombre"]},   Promedio: {estudiante["promedio"]:.2f}")

def Imprimir_PyU(estudiantes):
    if estudiantes:
        primero = estudiantes[0]
        ultimo = estudiantes[-1]
        print("Primero en la lista:")
        print(f"Código: {primero["codigo"]}, Nombre: {primero["nombre"]},Género: {primero["genero"]}, Edad: {primero["edad"]},Promedio: {primero["promedio"]:.2f}")
    
        print("Último en la lista:")
        print(f"Código: {ultimo["codigo"]}, Nombre: {ultimo["nombre"]},Género: {ultimo["genero"]}, Edad: {ultimo["edad"]},Promedio: {ultimo["promedio"]:.2f}")
    else:
        print("No hay alumnos registrados.")

while True:
    estudiantes = []

    while True:
        print("\n---------------Menú de opciones---------------")
        print("1. Registrar datos")
        print("2. Ver lista de alumnos")
        print("3. Ver notas por asignatura")
        print("4. Calcular promedios")
        print("5. Mostrar primero y último")
        print("6. Salir\n")
        print("")
        opcion = str(input("Seleccione una opción: "))

        if opcion == "1":
            Registrar_Alumno(estudiantes)
        elif opcion == "2":
            Imprimir_Estudiantes(estudiantes)
        elif opcion == "3":
            Imprimir_Notas(estudiantes)
        elif opcion == "4":
            Imprimir_Prom(estudiantes)
        elif opcion == "5":
            Imprimir_PyU(estudiantes)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Error: Opción inválida. Inténtelo de nuevo.")
