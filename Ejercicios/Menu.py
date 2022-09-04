import os

from main import Menu

main = Menu()

lista = ["1. Python", "2. Modulo","3. Paquete" ,"4. POO", "5. Terminar Ciclo"]
opc = ""

while opc != "5":
    os.system("cls")
    opc = main.menu(lista, "Menu")
    os.system("cls")
    if opc == '1':
        opc=""
        while opc != "7":
            os.system("cls")
            print("PYTHON")
            opc = main.menu(["1. Ejercicio 1", "...", "...", "...", "24. Ejercicio 25", "Exit Para Salir"],
                              "Elija un ejercicio del 1 al 25")
            os.system("cls")

            if opc == "1":
                os.system("cls")
                print("Exit para Terminar el ciclo")
                print("Has elegido La Opcion 1 Ejercicio 1") 
                import Ejercicio1
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "2":
                os.system("cls")
                print("Has elegido La Opcion 2 Ejercicio 2") 
                print("\n"
                "Variables"
                "\n") 
                import Ejercicio2
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "3":
                os.system("cls")
                print("Has elegido La Opcion 3 Ejercicio 3")
                print("\n"
                "Conversiones"
                "\n")
                import Ejercicio3
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "4":
                os.system("cls")
                print("Has elegido La Opcion 4 Ejercicio 4") 
                print("\n"
                "Operaciones Matematicas"
                "\n")
                import Ejercicio4
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "5":
                os.system("cls")
                print("Has elegido La Opcion 5 Ejercicio 5") 
                print("\n"
                "Concatenación"
                "\n")
                import Ejercicio5
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "6":
                os.system("cls")
                print("Has elegido La Opcion 6 Ejercicio 6")
                print("\n"
                "Cadenas"
                "\n") 
                import Ejercicio6
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "7":
                os.system("cls")
                print("Has elegido La Opcion 7 Ejercicio 7") 
                print("\n"
                "Tuplas"
                "\n")
                import Ejercicio7
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "8":
                os.system("cls")
                print("Has elegido La Opcion 8 Ejercicio 8") 
                print("\n"
                "Listas"
                "\n")
                import Ejercicio8
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "9":
                os.system("cls")
                print("Has elegido La Opcion 9 Ejercicio 9") 
                print("\n"
                "Diccionarios"
                "\n")
                import Ejercicio9
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "10":
                os.system("cls")
                print("Has elegido La Opcion 10 Ejercicio 10") 
                print("\n"
                "Ingreso De Datos"
                "\n")
                import Ejercicio10
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "11":
                os.system("cls")
                print("Has elegido La Opcion 11 Ejercicio 11") 
                print("\n"
                "Condicional IF, ELSE, ELIF"
                "\n")
                import Ejercicio11
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "12":
                os.system("cls")
                print("Has elegido La Opcion 12 Ejercicio 12") 
                print("\n"
                "Funciones"
                "\n")
                import Ejercicio12
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "13":
                os.system("cls")
                print("Has elegido La Opcion 13 Ejercicio 13")
                print("\n"
                "Operadores Logicos"
                "\n")
                import Ejercicio13
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "14":
                os.system("cls")
                print("Has elegido La Opcion 14 Ejercicio 14")
                print("\n"
                "Operadores Ternarios"
                "\n")
                import Ejercicio14
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "15":
                os.system("cls")
                print("Has elegido La Opcion 15 Ejercicio 15")
                print("\n"
                "IF con Tuplas y Listas"
                "\n")
                import Ejercicio15
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "16":
                os.system("cls")
                print("Has elegido La Opcion 16 Ejercicio 16")
                print("\n"
                "Funcion Ragnge"
                "\n")
                import Ejercicio16
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "17":
                os.system("cls")
                print("Has elegido La Opcion 17 Ejercicio 17")
                print("\n"
                "Bucle For"
                "\n")
                import Ejercicio17
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "18":
                os.system("cls")
                print("Has elegido La Opcion 18 Ejercicio 18")
                print("\n"
                "Factorial de un Numero"
                "\n")
                import Ejercicio18
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "19":
                os.system("cls")
                print("Has elegido La Opcion 19 Ejercicio 19")
                print("\n"
                "Bucle Wile"
                "\n")
                import Ejercicio19
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "20":
                os.system("cls")
                print("Has elegido La Opcion 20 Ejercicio 20")
                print("\n"
                "Breack, Continue, Pass"
                "\n")
                import Ejercicio20
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "21":
                os.system("cls")
                print("Has elegido La Opcion 21 Ejercicio 21")
                print("\n"
                "Generadores"
                "\n")
                import Ejercicio21
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "22":
                os.system("cls")
                print("Has elegido La Opcion 22 Ejercicio 22")
                print("\n"
                "Generadores2"
                "\n")
                import Ejercicio22
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "23":
                os.system("cls")
                print("Has elegido La Opcion 23 Ejercicio 23")
                print("\n"
                "Exepciones"
                "\n")
                import Ejercicio23
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "24":
                os.system("cls")
                print("Has elegido La Opcion 24  Ejercicio 24")
                print("\n"
                "Sentencia RAISE"
                "\n")
                import Ejercicio24
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "Exit":
                input("Saliendo..."
                "\n" "Presione una tecla para continuar...")
                break
            elif opc == "exit":
                input("Saliendo..."
                "\n" "Presione una tecla para continuar...")
                break



    if opc == '2':
        opc=""
        while opc != "7":
            os.system("cls")
            print("MODULO")
            opc = main.menu(["1) Ejercicio 1", "Exit para Salir"],"Elija una opción")
            os.system("cls")

            if opc == "1":
                os.system("cls")
                print("Has elegido La Opcion 1  Ejercicio 1")
                print("\n"
                "funciones Matemáticas"
                "\n")
                from Modulo import funcionesMatematicas
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            
            elif opc == "Exit":
                input("Saliendo..."
                "\n" "Presione una tecla para continuar...")
                break
            elif opc == "exit":
                input("Saliendo..."
                "\n" "Presione una tecla para continuar...")
                break



    if opc == '3':
        opc=""
        while opc != "7":
            os.system("cls")
            print("PAQUETE")
            opc = main.menu(["1) Ejercicio 1", "Exit para Salir"],"Elija una opción")
            os.system("cls")
            if opc == "1":
                os.system("cls")
                print("Has elegido La Opcion 1  Ejercicio 1")
                print("\n"
                "Prueba de Paquetes"
                "\n")
                import PruebaPaquete
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "Exit":
                input("Saliendo..."
                "\n" "Presione una tecla para continuar...")
                break
            elif opc == "exit":
                input("Saliendo..."
                "\n" "Presione una tecla para continuar...")
                break



    if opc == '4':
        opc=""
        while opc != "7":
            os.system("cls")
            print("POO")
            opc = main.menu(["1. Ejercicio 1", "...", "...", "7. Ejercicio 7", "Exit para Salir"],"Elija una opción del 1 al 7")
            os.system("cls")
            if opc == "1":
                os.system("cls")
                print("Has elegido La Opcion 1  Ejercicio 1")
                print("\n"
                "Persona"
                "\n")
                from POO import Persona
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            if opc == "2":
                os.system("cls")
                print("Has elegido La Opcion 2  Ejercicio 2")
                print("\n"
                "Curso"
                "\n")
                from POO import Curso
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            if opc == "3":
                os.system("cls")
                print("Has elegido La Opcion 3  Ejercicio 3")
                print("\n"
                "Cuenta"
                "\n")
                from POO import Cuenta
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            if opc == "4":
                os.system("cls")
                print("Has elegido La Opcion 4  Ejercicio 4")
                print("\n"
                "Herencia"
                "\n")
                from POO import Herencia
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            if opc == "5":
                os.system("cls")
                print("Has elegido La Opcion 5  Ejercicio 5")
                print("\n"
                "Herencia Multiple"
                "\n")
                from POO import HerenciaMultiple
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            if opc == "6":
                os.system("cls")
                print("Has elegido La Opcion 6  Ejercicio 6")
                print("\n"
                "Polimorfismo"
                "\n")
                from POO import Polimorfismo
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            if opc == "7":
                os.system("cls")
                print("Has elegido La Opcion 7  Ejercicio 7")
                print("\n"
                "Relaciones Clases"
                "\n")
                from POO import RelacionesClases
                print("\n"
                "Fin del Ejercicio")
                input("\n"
                "Presiona una tecla para continuar:)")
                os.system("cls")

            elif opc == "Exit":
                input("Saliendo..."
                "\n" "Presione una tecla para continuar...")
                break
            elif opc == "exit":
                input("Saliendo..."
                "\n" "Presione una tecla para continuar...")
                break