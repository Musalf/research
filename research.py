import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('research.csv')

print(df)
year = df['Year'].head(8)
value = df['RD_Value'].head(8)
 
# Figure Size
fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(year[0:10], value[0:10])
 
# Show Plot
plt.show()