import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

# Usa una lista de índices:
print(df.loc[[0, 1]])

# Nota: Al utilizar [], el resultado es un Pandas DataFrame.
"""Output
   calories  duration
0       420        50
1       380        40
2       390        45
   calories  duration
0       420        50
1       380        40
"""
