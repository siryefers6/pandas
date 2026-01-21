import pandas as pd

df = pd.read_csv('data.csv')

# Nota: El método corr() ignora las columnas "no numéricas".
print(df.corr())

"""Output
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.155408  0.009403  0.922721
Pulse    -0.155408  1.000000  0.786535  0.025120
Maxpulse  0.009403  0.786535  1.000000  0.203814
Calories  0.922721  0.025120  0.203814  1.000000
"""

"""
El resultado del método corr() es una tabla con numerosos números que representan la relación entre dos columnas. 

El número varía de -1 a 1.

1 significa que hay una relación de 1 a 1 (una correlación perfecta) y, para este conjunto de datos, cada vez que un valor aumentaba en la primera columna, el otro también aumentaba.

0,9 también es una buena relación, y si aumenta un valor, el otro probablemente también aumentará.

-0,9 sería una relación tan buena como 0,9, pero si aumenta un valor, el otro probablemente disminuirá.

0,2 significa NO una buena relación, lo que significa que si un valor aumenta no significa que el otro lo hará.

¿Qué es una buena correlación? Depende del uso, pero creo que se puede afirmar con seguridad que se necesita al menos 0,6 (o -0,6) para considerarla una buena correlación.
"""