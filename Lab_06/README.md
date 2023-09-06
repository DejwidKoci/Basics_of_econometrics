# Series Test
To explain the idea of a series test, let us use the example of a linear relationship with one explanatory variable explanatory variable.
The residuals can be positive, zero or negative, which corresponds to the situation that
points representing in a coordinate system the empirical values of the explanatory variable
and the explanatory variable, i.e $(x_i, y_i)$  $i = 1, 2, ..., n,$ may both lie above the straight (when $y_i > \hat{y_i}$), on the straight $(y_i = \hat{y_i})$ or under the straight $(y_i < \hat{y_i})$.  

If there are successively (i.e. according to increasing values of the explanatory variable) quite long series of residuals consisting only of values with the same signs, this means that there is some tendency among the residuals, i.e. they are non-random in nature.

The number of series of residuals should therefore not be too small, which corresponds to the situation that the empirical points should be randomly arranged above and below the straight line determined by the method of least squares.

### Procedure to be Followed if a Series Test is Used:
$H_0$: the distribution of the random component (the residuals in this model) is a random distribution  
$H_1$: the distribution of the random component (the residuals in this model) is not random.  
- Order the residuals in the sample in a non-decreasing order according to the ordering variable.
The ordering variable is the time variable when the data come from a time series, in the case of cross-sectional data, one of the explanatory variables.
- For an ordered sequence, the number of series of model residuals is calculated.
A series is the longest sequence of residuals of the same sign. The number of series of residuals is denoted by $S$.
If the residuals are random, the number of series is a random variable. Its distribution depends on the number of residuals positive and the number of negative residuals.
- If From the tables of the number of series test for the number of positive residuals $n_1$, the number of negative residuals $n_2$ and  the level of significance adopted $\alpha/2$ and $1 - \alpha/2$ the critical batch numbers are read $S_1$* and $S_2$*.  
If $S_1^{\star} < S < S_2^{\star}$ then there are no grounds to reject the hypothesis $H_0$, then residuals are random.
However, if $S \leq S_1^{\star}$ or $S \geq S_2^{\star}$ then the null hypothesis should be be rejected.

Note, the series test allows the hypothesis of randomness of the residuals to be verified only if, when the number of positive and negative residuals are not too large (usually assumed not to exceed 20.  
For a larger number of residuals, we use the Z statistic of the of the normal distribution. Then, to assess the randomness of the sequence of residuals, we can use the statistic:  
$$Z = \frac{S - E(S)}{\sigma_S}$$
Where mean: $E(S) = \frac{2n_1n_2}{n_1 + n_2} + 1,$
and standard deviation: $\sigma_s = \sqrt{\frac{2n_1n_2(2n_1n_2 - n_1 - n_2)}{(n_1 + n_2)^2(n_1 + n_2 - 1)}}$  
The $Z$ statistic has an asymptotic normal distribution $N(0,1)$
