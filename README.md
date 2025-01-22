
# Telco Churn Analysis

### This project aims to conduct a comprehensive churn analysis for Telco to understand the reasons behind customer attrition. By examining relevant customer data, we will identify key factors contributing to churn. Based on these insights, we will propose actionable strategies that Telco can implement to enhance customer retention and reduce churn rates

## Problem Statement

Telco is a Telephone company, a provider of telecommunications services, such as telephony and data 
communications. Telco is experiencing customer churn over some time and would want to know the like to know 
the reasons for the customer churn. 
Telco would want us to analyze all relevant customer data and develop focused customer retention programs and 
predict the behavior to retain the customer

### Source

The source file is aCSV file named "Telco Customer Churn" - https://github.com/meetsahir/Telco-Churn-Analysis/blob/main/Telco%20Customer%20Churn.csv

### Assumptions

1. No unusual occurrences which will have a substantial impact on the data used 
2. The information is still current and can be used to analyze a company’s possible plans in an eƯicient manner
3. The company is currently not using any of the suggested solutions 
4. Customers are paying for the services used only after they have used the services and not at the time of signing 
up 

### Research questions

1. What are the variables that aƯect the customer churn?
2. How can we predict the customer behavior?
3. What are the steps that the company can take to reduce the customer churn?

### Hypothesis

1. Senior citizens are churning out significantly when compared to non-senior citizens 
2. Customers with monthly contracts have an alarmingly high chance of churning out
3. Customers with electronic check payment method have a high churn rate
4. Churn rate of the customer decreases with increase in tenure 

### Analysis

As per analysis the data, we find that the total number of customers is 7043, out of which 5174 customers are still 
with the Telco and 1869 customers have churned out. So, Telco, is able to retain 73.46% of their customers 
whereas 26.54% of the customers have churned out

This is higher than usual, and we will need to check the reasons for the churn

![Image](https://github.com/user-attachments/assets/a7874954-8d63-4461-ac2a-1ac25899acb5)

Firstly, we are analyzing the data based on gender. When we check the churn details based on the gender, we are 
unable to find any relation between them. The gender-wise customer distribution is nearly equal, Telco has 2549 
female customers against 2625 male customer. Out of this, 939 and 930 customers have churned out respectively. 
This means, the churn ratio is nearly equal for both the gender types, and we do not have trends gender-wise


![Image](https://github.com/user-attachments/assets/c7be255a-9a80-4d4a-93ea-3fd013e6fbb2)


Next, we are checking the data related to senior citizen. Upon checking, we see that we mostly have customers 
who are not senior citizen, a total of 5901 customers are not senior citizen and 1142 customers are senior citizen

![Image](https://github.com/user-attachments/assets/4e51351c-f3fe-4f64-a5ed-e1a982b58e01)

However, the actual finding was that the churn% among the senior citizens is much higher than the customers who 
are not senior citizens. We see that 23.6% of the customers have churned out who are not senior citizens, whereas, 
the churn% goes up to 41.7% when we consider the senior citizens 

![Image](https://github.com/user-attachments/assets/a1f7dc76-1143-4405-816f-386a96435dd4)
