import os
import sys
import time
import pandas as pd

# Nombre del archivo de Excel
EXCEL_FILE = "empleados.xlsx"


def ejecutar_simulacion():
    print("==================================================")
    print("   SIMULADOR DE CHATBOT - GESTIÓN DE VACACIONES   ")
    print("==================================================")
    time.sleep(0.5)

    print("\n[Bot]: Hola! Bienvenido al sistema de gestion de vacaciones.")
    print("[Bot]: Escriba 'salir' en cualquier momento para terminar.")

    while True:
        print("\n[Bot]: Por favor, ingrese su numero de DNI (sin puntos):")
        dni_input = input("Usuario: ").strip()

        # Permitir salir de la simulacion
        if dni_input.lower() == "salir":
            print("\n[Sistema]: Simulacion finalizada por el usuario.")
            sys.exit()

        # Validacion: Verificar que sean solo numeros
        if not dni_input.isdigit():
            print("\n[Bot - ERROR]: El DNI debe contener solo numeros.")
            print("[Bot]: Intente de nuevo.")
            continue

        # Validacion: Verificar el largo del DNI
        if len(dni_input) < 7 or len(dni_input) > 9:
            print("\n[Bot - ERROR]: El DNI debe tener entre 7 y 9 digitos.")
            print("[Bot]: Intente de nuevo.")
            continue

        break

    print("\n[Sistema]: Buscando DNI en el archivo Excel...")
    time.sleep(1)

    try:
        # Si el archivo no existe en el celular, usa estos datos de prueba
        if not os.path.exists(EXCEL_FILE):
            data = {
                "DNI": [12345678, 23456789, 34567890],
                "Nombre": ["Juan Perez", "Maria Lopez", "Carlos Diaz"],
                "Dias_Disponibles": [15, 10, 0],
            }
            df = pd.DataFrame(data)
        else:
            df = pd.read_excel(EXCEL_FILE)

        # Convertimos el DNI ingresado a numero para buscarlo
        dni_buscado = int(dni_input)

        # Buscamos la fila del empleado
        empleado = df[df["DNI"] == dni_buscado]

        # REGLA DE NEGOCIO 1: ¿El empleado existe?
        if not empleado.empty:
            nombre = empleado.iloc[0]["Nombre"]
            dias_vacaciones = int(empleado.iloc[0]["Dias_Disponibles"])

            print(f"\n[Bot]: Empleado encontrado: {nombre}")

            # REGLA DE NEGOCIO 2: ¿Tiene dias disponibles?
            if dias_vacaciones > 0:
                print(f"\n[Bot - SOLICITUD APROBADA]: Felicidades {nombre}!")
                print(f"[Bot]: Usted tiene {dias_vacaciones} dias disponibles.")
            else:
                print(f"\n[Bot - SOLICITUD RECHAZADA]: Lo sentimos {nombre}.")
                print("[Bot]: No le quedan dias de vacaciones (Saldo: 0).")
        else:
            print(
                f"\n[Bot - RECHAZO]: El DNI {dni_buscado} no esta en el sistema."
            )
            print("[Bot]: Por favor, consulte con Recursos Humanos.")

    except Exception as e:
        print(f"\n[Error del Sistema]: Ocurrio un problema: {e}")

    print("\n==================================================")
    print("         SIMULACION FINALIZADA CON EXITO          ")
    print("==================================================")


if __name__ == "__main__":
    ejecutar_simulacion()
