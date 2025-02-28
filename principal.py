import numeros
import os
import time  

def menu():
    """Muestra el menú de opciones y obtiene la selección del usuario."""
    os.system("cls" if os.name == "nt" else "clear")  
    print("📋 Bienvenido al Turnero de la Farmacia")
    print("1️⃣ Perfumería")
    print("2️⃣ Farmacia")
    print("3️⃣ Cosmética")
    print("0️⃣ Salir")
    opcion = input("Seleccione el área deseada: ")
    return opcion

def main():
    while True:
        opcion = menu()
        
        if opcion == "1":
            numeros.obtener_turno_perfumeria()
        elif opcion == "2":
            numeros.obtener_turno_farmacia()
        elif opcion == "3":
            numeros.obtener_turno_cosmetica()
        elif opcion == "0":
            print("👋 ¡Gracias por usar el turnero de la farmacia! Hasta luego.")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

        time.sleep(3)  
        os.system("cls" if os.name == "nt" else "clear")  

if __name__ == "__main__":
    main()

