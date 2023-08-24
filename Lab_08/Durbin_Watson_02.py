import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson

data = pd.read_excel("data.xlsx", sheet_name = 'dane_02')
y = data['y']
X = data[['x1','x2']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)

residuals = y - y_predicted

d_value = durbin_watson(residuals)

print("Wynik testu Durbina-Watsona:")
print(f"Wartość statystyki Durbina-Watsona: {d_value}")

if d_value < 1.5:
    interpretation = "Wartość statystyki Durbina-Watsona poniżej 1.5 sugeruje obecność silnej autokorelacji dodatniej."
elif d_value > 2.5:
    interpretation = "Wartość statystyki Durbina-Watsona powyżej 2.5 sugeruje obecność silnej autokorelacji ujemnej."
elif 1.5 <= d_value <= 2.5:
    interpretation = "Wartość statystyki Durbina-Watsona w zakresie 1.5-2.5 wskazuje na brak istotnej autokorelacji."

print("Interpretacja:")
print(interpretation)