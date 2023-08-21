# Y -> Sprzedaż energii [MWh]
# X1 -> Długość linii przesyłowych [10000 km]
# X2 -> Liczba odbiorców [10000 osób]

import pandas as pd
import statsmodels.api as sm

data = pd.read_excel('data.xlsx')

X = data[['X1', 'X2']]  
X = sm.add_constant(X)  
Y = data['Y']

# Tworzenie modelu regresji liniowej
model = sm.OLS(Y, X)

# Dopasowanie modelu do danych
results = model.fit()

print(results.summary())

print()
print()
print()
print()

# Parametry
coefficients = results.params

# Reszty (residuals)
residuals = results.resid

# Odchyelnie standardowe reszt (Se)
std_residuals = residuals.std()

# R squared
r_squared = results.rsquared

# Błędy ocen parametrów
std_errors = results.bse

# Przedziały ufności (confidence interval)
conf_int_const = results.conf_int().loc['const']
conf_int_X1 = results.conf_int().loc['X1']
conf_int_X2 = results.conf_int().loc['X2']


print(f"Interpretacja parametru b1: Jeśli długość linii przesyłowych (X1) wzrośnie o jednostkę, czyli o 10000 km to sprzedaż energii (Y) wzrośnie średnio o {round(coefficients['X1'], 2)} mln MWh",
      "przy założeniu że liczba odbiorców (X2) się nie zmienia (ceteris paribus).")
print(f"Interpretacja parametru b2: Jeśli liczba odbiorców (X2) wzrośnie o jednostkę, czyli o 10000, to sprzedaż energii (Y) wzrośnie średnio o {round(coefficients['X2'], 2)} mln MWh,",
       "przy założeniu że długość linii przesyłowych się nie zmieni.")
print(f"Interpretacja odchylenia standardowego reszt (Se): Wartości empiryczne sprzedaży energii odchylają się przęciętne od {round(std_residuals, 2)} mln MWh",
       "od wartości teoretycznych wyznaczonych na podstawie modelu.")
print(f"Interpretacja R^2: {r_squared * 100}% całkowitej zmienności sprzedaży energii zostało wyjaśnionych modelem.")
print(f"Interpretacja współczynnika korelacji wielorakiej R: Empiryczne i teoretyczne wartości sprzedaży energii są skorelowane na poziomie {(round(r_squared ** (1/2) * 100, 3))}%")
print("Parametry beta1 i beta2 są statystycznie istotne (P>|t| jest mniejszy niż 0.05 dla X1 i X2)")
print()
print("Błędy ocen parametrów:")
print(f"- Ocena b0 różni się od parametru beta0 średnio o {round(std_errors['const'], 2)}")
print(f"- Ocena b1 różni się od parametru beta1 średnio o {round(std_errors['X1'], 2)}")
print(f"- Ocena b2 różni się od parametru beta2 średnio o {round(std_errors['X2'], 2)}")
print()
print("Interpretacje przedziałów ufności:")
print(f"- można sądzić na 95% że przedział od {round(conf_int_const[0], 2)} do {round(conf_int_const[1], 2)} obejmuje nieznaną wartość parametru beta0 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X1[0], 2)} do {round(conf_int_X1[1], 2)} obejmuje nieznaną wartość parametru beta1 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X2[0], 2)} do {round(conf_int_X2[1], 2)} obejmuje nieznaną wartość parametru beta2 ")


print()
print()
print()
print()


