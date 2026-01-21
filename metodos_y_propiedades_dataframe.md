### Métodos y propiedades de **DataFrame** (en español)

| Propiedad / Método  | Descripción                                                         |
| ------------------- | ------------------------------------------------------------------- |
| `abs()`             | Devuelve un DataFrame con el valor absoluto de cada elemento        |
| `add()`             | Suma los valores del DataFrame con el/los valor(es) especificado(s) |
| `add_prefix()`      | Agrega un prefijo a todas las etiquetas                             |
| `add_suffix()`      | Agrega un sufijo a todas las etiquetas                              |
| `agg()`             | Aplica una función o nombre de función sobre un eje del DataFrame   |
| `aggregate()`       | Aplica una función o nombre de función sobre un eje del DataFrame   |
| `align()`           | Alinea dos DataFrames usando un método de unión especificado        |
| `all()`             | Devuelve `True` si todos los valores son `True`; si no, `False`     |
| `any()`             | Devuelve `True` si algún valor es `True`; si no, `False`            |
| `append()`          | Añade nuevas columnas                                               |
| `applymap()`        | Ejecuta una función en cada elemento del DataFrame                  |
| `apply()`           | Aplica una función sobre un eje del DataFrame                       |
| `assign()`          | Asigna nuevas columnas                                              |
| `astype()`          | Convierte el DataFrame a un tipo de dato especificado               |
| `at`                | Obtiene o asigna el valor del elemento con la etiqueta especificada |
| `axes`              | Devuelve las etiquetas de filas y columnas                          |
| `bfill()`           | Reemplaza valores nulos con el valor de la siguiente fila           |
| `bool()`            | Devuelve el valor booleano del DataFrame                            |
| `columns`           | Devuelve las etiquetas de las columnas                              |
| `combine()`         | Compara dos DataFrames y una función decide qué valores conservar   |
| `combine_first()`   | Rellena nulos del primero con valores del segundo DataFrame         |
| `compare()`         | Compara dos DataFrames y devuelve las diferencias                   |
| `convert_dtypes()`  | Convierte columnas a nuevos tipos de datos                          |
| `corr()`            | Calcula la correlación entre columnas                               |
| `count()`           | Devuelve el número de celdas no vacías por columna/fila             |
| `cov()`             | Calcula la covarianza de las columnas                               |
| `copy()`            | Devuelve una copia del DataFrame                                    |
| `cummax()`          | Calcula el máximo acumulado                                         |
| `cummin()`          | Calcula el mínimo acumulado                                         |
| `cumprod()`         | Calcula el producto acumulado                                       |
| `cumsum()`          | Calcula la suma acumulada                                           |
| `describe()`        | Devuelve un resumen descriptivo por columna                         |
| `diff()`            | Calcula la diferencia con el valor de la fila anterior              |
| `div()`             | Divide los valores del DataFrame                                    |
| `dot()`             | Multiplica con otro objeto tipo array y suma el resultado           |
| `drop()`            | Elimina filas/columnas especificadas                                |
| `drop_duplicates()` | Elimina valores duplicados                                          |
| `droplevel()`       | Elimina niveles de índice/columna                                   |
| `dropna()`          | Elimina filas con valores nulos                                     |
| `dtypes`            | Devuelve los tipos de datos de las columnas                         |
| `duplicated()`      | Devuelve `True` para filas duplicadas                               |
| `empty`             | Devuelve `True` si el DataFrame está vacío                          |
| `eq()`              | `True` si es igual al valor especificado                            |
| `equals()`          | `True` si dos DataFrames son iguales                                |
| `eval`              | Evalúa una cadena especificada                                      |
| `explode()`         | Convierte cada elemento en una fila                                 |
| `ffill()`           | Rellena nulos con el valor de la fila anterior                      |
| `fillna()`          | Reemplaza nulos con un valor especificado                           |
| `filter()`          | Filtra el DataFrame según un criterio                               |
| `first()`           | Devuelve las primeras filas de una selección por fecha              |
| `floordiv()`        | Divide y aplica división entera                                     |
| `ge()`              | `True` si es mayor o igual                                          |
| `get()`             | Devuelve el elemento de la clave especificada                       |
| `groupby()`         | Agrupa filas/columnas                                               |
| `gt()`              | `True` si es mayor                                                  |
| `head()`            | Devuelve las primeras filas                                         |
| `iat`               | Obtiene/asigna por posición                                         |
| `idxmax()`          | Devuelve la etiqueta del valor máximo                               |
| `idxmin()`          | Devuelve la etiqueta del valor mínimo                               |
| `iloc`              | Acceso por posiciones                                               |
| `index`             | Devuelve las etiquetas de las filas                                 |
| `infer_objects()`   | Infiera tipos de datos                                              |
| `info()`            | Muestra información del DataFrame                                   |
| `insert()`          | Inserta una columna                                                 |
| `interpolate()`     | Interpola valores NaN                                               |
| `isin()`            | `True` si el elemento está en un conjunto                           |
| `isna()`            | Detecta valores NaN                                                 |
| `isnull()`          | Detecta valores nulos                                               |
| `items()`           | Itera sobre columnas                                                |
| `iteritems()`       | Itera sobre columnas                                                |
| `iterrows()`        | Itera sobre filas                                                   |
| `itertuples()`      | Itera filas como tuplas                                             |
| `join()`            | Une columnas de otro DataFrame                                      |
| `last()`            | Devuelve las últimas filas por fecha                                |
| `le()`              | `True` si es menor o igual                                          |
| `loc`               | Acceso por etiquetas                                                |
| `lt()`              | `True` si es menor                                                  |
| `keys()`            | Devuelve las claves del eje de información                          |
| `kurtosis()`        | Calcula la curtosis                                                 |
| `mask()`            | Reemplaza valores donde la condición es `True`                      |
| `max()`             | Devuelve el máximo                                                  |
| `mean()`            | Devuelve la media                                                   |
| `median()`          | Devuelve la mediana                                                 |
| `melt()`            | Convierte de formato ancho a largo                                  |
| `memory_usage()`    | Devuelve el uso de memoria                                          |
| `merge()`           | Fusiona DataFrames                                                  |
| `min()`             | Devuelve el mínimo                                                  |
| `mod()`             | Calcula el módulo                                                   |
| `mode()`            | Devuelve la moda                                                    |
| `mul()`             | Multiplica valores                                                  |
| `ndim`              | Devuelve el número de dimensiones                                   |
| `ne()`              | `True` si es distinto                                               |
| `nlargest()`        | Devuelve las filas con valores más grandes                          |
| `notna()`           | Detecta valores no NaN                                              |
| `notnull()`         | Detecta valores no nulos                                            |
| `nsmallest()`       | Devuelve las filas con valores más pequeños                         |
| `nunique()`         | Cuenta valores únicos                                               |
| `pct_change()`      | Calcula el cambio porcentual                                        |
| `pipe()`            | Aplica una función al DataFrame                                     |
| `pivot()`           | Reestructura el DataFrame                                           |
| `pivot_table()`     | Crea una tabla dinámica                                             |
| `pop()`             | Elimina y devuelve un elemento                                      |
| `pow()`             | Eleva valores                                                       |
| `prod()`            | Devuelve el producto                                                |
| `product()`         | Devuelve el producto                                                |
| `quantile()`        | Devuelve cuantiles                                                  |
| `query()`           | Consulta el DataFrame                                               |
| `radd()`            | Suma inversa                                                        |
| `rdiv()`            | División inversa                                                    |
| `reindex()`         | Cambia etiquetas                                                    |
| `reindex_like()`    | Reindexa como otro DataFrame                                        |
| `rename()`          | Renombra ejes                                                       |
| `rename_axis()`     | Renombra un eje                                                     |
| `reorder_levels()`  | Reordena niveles de índice                                          |
| `replace()`         | Reemplaza valores                                                   |
| `reset_index()`     | Reinicia el índice                                                  |
| `rfloordiv()`       | División entera inversa                                             |
| `rmod()`            | Módulo inverso                                                      |
| `rmul()`            | Multiplicación inversa                                              |
| `round()`           | Redondea valores                                                    |
| `rpow()`            | Potencia inversa                                                    |
| `rsub()`            | Resta inversa                                                       |
| `rtruediv()`        | División real inversa                                               |
| `sample()`          | Devuelve una muestra aleatoria                                      |
| `sem()`             | Error estándar de la media                                          |
| `select_dtypes()`   | Selecciona columnas por tipo                                        |
| `shape`             | Devuelve filas y columnas                                           |
| `set_axis()`        | Define el eje                                                       |
| `set_flags()`       | Define banderas del DataFrame                                       |
| `set_index()`       | Define el índice                                                    |
| `size`              | Devuelve el número de elementos                                     |
| `skew()`            | Calcula la asimetría                                                |
| `sort_index()`      | Ordena por índice                                                   |
| `sort_values()`     | Ordena por valores                                                  |
| `squeeze()`         | Convierte a Series si es posible                                    |
| `stack()`           | Convierte de ancho a largo                                          |
| `std()`             | Desviación estándar                                                 |
| `sum()`             | Suma                                                                |
| `sub()`             | Resta                                                               |
| `swaplevel()`       | Intercambia niveles                                                 |
| `T`                 | Transpone filas y columnas                                          |
| `tail()`            | Devuelve las últimas filas                                          |
| `take()`            | Devuelve elementos especificados                                    |
| `to_xarray()`       | Convierte a xarray                                                  |
| `transform()`       | Ejecuta una función por valor                                       |
| `transpose()`       | Transpone                                                           |
| `truediv()`         | División real                                                       |
| `truncate()`        | Elimina elementos fuera de un rango                                 |
| `update()`          | Actualiza con otro DataFrame                                        |
| `value_counts()`    | Cuenta filas únicas                                                 |
| `values`            | Devuelve como array NumPy                                           |
| `var()`             | Varianza                                                            |
| `where()`           | Reemplaza donde la condición es `False`                             |
| `xs()`              | Devuelve una sección cruzada                                        |
| `__iter__()`        | Devuelve un iterador de ejes                                        |
