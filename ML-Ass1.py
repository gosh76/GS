# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:34:16 2018 by Goldie Sahni
"""

import numpy as np
import pandas as pd
import csv
df1 = pd.read_csv('~/GSpython/Countries.csv')
df1.head()
x = df1['Service']
y = df1['GDP per captia USD per annum']

# Part-A Anova
from scipy import stats
stats.f_oneway(x,y)
"""
 F_onewayResult(statistic=137.30392301069392, pvalue=1.0867446686972355e-22)
 F-statistic is 137.3039 and p-value is 1.08e-22.
 this p-value shows that we cannot reject our null hypothesis that there is 
 no significant difference between means of Service and GDP per captia USD 
 per annum. 
 
"""

#Part-B Linear Regression
import statsmodels.api as sm
model = sm.OLS(y,x).fit()
model.summary()

"""
 OLS Regression Results                                 
========================================================================================
Dep. Variable:     GDP per captia USD per annum   R-squared:                       0.735
Model:                                      OLS   Adj. R-squared:                  0.731
Method:                           Least Squares   F-statistic:                     199.4
Date:                          Sat, 17 Feb 2018   Prob (F-statistic):           1.95e-22
Time:                                  18:00:50   Log-Likelihood:                -765.87
No. Observations:                            73   AIC:                             1534.
Df Residuals:                                72   BIC:                             1536.
Df Model:                                     1                                         
Covariance Type:                      nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Service     2.461e+04   1742.471     14.122      0.000    2.11e+04    2.81e+04
==============================================================================
Omnibus:                        6.515   Durbin-Watson:                   1.228
Prob(Omnibus):                  0.038   Jarque-Bera (JB):                6.640
Skew:                           0.706   Prob(JB):                       0.0362
Kurtosis:                       2.564   Cond. No.                         1.00
==============================================================================
1. Adj. R-squared is 0.731 which means that 73.1% of variance in  
GDP per captia USD per annum can be explained by variance in Service.

2. F-statistic is 199.4 which means that this model is good.

3. Regression coefficient of Service is 24610 which means that a increase of one unit in 
 variable Service will result in increase of 24610 units of GDP per captia USD per annum.
 
4. Durbin-Watson statistic is 1.228 which means that there is autocorrelation in the residuals.

# Part-C Difference between ANOVA & Regression outputs

1. ANOVA test p-value > level of significance alpha tells us that null hypothesis(of no 
significant difference between means of two or more populations) is accepted and vice-versa.
ANOVA tests for difference in mean of two or more groups/populations.

2. Linear Regression models the relationship between independent & dependent variables 
telling us how the regression coefficient of an independent variable affects the change in 
dependent variable when independent variable changes.The direction of change in dependent
variable may be same or opposite to the change in independent variable depending upon the 
sign of regression coefficient of the independent variable.

"""                                                                        
