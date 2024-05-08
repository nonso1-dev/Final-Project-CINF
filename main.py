import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


data=pd.read_csv(r"C:\Users\library\PycharmProjects\Final Project\IMDB-Movie-Data.csv")



print("1. Displaying top 10 rows of the dataset")
print(data.head(10),"\n")

print("2. Displaying  last 10 rows of the dataset")
print(data.tail(10),"\n")

print("3.Finding the shape of the dataset")
print("Number of rows", data.shape[0])
print("Number of Columns",data.shape[1],"\n")

print("4.  Getting Information About Our Dataset Like Total Number Rows,Total Number of Columns, "
      "Datatypes of Each Column And Memory Requirement")
data.info()

print("\n5. Display Missing Values In The Dataset")
print("Any missing value?", data.isnull().values.any())

print(data.isnull())
print(data.isnull().sum())

#visualizing the missing values as a heatmap using seaborn
plt.figure(figsize = (12,10))
sns.heatmap(data.isnull())
plt.title("HeatMap showing missing Values")
plt.show()

#Expressing missing values as a percentage
print("\nExpressing missing values as a percentage")
per_missing = data.isnull().sum() * 100 / len(data)
print(per_missing)

#6. Checking for missing values in dataset
print("\n 6. Checking for missing values in dataset")
print("Are there any missing values?",data.dropna(axis=0,inplace=True))

#7 Check for duplicate values in dataset
print("\n7. Check for duplicate values in dataset")
dup_data=data.duplicated().any()
print ("Are there any duplicate values?", dup_data)

data=data.drop_duplicates()
print(data)

#8. Get Overall Statistics About The DataFrame
print("\n8. Get Overall Statistics About The DataFrame")
print(data.describe(include='all'))

#9.Display title of movies having runtime greater than or equal to 120 Minutes
print("\n9.Display title of movies having runtime greater than or equal to 120 Minutes")
print(data.columns)
print(data[data['Runtime (Minutes)'] >= 120]["Title"])

#10. Movie Year with the highest average voting
print("\n 10. Movie Year with the highest average voting")
print(data.groupby('Year')['Votes'].mean().sort_values(ascending=False))

#visualizing the votes as a barplot using
sns.barplot(x='Year',y='Votes',data=data)
plt.title("Votes By Year")
plt.show()

#11. Movie Year with the highest average Revenue
print("\n 11. Movie Year with the highest average Revenue")
print(data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False))

#visualizing the Revenue as a barplot
sns.barplot(x='Year',y='Revenue (Millions)',data=data)
plt.title("Revenue By Year")
plt.show()

#12.Classify Movies Based on Ratings [Excellent, Good, and Average]
print("\n 12.  Movies Based on Ratings [Excellent, Good, and Average]")
def rating (rating):
      if rating >= 8.5:
            return "Excellent"
      elif rating >= 5.5:
            return "Good"
      else:
            return "Average"

data['rating_cat'] =data['Rating'].apply(rating)
print(data.head())

#13.Find unique values from each movie genre
print("\n 13.  Finding unique values from each movie genre")
print (data['Genre'])

list1 = []
for value in data['Genre']:
      list1.append(value.split(','))

print("\n",list1)

one_d = []
for item in list1:
      for item1 in item:
            one_d.append(item1)
print(one_d)

unik_list=[]
for item in one_d:
      if item not in unik_list:
            unik_list.append(item)
print(unik_list)


#14.How Many movies of each genre were made?
print("\n 14.  How Many Films of Each Genre Were Made?")

print((Counter(one_d)))
