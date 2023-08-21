import pandas as pd
import scipy.stats as stats
import numpy as np

data = pd.read_excel("dane.xlsx", sheet_name = "data_02")
x = data["Zużycie surowca"]
y = data["Produkcja"]

b1, b2, r, p, std_error = stats.linregress(x, y)
#b1, b2 = np.polyfit(x, y, 1)

y_pred = b1 * x + b2
y_mean = np.mean(y)
r_squared = np.sum((y_pred - y_mean) ** 2) / np.sum((y - y_mean)**2) 

n = data.shape[0]
k = 1
se = np.sqrt(np.sum((y - y_pred) ** 2) / (n - k - 1))

mae = np.mean(np.abs(y_pred-y))
wzl = se / y_mean

f = (n - k - 1) / k * r_squared/(1 - r_squared)
f_s = stats.f.ppf(1 - 0.05, k, n - 2)




print(f"Model: {round(b1,2)}x {round(b2,2)}")
#print(f"Model: {round(b1,2)}x + {round(b2,2)}")
print(f"Interpretacja parametru b1: Jeśli zużycie surowca wzrośnie o jednostkę to produkcja wzrośnie średnio o {b1} jednostkę")
print("R-value: ", r)
print("p-value: ", p)
print("Standard error of the parametr: ", std_error)
print(f"R-squared: {r_squared}, zatem {r_squared} całkowitej zmienności produkcji (y) zostało wyjaśnione modelem. " )
print(f"Standard error: {se}, zatem wartości empiryczne produkcji (y) odchylają się przeciennie (średnio)" 
      f" o {se} jednostek od wartości teoretycznych wyznaczonych na podstawie modelu")
print(f"Min absolute error: {mae}, czyli średnia z wartości bezwzględnych reszt wynosi {mae}")
print(f"Coefficient of random variation: {wzl}. Odchylenie standardowe reszt stanowi {wzl * 100}% średniej wartości produkcji."
      "Dopasowanie modelu można uznać za dostatecznie dobre")
print("Test F: ", end = "")
if f > f_s:
    print("Odrzucamy hipotezę zerową: parametr jest statystycznie isototny")
else:
    print("Brak podstaw do odrzucenia: parametr jest statystycznie nieistotny")
