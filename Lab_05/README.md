# Methods of Selecting Variables for an Econometric Model
The selection of explanatory variables for an econometric model is a two-stage task.   

In the first stage, a set of potential explanatory variables to enter the model is drawn up on the basis of knowledge of the relationships analysed. 
The main consideration in selecting variables should be their substantive value while taking into account the purpose of their study.  

In the second stage, a reduction of the set of explanatory variables is carried out taking into account statistical criteria.

### Issues  
- information overload, high dispersion
- outliers
- different titres (lack of comparability)
- deficiencies in empirical data, 
- reliability of empirical data


## Elimination of quasi-fixed variables

A measure of the level of variation is the coefficient of variation:
$$V_j = \frac{S_j}{\bar{x_j}}$$
Where:
- $S_j$ - standard deviation of variable $x_j$
- $\bar{x_j}$ - arithmetic mean of variable $x_j$

From the set of initially considered explanatory variables, those variables are eliminated which, for the previously chosen critical value of the coefficient of variation $V$* (for instance $V$* $= 0.1$) , satisfy the inequality $|V_j| \leq V$*. 
Such variables are considered quasi-constant and therefore do not contribute relevant information.

Files with this algorithm: "Quasi_stałe_01.py" & "Quasi_stałe_02.py".

## Hellwig Method
This method is based on the principle of selecting from a set of potential explanatory variables $x_1, x_2,..., x_m$ such explanatory variables that are:
1) Strongly correlated with the explanatory variable,
2) Weakly correlated with each other.

We consider all non-empty combinations of 'candidate' (i.e. potential explanatory variables) explanatory variables.

The number of these combinations is $2^k - 1$

### Integral storage capacity
$$H_l = \sum_{j \in I_l}h_{lj}, l = 1, 2, ..., L$$
Where:
- $L$ - number of combinations
- $l$ - combination number
- $I_l$ - the set of numbers of variables forming the l-th combination


The individual and integral capacities of the information media will take values in the interval $[0,1]$. 
The best combination of explanatory variables is chosen as the one whose value of the integral capacity of the information carriers reaches the maximum value.

Files with this algorithm: "Hellwig.py".

## Correlation Coefficient Matrix Analysis Method

We calculate:
$$r^{*} =\sqrt{\frac{t_{\alpha}^2}{t_{\alpha}^2 + N - 2}}$$
Algorithm:
1) From the set of explanatory variables we eliminate all for which $|r_j| \leq r^{*}$
2) Of the remaining variables, we select $x_h$, for which $r_h = \max_{j}|r_j|$
3) From the set of potential ones, those variables are eliminated for which: $|r_{hj}| > r^{*}$
4) Comebact to step 2)

Files with this algorithm: "Macierz_korelacji_01.py" & "Macierz_korelacji_02.py".

## Sequential Methods for Selecting Explanatory Variables for the Model

In sequential variable selection procedures, the final form of the model is reached by gradually "improving" successive versions of the model.  
Two main types of these procedures can be distinguished:  
- elimination procedures (backward stepwise regression)
- selection procedures (forward stepwise regression)
  
Files with this algorithm: "krokowa_w_przód.py" & "krokowa_w_tył.py".
