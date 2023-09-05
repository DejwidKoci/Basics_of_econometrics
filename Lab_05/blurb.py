from itertools import chain, combinations

def generate_combinations(variables):
    variable_combinations = []

    # Generowanie kombinacji pojedynczych zmiennych
    for variable in variables:
        variable_combinations.append([variable])

    # Generowanie kombinacji zawierających więcej niż jedną zmienną
    for r in range(2, len(variables) + 1):
        for combination in combinations(variables, r):
            variable_combinations.append(list(combination))

    return variable_combinations

variables = ["x1", "x2", "x3"]
all_combinations = generate_combinations(variables)

for combination in all_combinations:
    print(", ".join(combination))
