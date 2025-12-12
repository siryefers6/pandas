import pandas as pd

df = pd.read_csv('data.csv')

# Visualizar las primeras 10 rows del DataFrame:
print(df.head(10))

# Si no se especifica cantidad en el argumento head() imprime las primeras 5 rows
"""Output
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
5        60    102       127     300.5
6        60    110       136     374.0
7        45    104       134     253.3
8        30    109       133     195.1
9        60     98       124     269.0
"""
