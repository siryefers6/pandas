import pandas as pd

df = pd.read_csv('data.csv')

# Imprime las últimas 5 rows del DataFrame por defecto
print(df.tail())

"""Output
     Duration  Pulse  Maxpulse  Calories
164        60    105       140     290.8
165        60    110       145     300.4
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
"""
