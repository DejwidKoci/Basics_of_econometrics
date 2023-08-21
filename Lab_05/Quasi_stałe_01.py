import pandas as pd

data = pd.read_excel("data.xlsx")
v_critical = 0.15
variables = []
n = data.shape[1]

for i in range(1, n + 1):
    mean = data[f'X{i}'].mean()
    data[f'(X{i}-Xśr)^2'] = (data[f'X{i}'] - mean) ** 2
    S = (sum(data[f'(X{i}-Xśr)^2'])/data[f'X{i}'].shape[0]) ** (1/2)
    V = S/mean
    if abs(V) > v_critical:
        variables.append(f'X{i}')

print("Wybrane zmienne: ", variables)