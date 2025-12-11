import pandas as pd

a = [1, 7, 2]

# Con el argumento de index, puedes nombrar tus propias etiquetas.
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

"""Output
x    1
y    7
z    2
dtype: int64
"""