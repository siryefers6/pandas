import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# Cargar datos en objeto DataFrame
df = pd.DataFrame(data)

print(df)

"""Output
   calories  duration
0       420        50
1       380        40
2       390        45
"""
