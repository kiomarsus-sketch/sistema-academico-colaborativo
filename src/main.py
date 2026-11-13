"""Punto de entrada de la aplicación académica de demostración."""
from src.estudiantes import registrar_estudiante


def main():
    estudiantes = []
    print("=== TecnoAula: registro académico de demostración ===")
    while True:
        print("\n1. Registrar estudiante")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre completo: ")
            programa = input("Programa de estudios: ")
            try:
                estudiante = registrar_estudiante(
                    estudiantes, codigo, nombre, programa
                )
                print(f"Registrado: {estudiante['nombre']} ({estudiante['codigo']})")
            except ValueError as error:
                print(f"Error: {error}")
        elif opcion == "0":
            print("Fin de la demostración.")
            break
        else:
            print("Opción no válida. Seleccione 1 o 0.")


if __name__ == "__main__":
    main()
