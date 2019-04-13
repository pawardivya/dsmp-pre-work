# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
#Load the dataframe from the variable 'path' and store the dataframe in a variable called 'data'.
data = pd.read_csv(path)

#In the column Gender, replace '-' with 'Agender' using "replace()" function.
data['Gender'].replace('-','Agender')

#Save the value counts of Gender in a variable called 'gender_count' using "value_counts()".
gender_count = pd.value_counts(data['Gender'].values)
gender_count.hist() #plot the bar graph(histogram)
plt.title('Gender Counts')



# --------------
#Code starts here
import pandas as pd

#Save the value counts of Alignment in a variable called 'alignment' using "value_counts()".
alignment = pd.value_counts(data['Alignment'].values)

#plot the pie chart
plt.pie(alignment,explode=(0.05,0.05,0.05))

#Label the pie chart
plt.title('Character Alignment')



# --------------
#Code starts here
#Create a subset having columns Strength & Combat
sc_df = data.loc[ : , ['Strength', 'Combat']]

#Calculating Covariance between Strength & Combat
sc_covariance  = sc_df.Strength.cov(sc_df.Combat)
print('Covariance between Strength & Combat :', sc_covariance)

#Calculating standard deviation of Strength & Combat
sc_strength = sc_df.Strength.std()
print('Standard deviation of Strength :', sc_strength)
sc_combat = sc_df.Combat.std()
print('Standard devition of Combat :', sc_combat)

#Calculating pearson's correlation coefficient between Strength & Combat
sc_pearson = sc_covariance/(sc_combat*sc_strength)
print('Pearsons correlation coefficient between Strength & Combat :', sc_pearson)

#Create a subset having columns Intelligence & Combat
ic_df = data.loc[: , ['Intelligence', 'Combat']]

#Calculating Covariance between Intelligence & Combat
ic_covariance  = ic_df.Intelligence.cov(ic_df.Combat)
print('Covariance between Intelligence & Combat :', ic_covariance)

#Calculating standard deviation of Intelligence & Combat
ic_intelligence = ic_df.Intelligence.std()
print('Standard deviation of Intelligence :', ic_intelligence)
ic_combat = ic_df.Combat.std()
print('Standard devition of Combat :', ic_combat)

#Calculating pearson's correlation coefficient between Intelligence & Combat
ic_pearson = ic_covariance/(ic_combat*ic_intelligence)


# --------------
#Code starts here
#Find the quantile=0.99 value of 'Total' column
total_high= data['Total'].quantile(q=0.99)

#Subsetting the dataframe based on 'total_high' 
super_best=data[data['Total']>total_high]

#Creating a list of 'Name' associated with the 'super_best' dataframe
super_best_names=list(super_best['Name'])

#Printing the names
print(super_best_names)

#Code ends here


# --------------
#Code starts here
#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting box plot
ax_1.boxplot(super_best['Intelligence'])

#Setting the subplot axis title
ax_1.set(title='Intelligence')


#Plotting box plot
ax_2.boxplot(super_best['Speed'])

#Setting the subplot axis title
ax_2.set(title='Speed')


#Plotting box plot
ax_3.boxplot(super_best['Power'])

#Setting the subplot axis title
ax_3.set(title='Power')

#Code ends here   


