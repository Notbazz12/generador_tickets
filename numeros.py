def decorador_turno(func):
    """Decorador que añade texto antes y después del número de turno."""
    def wrapper():
        print("Tu turno es: ")
        turno = func()
        print(f"Turno: {turno}")
        print("Espere y sera atendido ")
        return turno
    return wrapper
    
def generador_turnos(letra):
    """Generador que devuelve turnos consecutivos con la letra del área."""
    numero = 1
    while True:
        yield f"{letra}-{numero}"
        numero += 1

#instancias para el generador
turno_perfumeria = generador_turnos("P")
turno_farmacia = generador_turnos("F")
turno_cosmetica = generador_turnos("C")

#funciones para obtener turnos
@decorador_turno
def obtener_turno_perfumeria():
    return next(turno_perfumeria)

@decorador_turno
def obtener_turno_farmacia():
    return next(turno_farmacia)

@decorador_turno
def obtener_turno_cosmetica():
    return next(turno_cosmetica)