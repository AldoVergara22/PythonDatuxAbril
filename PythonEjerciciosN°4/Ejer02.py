from datetime import datetime
def registrar_evento(nombre_archivo, nombre_evento):
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
    registro = f"{fecha_formateada}-{nombre_archivo}-{nombre_evento}\n"
    
    with open('info.log', 'a') as archivo_log:
        archivo_log.write(registro)

nombre_archivo = "Autos economicos"
nombre_evento = "Exposicion de Automoviles"
registrar_evento(nombre_archivo, nombre_evento)
