# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
#probability for the event that fico credit score is > 700
p_a = df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
print('p_a:',p_a)
#probability for the event that purpose==debt_consolidation
p_b = df[df['purpose']=='debt_consolidation'].shape[0]/(df.shape[0])
print('p_b:',p_b)
#calculating purpose==debt_consolidation
df1 = df[df['purpose']=='debt_consolidation']
#probability for the event that purpose==debt_consolidation given fico credit >700
p_a_b = df1[df1['fico'].astype(float)>700].shape[0]/df.shape[0]
print('p_a_b:',p_a_b)
#check for independency
result = p_a_b == p_a
print('Independency:',result)
# code ends here


# --------------
# code starts here
#probability for the event that paid.back.loan==yes
prob_lp = df[df['paid.back.loan']=='Yes'].shape[0]/df.shape[0]
print('prob_lp:',prob_lp)
#probability for the event that credit.policy==yes
prob_cs = df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
print('prob_cs:',prob_cs)
#calulating paid.back.loan==yes
new_df = df[df['paid.back.loan']=='Yes']
#probability for the event paid.back.loan==yes given credit.policy==yes
prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
print('prob_pd_cs:',prob_pd_cs)
#conditional probabilty
bayes = (prob_pd_cs*prob_lp)/prob_cs
print('Bayes:',bayes)
# code ends here


# --------------
# code starts here
df1 = df[df['paid.back.loan']=='No']
df1.hist()

# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
print('installment_median:',inst_median)

inst_mean = df['installment'].mean()
print('installment_mean:',inst_mean)

df['installment'].hist()
df['log.annual.inc'].hist()

# code ends here


