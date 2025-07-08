from datetime import datetime

class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__mascotas = []

    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def mostrar_info(self):
        return f"Nombre: {self.__nombre} | Tel: {self.__telefono} | Correo: {self.__correo}"

    def get_nombre(self):
        return self.__nombre

    def get_mascotas(self):
        return self.__mascotas


class Mascota:
    def __init__(self, nombre, especie, raza, edad, propietario):
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__propietario = propietario
        self.__historial = []

    def agregar_cita(self, cita):
        self.__historial.append(cita)

    def mostrar_info(self):
        return f"{self.__nombre} ({self.__especie}, {self.__raza}, {self.__edad} años) - Dueño: {self.__propietario.get_nombre()}"

    def get_nombre(self):
        return self.__nombre

    def get_historial(self):
        return self.__historial


class CitaMedica:
    def __init__(self, fecha, motivo, diagnostico):
        self.__fecha = fecha
        self.__motivo = motivo
        self.__diagnostico = diagnostico

    def mostrar_info(self):
        return f" {self.__fecha} | Motivo: {self.__motivo} | Diagnóstico: {self.__diagnostico}"


class Veterinaria:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__clientes = []

    def buscar_cliente(self, nombre_cliente):
        for cliente in self.__clientes:
            if cliente.get_nombre().lower() == nombre_cliente.lower():
                return cliente
        return None

    def buscar_mascota(self, nombre_mascota):
        for cliente in self.__clientes:
            for mascota in cliente.get_mascotas():
                if mascota.get_nombre().lower() == nombre_mascota.lower():
                    return mascota
        return None

    def registrar_cliente(self):
        while True:
            nombre = input("Nombre del propietario: ").strip()
            telefono = input("Teléfono: ").strip()
            correo = input("Correo electrónico: ").strip()

            print(f"\nNombre: {nombre}\nTeléfono: {telefono}\nCorreo: {correo}")
            confirm = input("¿Desea guardar este cliente? (si/no): ").lower()
            if confirm == 'si':
                cliente = Cliente(nombre, telefono, correo)
                self.__clientes.append(cliente)
                print(" Cliente registrado.")
            else:
                print(" Registro cancelado.")

            if input("¿Agregar otro cliente? (s/n): ").lower() != 's':
                break

    def registrar_mascota(self):
        while True:
            nombre_prop = input("Nombre del propietario: ").strip()
            cliente = self.buscar_cliente(nombre_prop)
            if cliente:
                nombre = input("Nombre de la mascota: ").strip()
                especie = input("Especie: ").strip()
                raza = input("Raza: ").strip()
                edad = input("Edad: ").strip()

                print(f"\nMascota: {nombre}, Especie: {especie}, Raza: {raza}, Edad: {edad}")
                confirm = input("¿Desea guardar esta mascota? (si/no): ").lower()
                if confirm == 'si':
                    mascota = Mascota(nombre, especie, raza, edad, cliente)
                    cliente.agregar_mascota(mascota)
                    print("Mascota registrada.")
                else:
                    print("Registro cancelado.")
            else:
                print(" Cliente no encontrado.")

            if input("¿Agregar otra mascota? (s/n): ").lower() != 's':
                break


    def agendar_cita(self):
        while True:
            nombre_mascota = input("Nombre de la mascota: ").strip()
            mascota = self.buscar_mascota(nombre_mascota)
            if mascota:
                hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                while True:
                    try:
                        dia = int(input("Día (1-31): "))
                        if not (1 <= dia <= 31): raise ValueError("Día inválido.")
                        mes = int(input("Mes (1-12): "))
                        if not (1 <= mes <= 12): raise ValueError("Mes inválido.")
                        anio = int(input("Año (ej. 2025): "))
                        if anio < hoy.year: raise ValueError("Año inválido.")

                        fecha = datetime(anio, mes, dia)
                        if fecha < hoy:
                            print(" La fecha no puede ser menor a hoy.")
                            continue

                        fecha_str = fecha.strftime("%Y-%m-%d")
                        break
                    except ValueError as e:
                        print("Error:", e)
                    except:
                        print(" Fecha inválida.")

                diag_previo = ""
                motivo = ""
                tiene_diag = input("¿Ha tenido diagnóstico previo? (si/no): ").lower()
                if tiene_diag == 'si':
                    diag_previo = input("Diagnóstico previo: ").strip()
                    doctor = input("Doctor que refiere: ").strip()
                    motivo = input("Motivo actual de consulta: ").strip()
                    diagnostico = f"Previo: {diag_previo} (Dr. {doctor}) | Actual: {motivo}"
                else:
                    motivo = input("Motivo de la consulta: ").strip()
                    inicio = input("Inicio de los síntomas: ").strip()
                    diagnostico = f"Inicio síntomas: {inicio}"

                print(f"\nFecha: {fecha_str}\nMotivo: {motivo}\nDiagnóstico: {diagnostico}")
                confirm = input("¿Guardar esta cita? (s/n): ").lower()
                if confirm == 's':
                    cita = CitaMedica(fecha_str, motivo, diagnostico)
                    mascota.agregar_cita(cita)
                    print(" Cita registrada.")
                else:
                    print("Cita cancelada.")
            else:
                print("Mascota no registrada.")

            if input("¿Agendar otra cita? (s/n): ").lower() != 's':
                break

    def ver_historial_citas(self):
        while True:
            if not any(hcita.get_mascotas() for hcita in self.__clientes):
                print("AÚN NO HAY NINGÚN REGISTRO AGREGADO.\n")
            else:
                nombre = input("Nombre de la mascota: ").strip()
                mascota = self.buscar_mascota(nombre)
                if mascota:
                    print(f"\ Historial de {mascota.get_nombre()}:")
                    if mascota.get_historial():
                        for cita in mascota.get_historial():
                            print(" -", cita.mostrar_info())
                    else:
                        print("No hay citas registradas.")
                else:
                    print("Mascota no encontrada.")

            while True:

                    opcion = input("¿ Deseas volver al menú? (Si o No)?: ").lower()
                    if opcion == 'no':
                        print("Hasta pronto.  Mi voz por la tuya. ")
                        exit()
                    elif opcion == 'si':
                        return
                    else:
                        print("Opción incorrecta.")



    def mostrar_clientes_y_mascotas(self):
        while True:
            if not self.__clientes:
                print("No hay clientes registrados.")
            else:
                for cliente in self.__clientes:
                    print(cliente.mostrar_info())
                    if cliente.get_mascotas():
                        for mascota in cliente.get_mascotas():
                            print("  -", mascota.mostrar_info())
                    else:
                        print(" Sin mascotas.")

            opcion = input("¿ Deseas volver al menú? (Si o No)?: ").lower()
            if opcion == 'no':
                print(" ¡Hasta pronto!")
                exit()
            elif opcion == 'si':
                return
            else:
                print("Opción incorrecta.")

def mostrar_menu():
    print("\n MENÚ PRINCIPAL ")
    print("1. Registrar nuevo cliente")
    print("2. Registrar nueva mascota")
    print("3. Agendar cita")
    print("4. Ver historial de citas")
    print("5. Ver registros")
    print("0. Salir")
    print("-" * 40)

def main():
    sistema = Veterinaria("Clínica Veterinaria MI VOZ POR LA TUYA")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            sistema.registrar_cliente()
        elif opcion == "2":
            sistema.registrar_mascota()
        elif opcion == "3":
            sistema.agendar_cita()
        elif opcion == "4":
            sistema.ver_historial_citas()
        elif opcion == "5":
            sistema.mostrar_clientes_y_mascotas()
        elif opcion == "0":
            print(" ¡Gracias por usar el sistema veterinario!")
            break
        else:
            print(" Esta opción no es válida.")

if __name__ == "__main__":
    main()

