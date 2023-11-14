import datetime

fecha_actual = datetime.datetime.now() #Fecha actual

fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")   #datetime (1997,12,13) #Fecha de nacimiento

fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")

edad = fecha_actual.year - fecha_nacimiento.year

print ("Tu edad es:" , edad, "años")

fecha_cumpleanios = datetime.datetime(fecha_actual.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)

diferencia = fecha_cumpleanios - fecha_actual
segundos_faltantes= diferencia.total_seconds()

print("faltan", int(segundos_faltantes), "segundos para tu proximo cumpleanios.")





