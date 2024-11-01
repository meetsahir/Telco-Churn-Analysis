# IMPORTING THE LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting the option to show complete dataframe data
pd.set_option('display.max_columns', None)

# LOADING THE DATA
df = pd.read_csv(r"C:\Users\Mohammad_sahir_Sahir\Downloads\Telco Customer Churn.csv")

# EXPLORATORY DATA ANALYSIS (EDA)
# Understanding the available data
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.describe())
print(df.info())

# DATA CLEANING
# checking for null values
print(df.isnull().sum())
# no null values were found in the dataset


# checking for duplicate values
print(df.duplicated())
# no duplicate value found across the dataset

# checking for duplicate value in the primary key - customerID
print(df["customerID"].duplicated().sum())
# no duplicates found in the primary key as well

#TRANSFORMING THE COLUMNS
# We see that the Monthly Charges column has a datatype of object when it should be float64
# When we try to convert the datatype to float we are getting error
# We see that some rows of the Total Charges column are empty as tenure for them is 0, replacing the empty values with 0
df["TotalCharges"] = df["TotalCharges"].replace(" ", 0)

df["TotalCharges"] = df["TotalCharges"].astype("float64")
# After replacing the empty values with 0 and then converting to float datatype works

# Also we see that the senior citizen has values 0 and 1, we change it to yes and no and for better understanding
df["SeniorCitizen"] = df["SeniorCitizen"].replace({0: "no", 1: "yes"})

# CREATING VISUALIZATIONS
# count plot for find the number of customers churned
c = ["#1f77b4", "#ff7f0e"]
ax = sns.countplot(x= 'Churn', data = df, palette = c)
for container in ax.containers:
    ax.bar_label(container)
plt.title("Count of Customer by Churn")
plt.show()

# pie chart to find the percentage of customers churned
gb = df.groupby("Churn").agg({"Churn": "count"})
plt.pie(gb["Churn"], labels = gb.index, autopct = "%1.2f%%")
plt.title("Percentage of Churned Customer")
plt.show()

# count plot to understand the gender distribution for churn
ax1 = sns.countplot(x= "gender", data = df, hue = "Churn", palette = c)
for container in ax1.containers:
    ax1.bar_label(container)
plt.title("Churned Customer's Gender-wise")
plt.show()

# count plot to understand the effect of churn by senior citizen
ax2 = sns.countplot(x= "SeniorCitizen", data = df, palette = c)
for container in ax2.containers:
    ax2.bar_label(container)
plt.title("Count of Senior Citizen")
plt.show()

# stacked bar chart
churn_percentage = df.groupby(['SeniorCitizen', 'Churn']).size().unstack().fillna(0)
churn_percentage = churn_percentage.div(churn_percentage.sum(axis=1), axis=0) * 100

# Plot the stacked bar chart
ax3 = churn_percentage.plot(kind='bar', stacked=True, color= c)
plt.title("Churn Percentage among Senior Citizens")
plt.xlabel("Senior Citizen")
plt.ylabel("Percentage")
plt.legend(title='Churn')

for container in ax3.containers:
    labels = [f'{v:.1f}%' if v > 0 else '' for v in container.datavalues]
    ax3.bar_label(container, labels = labels)
plt.show()


# plotting histogram to check the churn ratio by tenure
sns.histplot(x= "tenure", data = df, bins = 72, hue = "Churn", kde = True)
plt.title("Churned Customer by Tenure")
plt.show()

# countplot for contract type based on churn
ax4 = sns.countplot(x = "Contract", data = df, hue = "Churn", palette = c)
for container in ax4.containers:
    ax4.bar_label(container)
plt.title("Churned customer by Contract-type")
plt.show()

# countplot for payment method against churn
ax5 = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn", palette = c)
for container in ax5.containers:
    ax5.bar_label(container)
plt.title("Churned Customer by Payment method")
plt.show()

# histogram plot for monthly charges against churn
sns.histplot(x = "MonthlyCharges", data = df, bins = 60, hue = "Churn")
plt.title("Churned Customer against Monthly Charges")
plt.show()

# subplot for all the services against churn
columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
           'StreamingMovies']

# Create subplots
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(10, 10))

# Flatten the axes array for easy iteration
axes = axes.flatten()

# Iterate over columns and create count plots
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i], hue = "Churn")
    axes[i].set_title(f'Count of {col}')
    axes[i].set_xlabel("")

# Adjust layout
plt.tight_layout()
plt.show()