# Continuation
Here, compared to Lab_02, we have added the errors of the parameter evaluations and the confidence intervals in which they fall, together with interpretations.

## Error Analysis of Parameter Evaluations
Let us use matrix notation to estimate the parameters of the model, where the vector of parameter estimates is:
$$b = [b_0, b_1, \ldots, b_k]^T $$

Let us now estimate the standard errors of the parameter estimates using the notation of the
matrix notation.
The unconstrained estimator of the variance-covariance matrix of the estimator b is:
$$D^2(b) = S_e^2(X^TX)^{-1}$$
Where:
- $S_e^2$ means variance of estimation error.

Let us also use matrix notation to estimate the variance of the estimation error.
$$S_e^2 = \frac{1}{n-k-1}(y^Ty-b^TX^Ty)$$
Let us denote by $d_{ij}, i=0,1,...,k, j=0,1,...,k$ elements of matrix $D^2(b)$
Diagonal elements of the matrix $D^2(b), d_{jj}, j=0,1,...,k$ are are the variance scores of the estimators of the individual para-meters of the model,
while the square roots of the variance estimates are the standard errors of parameter estimation $\beta_j, j=0,1,...k$:
$$S_{b_j} = \sqrt{d_{jj}}$$

Standard error of parameter estimation $S_{b_{jj}}$ is an estimation of the standard deviation of the
values of the estimator $b_j$ that it takes in n-element samples.
The standard error of the parameter estimate $S_{b_j}$
indicates how much, on average, the estimate of $b_j$ differs from the  parameter $\beta_j$ if the parameter $\beta_j$ has been estimated on the basis of different samples consisting of the
of the same number of observations.

## Confidence interval
The confidence interval for the $beta_j$ parameter is of the form:
$$(b_j - t_{\alpha, n-k-1} \cdot S_{b_j} , b_j + t_{\alpha, n-k-1} \cdot S_{b_j}), j=0,1,2,...,k$$
Where:
- $b_j$ is an estymator with normal distribution with mean $\beta_j$ and with standard deviation $\sigma_{b_j}$
- $t_{\alpha, n-k-1}$ is critical value of the t-student distribution with level of significance $\alpha$ and $n-k-1$ degrees of freedom ($n$ - the number of observations, $k$ - the number of depended variables)
- $S_{b_j}$ - error analysis of parameter evaluations $b_j$
