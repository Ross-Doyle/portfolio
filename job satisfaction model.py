import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

#import the excel version of the dataset
employees=(r"C:\Users\rossd\Downloads\employee.csv")
data=pd.read_csv(employees)
#directory can be set to read data from source instead of downloading first

#set y as our target which will be the satisfaction level of each employee
#and X contains the 'features' or determining factors, that we will use to predict
#what areas of a job are most influential to an individuals happiness with their job

y=data.satisfaction_level
features=['average_montly_hours','time_spend_company','Work_accident','promotion_last_5years']
X=data[features]

#split the data into training data and testing data,
#test_size=0.1 takes 10% of employees and uses them as the test data
#the remaining 90% is used as the training data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1)

#use decision tree to compare predictions to actual data
data_model=DecisionTreeRegressor(random_state=1)
data_model.fit(X,y)

#print the results for the first 5 satisfaction level predictions
print("predictions for the first 5 employees")
print(data_model.predict(X.head()))
print("actual first 5 employee satisfaction level")
print(y.head())

#the results are within the correct range but are not as accurate as we would like
#them to be. We can make several changes to increase the accuracy of predictions.
#One change is adding in the 'salary column, however pandas cannot convert low, medium and high into
#float values, so we instead convert salaries into integers on the excel file and use the new salary_figures column

## ------ In Excel:
# =IFS(I2="low",RANDBETWEEN(14000,25000),I2="medium",RANDBETWEEN(26000,50000),I2="high",RANDBETWEEN(51000,81000))

features=['average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','salary_figure']
X=data[features]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1)
data_model=DecisionTreeRegressor(random_state=1)
data_model.fit(X,y)

print("predictions for the first 5 employees with salaries included")
print(data_model.predict(X.head()))
print("actual first 5 employee satisfaction level")
print(y.head())

#the new predictions are now accurate, a bit too accurate perhaps
#our predictions have determined the exact values for the satisfaction level of the first 5 employees listed
#we have overfitted the data, as the random values for the salaries have made each employee fit into their own
#leaf at the end of the decision tree

#if we instead make the salaries for low, medium and high a random choice of 3 or 4 options, we can still increase
#the accuracy whilst avoiding overfitting

#in Excel:
# =IFS(I2="low",(INDEX($Q$2:$Q$4,RANDBETWEEN(1,ROWS($Q$2:$Q$4)),1)),
# I2="medium",(INDEX($Q$7:$Q$9,RANDBETWEEN(1,ROWS($Q$7:$Q$9)),1)),
# I2="high",(INDEX($Q$12:$Q$14,RANDBETWEEN(1,ROWS($Q$12:$Q$14)),1)))

#Where the arrays are entries in a table with 3 salaries for each level

features=['average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','new_salaries']
X=data[features]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1)
data_model=DecisionTreeRegressor(random_state=1)
data_model.fit(X,y)

print("predictions for the first 5 employees with new salaries")
print(data_model.predict(X.head()))
print("actual first 5 employee satisfaction level")
print(y.head())

#here our predictions are extremely accurate but not due to leaf being occupied by a single employee


#some changes/additions to improve this model;
#create a function to reduce the amount of repeated code
#add a decision tree forest to run the model several times over