# Testing for Homoskedasticity of the Random Component

In the classical least squares method, it is assumed that the variance of the random component $\epsilon_i$ is constant for all i, i.e.
$$D^2(\epsilon_i) = \sigma^2$$

The property of equal variances is called homoskedasticity of random components. Its its opposite is heteroskedasticity.
One of the tests used to verify the hypothesis of homoskedasticity of the of random components is the Goldfeld-Quandt test.  

Application of this test requires separating 2 sub-samples, where we believe that the variation within each sub-sample is
small, while there is a significant difference between the variances in these 2 subsamples.  

The constancy of variances of random components is verified by the hypothesis of equality of variances of the two extreme subsamples of observations:  

$H_0: \sigma_1^2 = \sigma_2^2$  
$H_1: \sigma_1^2 > \sigma_2^2$

Where $\sigma_1^2$ denotes the variance in the first subsample, and $\sigma_2^2$ the variance in the second subsample.
The procedure is then as follows:
1. We order the non-decreasing observations in the sample according to the ordering variable.  
The  variable ordering variable when the data come from a time series is the time variable, while the
in the case of cross-sectional data, one of the explanatory variables that we suspected of causing heteroskedasticity.  
2. The two outermost subsamples are selected. The number of observations omitted should not exceed one third of the total sample size, i.e. $\frac{1}{3} n$ (cf. Greene).  
By $n_1$ we denote the number of observations in the first subsample and $n_2$ the number of observations in the second subsample.  
3. We estimate the model parameters individually in each subsample and determine the variances residuals $S_1^2$ and $S_2^2$ in the first and second subsamples, respectively.  
4. We calculate $\frac{S_2^2}{S_1^2}$ (in the numerator must be the greater of the variances). If hypothesis $H_0$ is true, then $\frac{S_2^2}{S_1^2}$ has an F Snedecor distribution.  
5. In the statistical tables for the assumed significance level $\alpha$ and $m_1=n_2-k-1, m_2=n_1-k_1$ degrees of freedom we read the critical value $F^{\star}$. If $F \leq F^{\star}$, then there are no grounds to reject the hypothesis $H_0$ of homoskedasticity of the random components. If, on the other hand
$F>F^{\star}$, we reject hypothesis $H_0$ in favour of hypothesis $H_1$ (i.e. there was a case of heteroskedasticity has occurred).


The Goldfeld-Quandt test is useful in situations where the variation in the variance of a random component of a random component is dependent on only one explanatory variable. 
If heteroskedasticity has been caused jointly by several explanatory variables, it is more appropriate to the use of other tests, such as the White or Harvey-Godfrey test or the Breusch - Pagan.
These tests can only be used when the number of observations is large. The number of degrees of freedom should be at least 30.
In the output model, the explained variable depends on k explanatory variables:
$$y_i = \beta_0 + \beta_1x_{1i} + ... + \beta_kx_{ki} + \epsilon_i$$

A. In the White's test, the variance of the random component is determined by a linear model in
in which the explanatory variables are: $x_1, x_2, ..., x_k, x_1^2, x_2^2, ..., x_k^2$ and $x_jx_l$ $j = 1, 2,...,k, l = 1, 2, ..., k$.
B. In the case of the Harvey-Godfrey test, the values of the explanatory variable are the logarithms of the natural squares of the output model residuals and the explanatory variables are the variables $x_1, x_2, ..., x_k$

The procedure in these tests is as follows:
1. We estimate the parameters of the output model: $y_i = \beta_0 + \beta_1x_{1i} + ... + \beta_kx_{ki} + \epsilon_i$
2. We determine the squares of the residuals of the output model. We consider them as realisations of the variance of the random component.
3. We estimate the parameters of the auxiliary model. In this model:
   - In the White test, the values of the explained variable are the squares of the residuals of the model output and the explanatory variables are $x_1, x_2, ..., x_k$ and $x_jx_l, j=1,2,...,k, l=1,2,...,k,$
   - In the case of the Harvey-Godfrey test, the values of the explanatory variable are the logarithms of the natural squares of the residuals of the output model and the explanatory variables are $x_1, x_2, ..., x_k$.
4. We determine the value of the statistic $nR^2$ , where $n$ is the sample size and $R^2$ is the coefficient of determination in the auxiliary model.
We compare $nR^2$ with the critical value of the chi-square test for the significance level $\alpha$ and $p$ degrees of freedom $\chi^2_{\alpha, k}$ , where $k$ is the number of explanatory variables in the auxiliary models.
5. If $nR^2 > \chi^2_{\alpha,k}$ then we reject the hypothesis of homoskedasticity, whereas if $nR^2 \leq \chi^2_{\alpha, k}$, then there are no grounds to reject the null hypothesis of homoskedasticity.
