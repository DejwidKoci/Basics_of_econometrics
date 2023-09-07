# Multicollinarity
In this module we examine multicollinarity between depended variables.
Exact collinearity exists when there is such a vector $C_k \neq 0$, that:
$$c_1x_{1i} + c_2x_{2i} + ... + c_kx_{ki} = 0$$
$$x_{(k)i} \cdot c_{(k)} = 0$$
$$i = 1, 2, ..., n$$
Where:
- $x_{ki} = [x_{1i}, x_{2i}, ... , x_{ki}]$
- $c_k = [c_1, c_2, ..., c_k]^T$

This means that the matrix X does not have a full column row.  We call the row of a matrix $A$ the number of linearly independent columns of this matrix $rz(A)$.  
Full row of matrix $X$ - none of the independent variables can be represented as a linear function of the others.  
The matrix X is not of full order:  
- The system has infinitely many solutions,
- Non-identifiability, redundancy.

## Variance Inflation Factor $(VIF_j)$ as a Tool to Measure Multicollinearity
$$CIW_j = \frac{1}{1 - R_j^2}$$
When $CIW_j > 10$, denotes the presence of mulitcollinearity, which permanently distorts the quality of the model.
