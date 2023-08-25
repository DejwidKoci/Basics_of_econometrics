import pandas as pd
import statsmodels.api as sm


data = pd.read_excel("data.xlsx", sheet_name='dane_03')


X = data.drop(columns=["Y"])
y = data["Y"]


def backward_stepwise_regression(X, y, threshold_out=0.05):
    num_vars = X.shape[1]
    selected_vars =  X.columns.tolist()  # Zmienne początkowo wybrane to wszystkie
    
    while True:
        X_selected = sm.add_constant(X[selected_vars])  # Dodajemy kolumnę jedynek
        model = sm.OLS(y, X_selected).fit()
        print(model.summary())
        p_values = model.pvalues[1:]  # Pomijamy wartość dla stałej (indeks 0)
        max_p_value = p_values.max()
        
        if max_p_value > threshold_out:
            remove_idx = p_values.idxmax()
            selected_vars.remove(remove_idx)
        else:
            break
    
    return model, selected_vars

final_model, selected_vars = backward_stepwise_regression(X, y)
print("Wybrane zmienne:", selected_vars)
print(final_model.summary())