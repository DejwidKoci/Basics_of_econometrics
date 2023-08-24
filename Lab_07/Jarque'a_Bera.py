import pandas as pd
import statsmodels.api as sm
from scipy import stats


def jarque_bera_test(data):
    
    # Obliczenie skośności (third moment) i kurtozy (fourth moment)
    skewness = stats.skew(residuals)
    kurtosis = stats.kurtosis(residuals)


    # Obliczenie statystyki testowej Jarque'a-Bera
    n = len(data)
    jb_statistic = (n / 6) * (skewness ** 2 + (1/4) * (kurtosis - 3) ** 2)

    # Obliczenie p-wartości na podstawie rozkładu chi-kwadrat
    p_value = 1 - stats.chi2.cdf(jb_statistic, df=2)
    
    return jb_statistic, p_value


data = pd.read_excel("data.xlsx", sheet_name = 'dane_01')
y = data['Wydatki']
X = data[['Dochody']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)
residuals = y - y_predicted


jb_statistic, p_value = jarque_bera_test(residuals)
print("Statystyka testu Jarque'a-Bera:", jb_statistic)
print("P-wartość:", p_value)


alpha = 0.05
if p_value < alpha:
    print("Odrzucamy hipotezę zerową - dane nie pochodzą z rozkładu normalnego.")
else:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej - dane mogą pochodzić z rozkładu normalnego.")
