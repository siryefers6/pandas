import pandas as pd

df = pd.read_csv('data.csv')

# Imprime mucha información sobre el DataFrame
print(df.info())

"""Output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
"""

"""Explicación del resultado

El resultado nos dice que hay 169 filas y 4 columnas:
```
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
```

Y el nombre de cada columna, con el tipo de dato:
```
#   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
0   Duration  169 non-null    int64  
1   Pulse     169 non-null    int64  
2   Maxpulse  169 non-null    int64  
3   Calories  164 non-null    float64
```

Valores null:
El método `info()` también nos indica cuántos valores No Nulos hay presentes en cada columna,
y en nuestro conjunto de datos parece que hay 164 de 169 valores No Nulos en la columna "Calorías".

Lo que significa que hay 5 filas sin valor alguno, en la columna de "Calorías", por la razón que sea.

Los valores vacíos, o valores nulos, pueden ser malos al analizar datos, Y deberías considerar eliminar
filas con valores vacíos. Esto es un paso hacia lo que se llama limpieza de datos, Y aprenderéis más 
sobre eso en los próximos capítulos.
"""
