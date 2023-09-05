# OLS Model with Stastictic Measures 

Here we estimated the OLS model.
$$\hat{y_i} = \beta_0 + \beta_1 x_i $$

To assess the quality of this model, we calculate statistic measures and interpret them
## Coefficient of determination $R^2$
First of them is $R^2$:
$$R^2 = \frac{\sum{(\hat{y_i} - \bar{y})^2}}{\sum{(y_i - \bar{y}})^2}$$

The coefficient of determination R2 (R-squared) indicates how much of the total variation in the explanatory variable is explained by the model.  
The R2 coefficient takes values in the interval [0, 1] and that the greater the variability of the explanatory variable explained by the model, the closer to one the value of the coefficient of of determination  

## Standard deviation of the residuals $S_e$
The standard deviation of the residuals indicates how much the average observed values of the of the explained variable differs from the theoretical values of that variable determined from the model.
$$S_e = \sqrt{\frac{1}{n - k - 1} \cdot \sum_{i=1}^{n} e_i^2}$$

Where:
- $n$ is the number of observations
- $k$ is the number of depended variables
- $e_i = \hat{y_i} - y_i$, so $\sum e_i^2$ is the sum of the squares of the residuals, i.e. the variation in the explained variable not
explained by the model.

The standard deviation of the residuals is sometimes also referred to as the standard error of estimation (standard error of estimation).

## Mean Absolute Error (MAE)
Mean absolute error - reports the average of the of the absolute values of the residuals. 
The smaller the MAE values are, the better the fit of the model to the empirical data.

$$MAE = \frac{\sum|e_i|}{n}$$

## Coefficient of random variation $W_e$
The coefficient of random variation indicates what percentage of the mean value of the explained variable
is the standard deviation of the residuals.
$$W_e = \frac{S_e}{\bar{y}} \cdot 100\% $$

The smaller the value of the random coefficient of variation, the greater the consistency of theof the model with the empirical data.  
If, for a predetermined critical value of the coefficient of random variability coefficient W* (f.e W*= 10%) an inequality exists:
$W_e \leq W$* then the model is considered to be sufficiently well fitted to the empirical data.

## F test
The $F$ test can be used to verify the statistical significance of a coefficient of multiple determination.
The procedure for verifying the statistical significance of of the coefficient of determination is as follows:  
$$H_0: R^2 = 0$$
$$H_1: R^2 > 0$$

$F$ statistics defined as:
$$F = \frac{n - k - 1}{k} \cdot \frac{R^2}{1 - R^2}$$

We then read the critical value of $F$* with the significance level $\alpha$ (usually $\alpha = 0.05)$ , the number of explanatory variables $k$ and the number of degrees of freedom $n - k - 1$.
If $F>F$* we reject the null hypothesis, so the parameters are statistically significant.
