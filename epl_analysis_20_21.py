# -*- coding: utf-8 -*-
"""EPL Analysis 20-21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w4UPTCCNURO_tIJ-R7ibbPpM_viFrKdf
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv('EPL_20_21.csv')
df.head()

df.isna().sum()

df.info()

df.describe()

df.head(1)

df['MinsPerMatch'] = (df['Mins'] / df['Matches']).astype(int)

df['GoalsPerMatch'] = (df['Goals'] / df['Matches']).astype(float)

df.head()

# Total Goals

TotalGoals = df['Goals'].sum()
TotalGoals

# Penalty Goals

PenaltyGoals = df['Penalty_Goals'].sum()
PenaltyGoals

# Penalty Attempts
PenaltyAttempts = df['Penalty_Attempted'].sum()
PenaltyAttempts

# Pie chart for penalties missed versus penalties scored

plt.figure(figsize=(12,6))
Penaltiesmissed = PenaltyAttempts - PenaltyGoals
data = [Penaltiesmissed, PenaltyGoals]
labels = ['Penaltymissed','PenaltyGoals' ]
color = sns.color_palette('Set2')
plt.pie(data, labels = labels, colors = color, autopct='%.0f%%')
plt.show()

# Unique positions in the league

UniquePositions = df['Position'].unique()
UniquePositions

# Total FW who are under 25

TotalFW_under25 = df[(df['Position'] == 'FW') & (df['Age'] <= 25)]
TotalFW_under25.head(10)

# Number of Nations

TotalNations = np.size(df['Nationality'].unique())
TotalNations

# Top 7 clubs which have more number of players

df['Club'].value_counts().nlargest(7).plot(kind = 'bar', color = sns.color_palette('viridis'))

# Total clubs in the league

TotalClubs = np.size((df['Club']).unique())
TotalClubs

# Club Names

df['Club'].unique()

# Top 7 clubs which have the least number of players

df['Club'].value_counts().nsmallest(7).plot(kind = 'bar', color = sns.color_palette('rocket'))

Under20 = df[df['Age'] <= 20]
Under20.sum()

# Players based on the age group

Under20 = df[df['Age'] <= 20]
Age20_25 = df[(df['Age'] > 20) & (df['Age'] <= 25)]
Age25_30 = df[(df['Age'] > 25) & (df['Age'] <= 35)]
Above30 = df[df['Age'] > 30]

x = np.array([Under20['Name'].count(), Age20_25['Name'].count(), Age25_30['Name'].count(), Above30['Name'].count()])
labels = ['Under20','Age20_25', 'Age25_30', 'Above30']
color = sns.color_palette('Set2')
plt.pie(x, labels = labels, colors = color, autopct = '%.1f%%')
plt.title('Total Players with age')
plt.show()

#Players who are under 20 in each club

player_under20 = df[df['Age'] <= 20]

player_under20['Club'].value_counts().plot(kind = 'bar', color = sns.color_palette('cubehelix'))

player_under20.head(3)

ManU_under20 = player_under20[player_under20['Club'] == 'Manchester United']
ManU_under20.head()

