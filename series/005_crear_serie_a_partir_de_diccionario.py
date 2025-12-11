import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

# Nota: Las claves del diccionario se convierten en las etiquetas.
myvar = pd.Series(calories)

print(myvar)

"""Output
day1    420
day2    380
day3    390
dtype: int64
"""
