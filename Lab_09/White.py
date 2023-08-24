import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_white


data = pd.read_excel('data.xlsx', sheet_name = 'dane_03')
y = data['Y']
X = data[['X1', 'X2']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
residuals = model.resid


test_result = het_white(residuals, X)
test_statistic = test_result[0]
p_value = test_result[1]

print("Statystyka testu White'a:", test_statistic)
print("P-wartość:", p_value)


alpha = 0.05
if p_value < alpha:
    print("Odrzucamy hipotezę zerową - istnieją dowody na heteroskedastyczność reszt.")
else:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej - reszty są homoskedastyczne.")
