import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.api import het_goldfeldquandt

data = pd.read_excel('data.xlsx', sheet_name = 'dane_02')
y = data['Y']
X = data[['X']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)

residuals = y - y_predicted

test_result = het_goldfeldquandt(residuals, X)

print("Wynik testu Goldfelda-Quandta:")
print("Statystyka testowa:", test_result[0])
print("P-wartość:", test_result[1])

alpha = 0.05  

if test_result[1] > alpha:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej: Reszty są homoskedastyczne.")
else:
    print("Odrzucamy hipotezę zerową: Reszty nie są homoskedastyczne.")
