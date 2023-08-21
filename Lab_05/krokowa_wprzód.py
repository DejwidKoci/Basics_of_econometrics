import pandas as pd
import statsmodels.api as sm

# Wczytaj dane z pliku Excel
data = pd.read_excel("data.xlsx", sheet_name='dane_03')

# Definiuj zmienne objaśniające (X) i zmienną objaśnianą (y)
X = data.drop(columns=["Y"])
y = data["Y"]

def forward_stepwise_regression(X, y, threshold=0.05):
    included = []
    remaining_features = X.columns.tolist()
    
    while remaining_features:
        best_pvalue = 1
        best_feature = None
        
        for feature in remaining_features:
            model = sm.OLS(y, sm.add_constant(X[included + [feature]])).fit()
            p_value = model.pvalues[feature]
            
            if p_value < best_pvalue:
                best_pvalue = p_value
                best_feature = feature
        
        if best_pvalue < threshold:
            included.append(best_feature)
            remaining_features.remove(best_feature)
        else:
            break
    
    final_model = sm.OLS(y, sm.add_constant(X[included])).fit()
    return final_model

# Wywołaj funkcję dla regresji krokowej w przód
final_model = forward_stepwise_regression(X, y)

# Wyświetl wyniki
print("Wybrane zmienne objaśniające:")
print(final_model.model.exog_names[1:])
print("Model regresji krokowej w przód:")
print(final_model.summary())
