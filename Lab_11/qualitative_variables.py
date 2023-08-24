import pandas as pd
import statsmodels.api as sm

data_01 = pd.read_excel('data.xlsx', sheet_name = 'dane_01')
y = data_01['Y']
X = data_01[['X1', 'Z1']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
#print(model.summary())

print(f"Model: {round(model.params['const'], 2)} + {round(model.params['X1'],2)}X1 + {round(model.params['Z1'],2 )}Z1")
print("Interpretacja: ")
print("X1: Po wyeliminowaniu wpływu płci wzrost dochodu o jednostkę, czyli o 1000 zł powodował wzrost spożycia owoców średnio o 0,31 kg. ")
print("Z1: Przy takim samym dochodzie kobiety spożywały średnio o 0,6 kg owoców więcej w porównaniu do mężczyzn.")
print()
print()


###############


data_02 = pd.read_excel('data.xlsx', sheet_name = 'dane_02')
y = data_02['Y']
X = data_02[['X1', 'Z1', 'Z2']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(f"Model: {round(model.params['const'], 2)} + {round(model.params['X1'], 2)}X1 + {round(model.params['Z1'], 2)}Z1 + {round(model.params['Z2'], 2)}")
print("Interpretacja: ")
print(f"X1: Po wyeliminowaniu wpływu płci wzrost dochodu o 1000 zł powodował wzrost spożycia owoców powodował wzrost spożycia owoców średnio o {round(model.params['X1'], 2)} kg ")
print(f"X1: Przy takich samych dochodach kobiety spożywały średnio o {round(model.params['Z1'], 2)} kg owoców więcej od mężczyzn na stanowiskach robotniczych ")
print(f"Z2: Przy takich samych dochodach mężczyźni na stanowiskach nierobotniczych spożywali średnio {round(model.params['Z1'], 2)}kg owoców w porównaniu do mężczyzn na stanowiskach robotniczych.")
print()
print()


###############

data_03 = pd.read_excel('data.xlsx', sheet_name = 'dane_03')
print(data_03)
y = data_03['Y']
Z = data_03[['t', 'Z1', 'Z2', 'Z3', 'Z4']]
Z = sm.add_constant(Z)
model = sm.OLS(y, Z).fit()
print(model.summary())

print(f"Model: {round(model.params['const'], 2)} + {round(model.params['t'], 2)} t + {round(model.params['Z1'], 2)} Z1 + {round(model.params['Z2'], 2)} Z2 + {round(model.params['Z3'], 2)} Z3")
print("Interpretacja:")
print(f"t: W badanym okresie z kwartału na kwartał produkcja rosła średnio o {round(model.params['t'], 2)}mln sztuk jaj.")
print(f"Z1: W badanym okresie produkcja jaj w pierwszym kwartale była średnio niższa o {round(model.params['Z1'], 2)} mln sztuk od produkcji w kwartale czwartym.")
print(f"Z2: W badanym okresie produkcja jaj w drugim kwartale była średnio niższa o  {round(model.params['Z2'],2 )} mln sztuk jaj.")
print(f"Z3:  W badanym okresie produkcja jaj w trzecim kwartale była średnio niższa o {round(model.params['Z3'])} mln sztuk jaj.")