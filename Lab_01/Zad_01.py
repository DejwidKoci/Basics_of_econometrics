import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

dane = pd.read_excel("dane.xlsx")
dochod = dane["Dochód"]
mieso = dane["Spożycie mięsa"]


# test t
t_statistic, p_value = stats.ttest_ind(dochod, mieso)

print("Wartość statystyki t:", t_statistic)
print("Wartość p:", p_value)

alpha = 0.05
if p_value < alpha:
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