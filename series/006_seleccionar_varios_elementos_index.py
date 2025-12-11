import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

# Utilice el argumento `index` y especifique solo los elementos que desea incluir en la Serie.
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

"""Output
day1    420
day2    380
dtype: int64
"""
