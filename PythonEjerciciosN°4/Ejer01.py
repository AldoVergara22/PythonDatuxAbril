import requests
import sqlite3

def funcion():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Explorar la estructura del JSON
            for key, value in data.items():
                print(key, value)  # Imprimir todas las claves y valores del JSON
            
            # Extraer y guardar los datos necesarios en la base de datos
            # Adaptar este código según la estructura real del JSON
            
            conn = sqlite3.connect('basedatos.db')
            cursor = conn.cursor()
            
            cursor.execute('CREATE TABLE IF NOT EXISTS tipo_cambio (fecha TEXT, compra REAL, venta REAL)')
            
            # Extraer y guardar los datos según la estructura real del JSON
            # Por ejemplo:
            if 'fecha' in data:
                fecha = data['fecha']
                compra = data['compra']
                venta = data['venta']
                
                cursor.execute('INSERT INTO tipo_cambio VALUES (?, ?, ?)', (fecha, compra, venta))
            
            conn.commit()
            conn.close()
            
            print('Los datos se han guardado exitosamente en la base de datos.')
        else:
            print('La solicitud a la API ha fallado con código de respuesta:', response.status_code)
    
    except requests.exceptions.RequestException as e:
        print('Ha ocurrido un error al realizar la solicitud a la API:', str(e))

funcion()