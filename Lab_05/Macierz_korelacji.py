import numpy as np
import pandas as pd
import scipy.stats as stats

# Macierz korelacji
data = np.matrix([[1, 0.32, -0.67, -0.25, 0.27, -0.35, 0.15, -0.22, 0.54, 0.32],
              [0.32, 1, 0.17, 0.32, -0.25, 0.45, -0.28, -0.25, 0.67, 0.25],
              [-0.67, 0.17, 1, 0.25, 0.32, 0.25, 0.45, 0.35, 0.1, 0.63],
              [-0.25, 0.32, 0.25, 1, -0.32, 0.22, 0.31, 0.19, -0.28, 0.12],
              [0.27, -0.25, 0.32, -0.32, 1, 0.17, 0.26, -0.05, -0.15, -0.25],
              [-0.35, 0.45, 0.25, 0.22, 0.17, 1, 0.01, -0.3, 0.23, 0.36],
              [0.15, -0.28, 0.45, 0.31, 0.26, 0.01, 1, 0.23, 0.42, -0.25],
              [-0.22, -0.25, 0.35, 0.19, -0.05, -0.3, 0.23, 1, 0.25, 0.12],
              [0.54, 0.67, 0.1, -0.28, -0.15, 0.23, 0.42, 0.25, 1, 0.09],
              [0.32, 0.25, 0.63, 0.12, -0.25, 0.36, -0.25, 0.12, 0.09, 1]
              ])
R = pd.DataFrame(data, columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10'], index = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10'])

R0 = pd.DataFrame([[0.78, 0.3, -0.25, 0.35, 0.3, -0.37, -0.29, -0.29, 0.45, 0.1]], columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10'])

n = 50
alfa = 0.05
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









