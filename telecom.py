import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("C://churn-bigml-20.csv")
print(data.head(50))
print(data.columns)
print(data.tail(50))
print(data.describe())
plt.figure(figsize=(10, 6))
sns.countplot(x="telecom_partner", data=data)
plt.title("Counts of telecom_partner")
plt.xlabel("telecom_partner")
plt.ylabel("Count")
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x='telecom_partner', y='state', data=data)
plt.title('Boxplot of telecom_partner vs. state')
plt.xlabel('telecom_partner')
plt.ylabel('state')
plt.show()