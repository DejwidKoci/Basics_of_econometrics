import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

dane = pd.read_excel("dane.xlsx", sheet_name = "data_02")
produkcja = dane["Produkcja"]
surowiec = dane["Zużycie surowca"]


# test t
t_statistic, p_value = stats.ttest_ind(produkcja, surowiec)

print("Wartość statystyki t:", t_statistic)
print("Wartość p:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Odrzucamy hipotezę zerową - wartość współczynnika korelacji jest różna od zera.")
else:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej - współczynnik korealcji jest równy zero.")

# wykres
plt.figure(figsize = (10,8))
plt.scatter(produkcja, surowiec, color = "red")
plt.xlabel("Produkcja [zł]")
plt.ylabel("Zużycie surowca [kg]")
plt.title("ZALEŻNOŚĆ PRODUKCJI OD ZUŻYCIA SUROWCA")
plt.show()