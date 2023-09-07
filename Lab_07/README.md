# Tests of Normality of the Distribution of the Random Component
## Shapiro-Wilk Test
Of the tests verifying the normality of the random component, the Shapiro-Wilk test deserves attention because:
- is insensitive to autocorrelation and heteroskedasticity of the random components.
- as opposed to other tests of concordance with a normal distribution, such as the Kolmogorov-Liliefors or $\chi^2$ test, it can be used for small samples, when  $n<=30$.

Procedure for the use of the Shapiro-Wilk test
The hypothesis shall be verified:  

$H_0:$ random component of the model $y = X\beta + \epsilon$ has a normal distribute  
$H_1:$ random component of model $y = X\beta + \epsilon$ has not a normal distribute

Algorithm for dealing with the Shapiro-Wilk test:
1. Order the remainders according to non-decreasing values so that you get a sequence of $e_{(1)}, e_{(2)}, ..., e_{(n)}$.
2. The value of the statistic shall be calculated $$W = \frac{[\sum a_{n,i} \cdot (e_{(n-i+1)}-e_{(i)})]^2}{\sum e_{(i)}^2}$$
Where:
- $a_{n,i}$ - Shapiro-Wilk coefficient read from tables ($\sum a_{n,i}$ is made from $i = 1$ to $n/2$)
  
3. From the tables of the Shapiro-Wilk test, for the assumed significance level $\alpha$ and sample size $n$, the critical value $W^{*}$ is read.
The Shapiro-Wilk test is a left-tailed test, so if $W > W^{\star}$, there are no grounds for rejecting the hypothesis $H_0$ stating that the distribution of the of the random components is normal.
On the other hand, if $W < W^{\star}$ , hypothesis $H_0$ should be rejected in favour of hypothesis $H_1$, which means that the distribution of the random components is not normal.

## Jarque-Bera Test
Another test to verify the hypothesis on the normality of the random component is the Jarque-Bera test.  
The values of the Jarque-Bera statistic are provided by some econometric programs, e.g. Pc-Give.  
C. M. Jarque and A. K. Bera proposed a test comparing how measures of asymmetry and kurtosis calculated from the residuals differ from those measures characteristic of a normal distribution.  
Measures of asymmetry and kurtosis are determined from the third and fourth moments, respectively, as follows:
 - asymmetry factor: $A = \frac{M_3}{S^3}$ where:  
   - $M_3 = \frac{1}{n} \sum e_i^3$ this means, $M_3$ is the third moment,  
   - $S = \sqrt{\frac{1}{n} \sum e_i^2}$
 - concentration factor (kurtosis): $K = \frac{M_4}{S^4}$ where:
   - $M_4 = \frac{1}{n} \sum e_i^4$ this means, $M_4$ is the fourth moment,

The asymmetry coefficient is positive for right-handed asymmetry, negative for in the case of left-hand asymmetry and takes on a value of zero for symmetric distributions.
Thus, for a normal distribution, the coefficient is equal to zero.

In the case of a normal distribution $K=3$, if the distribution is more flattened relative to the to the normal distribution, then $K<3$, and if it is more slender, then $K>3$.
Therefore, in order to check whether the distribution is more or less slender than normal, a measure called the a measure called excess equal to kurtosis minus 3.


Jarque and Bera introduced the designations:
$\sqrt{B_1} = A$ and $B_2 = K$ and noted that statistics:
$$JB = n(\frac{1}{6}B_1 + \frac{1}{24} (B_2 - 3)^2)$$
has an asymptotic chi-square distribution with 2 degrees of freedom.

Verification of the hypothesis of normality of the random component with the Jarque-Bera test proceeds as follows:
1. On the basis of the residuals of the estimated model, the asymmetry coefficient should be calculated: $\sqrt{B_1} = A = \frac{M_3}{S^3}$ and kurtosis $B_2 = K = \frac{M_4}{S^4}$
2. The value of the Jarque-Bera statistic should be determined: $JB$
3. If $JB > \chi_{\star}^2$, then the hypothesis of normality of the random component must be rejected, whereas if $JB \leq \chi_{\star}^2$ then there are no grounds to reject this hypothesis.
$\chi^2_{\star}$ denotes here the critical value of the chi-square test for a significance level of $\alpha$ and 2 degrees of freedom.

The use of the Jarque-Bera test, due to its asymptotic convergence to a chi-square distribution, is only possible for large samples.
