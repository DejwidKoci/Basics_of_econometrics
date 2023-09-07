# Qualitative Variables
Here we focus on a model where the explanatory variable is expressed on a continuous scale and the explanatory variables can be quantitative and qualitative.
If a qualitative explanatory variable refers to 2 possible options A and B, then the corresponding zero-one variable can be defined as:
- $z_{1i} = 1$, when the observation represents variant $A$ 
- $z_{1i} = 0$, when the observation represents variant $B$


Then in the model
$$\hat{y_i} = c_0 + a_1x_{1i} + c_1z_{1i}$$
$c_i$ measures the average impact on the explanatory variable of variant $A$ relative to variant $B$ (at the same level of the quantitative variable $x_{1i}$).

When a qualitative variable refers to the 3 possible options A, B and C, then the zero-one variables are defined as:
- $z_{1i} = 1$, when the observation represents variant $A$ 
- $z_{1i} = 0$, on the contrary

and

- $z_{2i} = 1$, when the observation represents variant $B$ 
- $z_{2i} = 0$, on the contrary

In a model with a constant, the variable relating to the third option should no longer be included.  
This is because if the variable $z_3$ were included:
- $z_{3i} = 1$, when the observation represents variant $C$ 
- $z_{3i} = 0$, on the contrary

then there would be a linear relationship between the constant and the variables $z_1, z_2, z_3$, so no
it would not be possible to unambiguously estimate the model parameters.



In general, in a model with a constant, the number of variables representing the quality variable
must be one less than the number of variants.
If in model:
$$y_i = \beta_0 + \alpha_1x_{1i} + \beta_1z_{1i} + \beta_2z_{2i} + \beta_3z_{3i} + \epsilon_i$$
remove the variable z3i corresponding to variant C, then we obtain the model:
$$y_i = \beta_0 + \alpha_1x_{1i} + \beta_1z_{1i} + \beta_2z_{2i} + \beta_3(1-z_{1i}-z_{2i}) + \epsilon_i$$,
so after sorting we get:
$$y_i = (\beta_0 + \beta_3) + \alpha_1x_{1i} + (\beta_1 - \beta_3)z_{1i} + (\beta_2 - \beta_3)z_{2i} + \epsilon_i$$

It follows from the formula above that the parameter score appearing in the model with the variable
representing a variant measures the average impact on the explanatory variable of that variant
related to the impact of the omitted variant.
Qualitative variables can also be used to analyse seasonal data.

If there are seasonal variations in the phenomenon under study, which are linear and constant for the
individual quarters, they can be described as follows:
$$y_i = \beta_0 + \sum \beta_lz_{li} + \sum \alpha_j x_{ji} + \epsilon_i$$
where:
- $z_l$ - zero-item variables taking the value of one in the $l$-th quarter of each year and a value of zero in the remaining quarters, $l=1, 2, 3, 4$.
- $x_j$ - other explanatory variables, $j=1, 2, ...,k$.

Bearing in mind that the number of variables representing a qualitative variable must be one less than the number of variants, we substitute $z_{4i} = 1 - z_{1i} - z_{2i} - z_{3i}$ and we receive:
$$y_i = \beta_0 + \beta_1z_{1i} + \beta_2z_{2i} + \beta_3z_{3i} + \beta_4(1 - z_{1i} - z_{2i} - z_{3i}) + \sum \alpha_j x_{ji} + \epsilon_i$$

The model was therefore transformed to the form:
$$y_i = \gamma_0 + \sum \gamma_i z_{li} + \sum \alpha_j x_{ji} + \epsilon_i$$
where:
- $\gamma_0 = \beta_0 + \beta_4$
- $\gamma_1 = \beta_1 - \beta_4$
- $\gamma_2 = \beta_2 - \beta_4$
- $\gamma_3 = \beta_3 - \beta_4$

Then $c_l$ - parameter evaluations $\gamma_l$ report the average magnitude of seasonal effects in
in relation to the size of the explained variable in Q4, $l = 1, 2, 3$.
