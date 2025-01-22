
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

Coming to the churn% based on the monthly charges paid the customer, we are again unable to find any corelation, we find the similar percent have churned irrespective of the monthly charges, so this does not seem to be a deciding factor

![Image](https://github.com/user-attachments/assets/ebba4eb5-39d5-456b-aa45-a251737c9a21)

Another important finding is the churn% based on the contract type, here we are able to find that we have 
maximum number of customers having monthly contract, followed by two-year and one year contract has the least 
customers. Out of this, the churn% of the monthly contract customers are alarmingly higher and those of the other 
two types are more than acceptable. So, Telco really need to focus on this area

![Image](https://github.com/user-attachments/assets/66173ce4-d450-4875-88c9-cab1126551d3)

When we check the customer churn by Payment Method, we see that we have an equal share for all the payment 
method, however, the churned customers mainly belong to the Electronic check category. It is not easy to predict 
whether a co-relation exists between this, but this is something that can certainly be worth checking

![Image](https://github.com/user-attachments/assets/b8029a60-b004-481f-9813-9b8e38d23f78)

Next, when we investigate the customer churn based on the tenure, we see a clear trend where the customer 
churn decreases as the tenure increases and vice versa. The normal distribution curve of the histogram confirms 
the same

![Image](https://github.com/user-attachments/assets/8bf665a8-ab31-4509-ba00-1241b0ea7938)

Finally, we take a look at the customer churn rate based on the services that we are oƯering. The conclusion here is 
that most of our customers are not using the services that we oƯer. On that, the customer not using tech support, 
online backup, online security have a high churn rate. The contrary would be the internet service, where there is a 
higher churn rate for customers using fiber optic


![Image](https://github.com/user-attachments/assets/5e31dacc-1fae-49b3-8eed-adf9e25f5ae3)

### Findings and suggestions 

1. The data suggests that Telco has very less senior citizen customers and those that are there also have a high 
churn rate, so the company needs to check the reasons for that. They need to promote more towards the senior 
citizen customers and maybe bring better oƯers for them, so that they have more senior citizens joining and staying 
with them 
2. As per the data, customers who are choosing monthly contracts are having a very high rate of churn. So, the 
company needs to come up with strategies to convert the monthly contracts into yearly contracts or two-year 
contracts where the churn rate decreases rapidly 
3. Continuing with the above point, we also see that the customers with less tenure with Telco has a high rate of 
churn, so the company needs to focus on making the yearly, two-yearly contracts more lucrative and attractive 
which will eventually help them in retaining their customers 
4. Another interesting fact is that the customers with electronic check payment method have high churn rate. 
Though this does not directly indicate anything, but the company can talk to their customers to understand if there 
are any challenges with this payment method as the customers using other payment methods have a significantly 
lower churn rate 
5. It is also observed that most of the Telco customers are not using the services oƯered by the company and churn 
ratio among those customers are also on the higher side. The company should take up initiatives to educate 
customers more about their services, so the customer can start using their preferred services which has a high 
chance of reducing the customer churn 

### CONCLUSION 

ased on the Telco Churn Analysis, we find that the company is experiencing a higher churn rate than expected. 
We did analyze the factors that might be causing the customer churn rate to go higher and suggested the steps that 
the company should implement. We expect the customer churn rate of the company to reduce once they start 
implementing the steps 
