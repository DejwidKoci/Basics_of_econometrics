import numpy as np
import pandas as pd

# Podane dane
correlation_matrix = np.array([[1, -0.3, 0.5],
                               [-0.3, 1, -0.1],
                               [0.5, -0.1, 1]])

correlation_with_y = np.array([0.6, -0.9, 0.2])

variable_names = ['X1', 'X2', 'X3']

# Obliczenie wartości h11, h22, h33
H1 = h11 = correlation_with_y[0] ** 2
H2 = h22 = correlation_with_y[1] ** 2
H3 = h33 = correlation_with_y[2] ** 2

# Obliczenie wartości h41 i h42
h41 = correlation_with_y[0] ** 2 / (np.abs(correlation_matrix[0, 0]) + np.abs(correlation_matrix[1, 0]))
h42 = correlation_with_y[1] ** 2 / (np.abs(correlation_matrix[0, 1]) + np.abs(correlation_matrix[1, 1]))

# Obliczenie wartości H4
H4 = h41 + h42

# Obliczenie wartości h51 i h53
h51 = correlation_with_y[0] ** 2 / (np.abs(correlation_matrix[0, 0]) + np.abs(correlation_matrix[2, 0]))
h53 = correlation_with_y[2] ** 2 / (np.abs(correlation_matrix[0, 2]) + np.abs(correlation_matrix[2, 2]))

# Obliczenie wartości H5
H5 = h51 + h53

# Obliczenie wartości h62 i h63
h62 = correlation_with_y[1] ** 2 / (np.abs(correlation_matrix[1, 1]) + np.abs(correlation_matrix[2, 1]))
h63 = correlation_with_y[2] ** 2 / (np.abs(correlation_matrix[1, 2]) + np.abs(correlation_matrix[2, 2]))

# Obliczenie wartości H6
H6 = h62 + h63

# Obliczenie wartości h71, h72 i h73
h71 = correlation_with_y[0] ** 2/ (np.abs(correlation_matrix[0, 0]) + np.abs(correlation_matrix[1, 0]) + np.abs(correlation_matrix[2, 0]))
h72 = correlation_with_y[1] ** 2 / (np.abs(correlation_matrix[0, 1]) + np.abs(correlation_matrix[1, 1]) + np.abs(correlation_matrix[2, 1]))
h73 = correlation_with_y[2] ** 2 / (np.abs(correlation_matrix[0, 2]) + np.abs(correlation_matrix[1, 2]) + np.abs(correlation_matrix[2, 2]))

# Obliczenie wartości H7
H7 = h71 + h72 + h73

# Obliczenie wskaźników H dla correlation_with_y
H_y = correlation_with_y ** 2

# Wybór zmiennej z najwięks
max_H = max(H1, H2, H3, H4, H5, H6, H7, *H_y)
selected_variable = None

# Wybór zmiennej z największym wskaźnikiem H
max_H = max(H1, H2, H3, H4, H5, H6, H7)
selected_variable = None
if max_H == H1:
    selected_variable = "C1: {x1}"
elif max_H == H2:
    selected_variable = "C2: {x2}"
elif max_H == H3:
    selected_variable = "C3: {x3}"
elif max_H == H4:
    selected_variable = "C4: {x1, x2}"
elif max_H == H5:
    selected_variable = "C5: {x1, x3}"
elif max_H == H6:
    selected_variable = "C6: {x2, x3}"
elif max_H == H7:
    selected_variable = "C7: {x1, x2, x3}"

print(f"Maksymalną wartość wskaźnika pojemności informacyjnej (H) otrzymano dla kombinacji {selected_variable}")
