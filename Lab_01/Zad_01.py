import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

dane = pd.read_excel("dane.xlsx")
dochod = dane["Dochód"]
mieso = dane["Spożycie mięsa"]


# test t
rxy, p_value = stats.pearsonr(dochod, mieso)
t_statistic = (abs(rxy) / np.sqrt(1 - rxy**2)) * np.sqrt(dane.shape[0] - 2)
alpha = 0.05
print(dane.shape[0])
t_emp = stats.t.ppf(1 - alpha, dane.shape[0] - 2)
print("Wartość statystyki t:", t_statistic)

alpha = 0.05
if abs(t_statistic) > t_emp:
    print("Odrzucamy hipotezę zerową - wartość współczynnika korelacji jest różna od zera.")
else:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej - współczynnik korealcji jest równy zero.")


# wykres
plt.figure(figsize = (10,8))
plt.scatter(dochod, mieso, color = "blue")
plt.xlabel("Dochód [zł]")
plt.ylabel("Spożycie mięsa [kg]")
plt.title("ZALEŻNOŚĆ SPOŻYCIA MIĘSA OD DOCHODÓW")
plt.show()