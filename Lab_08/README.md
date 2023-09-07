# Autocorrelation Testing
To test for first-order autocorrelation, a coefficient is used $\rho$ defined as:
$$\rho = \frac{cov(\epsilon_i, \epsilon_{i-1})}{D(\epsilon_{i})D(\epsilon_{i-1})}$$
Where:
- $cov(\epsilon_i, \epsilon_{i-1})$ - covariance between $\epsilon_i$ and $\epsilon_{i-1}$
- $D(\epsilon_i)$, $D(\epsilon_{i-1})$ - standard deviation for $\epsilon_i$ and $\epsilon_{i-1}$

Autocorrelation coefficient from the sample defined by the formula:

$$\hat{\rho} = \frac{\sum e_i e_{i-1}}{\sqrt{\sum e_i^2 \cdot \sum e_{i-1}^2}}$$
Autocorrelation coefficient from the sample $\hat{\rho}$ has properties such as the correlation coefficient, among others:
- takes values in the range [-1,1]
- determines the direction of the relationship,
- absolute value $\hat{\rho}$ indicates the strength of the linear relationship.

The test to verify the existence of first-order autocorrelation is the DurbinWatson statistic.
$$d = \frac{\sum(e_i - e_{i-1})^2}{\sum e_i^2}$$

In the case of a large sample size, between the $d$ statistic and the coefficient of the of sample autocorrelation  $\hat{\rho}$ there is thus a relationship:
$$d \approx 2(1-\hat{\rho})$$

Thus, when $\hat{\rho}$ is close to 1 (strong positive autocorrelation), $d$ has a value approximately equal to 0. Conversely, when
$\hat{\rho}$ is close to -1 (strong negative autocorrelation), the Durbin-Watson statistic takes on a value close to 4.
Durbin-Watson takes on a value close to 4. Conversely, when this coefficient is equal to 0 (no autocorrelation), $d$ is approximately equal to 2.

Caution!
To apply this test correctly, the econometric model under consideration must have the the following properties:
- the model has a free expression,
- the random component has a normal distribution,
- there is no lagged explanatory variable as an explanatory variable in the model.

Inference from the Durbin-Watson statistic is carried out as follows way:

1. If $\hat{\rho}$ (autocorrelation coefficient from the sample) hypotheses are verified:  
$H_0: \rho = 0$    
$H_1: \rho > 0$
When $d > d_U$, there are no grounds to reject hypothesis H0 (no autocorrelation),
- when $d < d_L$, the hypothesis $H_0$ must be rejected (there is positive autocorrelation),
- when $d_L \leq d \leq d_U$ no test result.

2. If $\hat{\rho}$ (autocorrelation coefficient from the sample) hypotheses are verified:
$H_0: \rho = 0$
$H_1: \rho < 0$

We calculate $d' = 4-d$, then
- when $d' > d_U$, there are no grounds to reject hypothesis $H_0$ (no autocorrelation),
- when $d' < d_L$, the hypothesis $H_0$ must be rejected (there is negative autocorrelation),
- when $d_L \leq d' \leq d_U$, there is no resolution of the test.

The Durbin-Watson test can also be used for hypotheses:  
$H_0: \rho = 0$  
$H_1: \rho \neq 0$   
- If $d_U < d < 4 - d_U$, then there is no basis for rejecting the null hypothesis (no autocorrelation),  
- If $0 < d < d_L$ or $4 - d_L < d < 4$, then we reject the null hypothesis (autocorrelation has occurred),  
- If $4-d_U < d < 4-d_L$ or $d_L < d < d_U$, then on the basis of the Durbin-Watson test we cannot we can decide whether autocorrelation has occurred or not.  
