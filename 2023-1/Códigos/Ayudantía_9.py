import pandas as pd

def leer_dataframe(ruta):
    dataframe = pd.read_csv(ruta, sep=";")
    return dataframe

def añadir_registro(dataframe, registro, ruta):
    dataframe.loc[len(dataframe)] = nuevo_registro
    dataframe.to_csv("prueba.csv", sep=";", index=False)
    return None

def ultimos_10(dataframe):
    ultimos_registros_correctos = dataframe[dataframe['correcto'] == 'Correcto'].tail(10)
    return ultimos_registros_correctos

ruta="prueba.csv"
df=leer_dataframe(ruta)

nuevo_registro = ["Diego", "Prueba", "Correcto"]
añadir_registro(df, nuevo_registro, ruta)

ultimos_10_correctos=ultimos_10(df)
print(ultimos_10_correctos)

veces_jugadas=len(df)
print(veces_jugadas)