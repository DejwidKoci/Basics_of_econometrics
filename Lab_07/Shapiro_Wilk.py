import pandas as pd
import statsmodels.api as sm
from scipy.stats import shapiro

data = pd.read_excel("data.xlsx", sheet_name = 'dane_01')
y = data['Wydatki']
X = data[['Dochody']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)

residuals = y - y_predicted

statistic, p_value = shapiro(residuals)
alfa = 0.05

print("Wynik testu Shapiro-Wilka:")
print(f"Statystyka testowa: {statistic}")
print(f"P-wartość: {p_value}")

if p_value > alfa:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej: Dane pochodzą z rozkładu normalnego.")
else:
    print("Odrzucamy hipotezę zerową: Dane nie pochodzą z rozkładu normalnego.")