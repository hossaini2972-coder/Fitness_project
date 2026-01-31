import pandas as pd

#Reading csvfile
activity = pd.read_csv(r"C:\Users\1PC\OneDrive\Documents\dailyActivity_merged.csv")

print(activity.head())

#Basic info check
print(activity.info())
print(activity.describe())

# converting date column
activity['ActivityDate'] = pd.to_datetime(activity['ActivityDate'])

#Visualization
import matplotlib.pyplot as plt

# Steps trend over time
plt.figure(figsize=(10,5))
plt.plot(activity['ActivityDate'], activity['TotalSteps'], marker='o')
plt.xticks(rotation=45)
plt.title("Daily Steps Trend")
plt.xlabel("Date")
plt.ylabel("Total Steps")
plt.show()

# Calories burned histogram
plt.figure(figsize=(6,4))
plt.hist(activity['Calories'], bins=20, edgecolor='black')
plt.title("Calories Burned Distribution")
plt.xlabel("Calories")
plt.ylabel("Frequency")
plt.show()


# project Tittle >>> Data-Driven Analysis of Steps and calories burned Pattern
