
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("Zomato data .csv")
print(dataframe.head())
def handleRate(value):
	value=str(value).split('/')
	value=value[0];
	return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

dataframe.info()
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of Restaurant")
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()



sns.barplot(x='listed_in(type)', y='votes', hue='listed_in(type)', data=dataframe, estimator=sum, palette="husl",errorbar=None)

plt.xlabel("Type of Restaurant", c="black", size=20)
plt.ylabel("Total Votes", c="black", size=20)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()





max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name'].values[0]
print("\n")

print(f"The restaurant with the max no of votes is {restaurant_with_max_votes} with {max_votes} votes.")

sns.countplot(x=dataframe['online_order'])