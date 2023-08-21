import numpy as np
import pandas as pd
import scipy.stats as stats

# Macierz korelacji
data = np.matrix([[1, -0.09, 0.35, -0.17, -0.62, -0.4, -0.16, -0.55],
                  [-0.09, 1, -0.06, -0.38, 0, 0.15, 0.22, 0.11],
                  [0.35, -0.06, 1, 0.33, -0.11, -0.2, -0.45, -0.02],
                  [-0.17, -0.38, 0.33, 1, 0.2, -0.07, -0.44, 0.07],
                  [-0.62, 0, -0.11, 0.2, 1, 0.22, 0.17, -0.11],
                  [-0.4, 0.15, -0.2, -0.07, 0.22, 1, -0.19, 0.05],
                  [-0.16, 0.22, -0.45, -0.44, 0.17, -0.19, 1, 0.05],
                  [-0.55, 0.11, -0.02, 0.07, -0.11, 0.47, 0.05, 1]
              ])
R = pd.DataFrame(data, columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8'], index = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8'])

R0 = pd.DataFrame([[-0.59, -0.06, 0.08, 0.13, 0.54, -0.15, -0.1, 0.79]], columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8'])

n = 28
alfa = 0.1
t_critical = stats.t.ppf(1 - alfa/2, n - 2)
r_critical = ((t_critical ** 2) / (t_critical ** 2 + n - 2)) ** (1/2)
final_variables = []
good = []
finish = False 

R0 = R0.applymap(lambda x: x if abs(x) > r_critical else np.nan)
h = R0.stack().idxmax()
final_variables.append(h[1])

# Szukanie indeksów kolumn, które mają przynajmniej jedno NaN w R0
columns_with_nan = R0.columns[R0.isna().any()]

# Usunięcie kolumn z R0, które zawierają wartości NaN
R0_filtered = R0.drop(columns=columns_with_nan)

# Usunięcie odpowiednich wierszy i kolumn z macierzy R
indices_to_drop = R0.columns.get_indexer_for(R0_filtered.columns)
R = R.iloc[indices_to_drop, indices_to_drop]

R0[h[1]] = np.nan
step = R[h[1]]
good = step[abs(step) <= r_critical]

R0 = R0[good.index]

while(finish == False):
    if len(good) == 0:
        finish = True
        break

    if len(good) == 1:
        finish = True
        final_variables.append(good.index[0])
        break

    # Indeks maksymalnego elementu w całym DataFrame
    h = R0.stack().idxmax()
    R0[h[1]] = np.nan
    R = R.loc[good.index, good.index]
        
    step = R[h[1]]
    good = step[abs(step) <= r_critical]
    final_variables.append(h[1])

    
    

print(final_variables)









