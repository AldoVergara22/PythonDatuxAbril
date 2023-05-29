import pandas as pd
# Cargar archivos CSV
df1 = pd.read_csv('F:/archivo.csv',header= None)
df2 = pd.read_csv('F:/archivo2.csv',header= None)

# Cambiar el formato de comas(por defecto) a uno espaciado
df1 = df1.replace(';', '\t', regex=True)
df1.to_csv('datos_modificados1.csv', index=False)

#Cargar el archivo modificado que nos creo VisualStudio
df3 = pd.read_csv('F:/datos_modificados1.csv',header= None)





#Cargar los nuevos archivos CSV
# Realizar la operación de merge en base a la columna 'Promedios'
#df_merged = pd.merge(df1, df2, on='Promedios', how='inner')

# Mostrar el resultado del merge
#print(df_merged)