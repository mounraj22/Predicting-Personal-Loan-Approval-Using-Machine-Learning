# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uyRmh_PJPUTCAdSYxPjZ5u1qQTTTT2zz
"""

# Commented out IPython magic to ensure Python compatibility.
  import pandas as pd
  import numpy as np
  import pickle
  import matplotlib.pyplot as plt
#   %matplotlib inline  
  import seaborn as sns 
  import sklearn 
  from sklearn.tree import DecisionTreeClassifier
  from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
  from sklearn.neighbors import KNeighborsClassifier
  from sklearn.model_selection import RandomizedSearchCV
  import imblearn
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import StandardScaler
  from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,f1_score

data= pd.read_csv('/content/archive.zip')
data

data['Gender']=data['Gender'].astype('int64')
data['Married']=data['Married'].astype('int64')
data['dependents']=data['dependents'].astype('int64')
data['self_employed']=data['self_employed'].astype('int64')
data['coapplicantIncome']=data['coapplicantIncome'].astype('int64')
data['LoanAmount']=data['LoanAmount'].astype('int64')
data['Loan_amount-term']=data['LoanAmount'].astype('int64')
data['Credit_History']=data['credit_history'].astype('int64')

from imblearn.combine import SMOTETomek

smote = SMOTETomek(0.90)

y = data['Loan_Status']
x = data.drop(columns=['Loan_status'],axis=1)

x_bal,y_bal = smote.fit_resample(x,y)

print(y.value_counts())
print(y_bal.value_counts())

"""TASK 3 (EXPLORATORY DATA ANALSIS)

"""

data.describe()

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(data['applicantIncome'],color='r')
plt.subplot(122)
sns.distplot(data['credit_history'])
plt.show()

plt.figure(figsize=(18,4))
plt.subplot(1,4,1)
sns.countplot(data['Gender'])
plt.subplot(1,4,2)
sns.countplot(data['education'])
plt.show()

plt.figure(figsize=(20,5))
plt.subplot(131)
sns.countplot(data['married'],hue=data['Gender'])
plt.subplot(132)
sns.countplot(data['property_Area'],hue=data['Loan_amount_term'])

sns.swarmplot(data['Gender'],data['ApplicantIncome'], hue = data['Loan_Status''])

def decisionTree(x_train, x_test, y_train, y_test):
    dt=DecisionTreeClassifier()
    dt.fit(x_train,y_train)
    ypred = dt.predict(x_test)
    print('***Decisiontreeclassifier***')
    print('confusion matrix')
    print(confusion_matrix(y_test,ypred))
    print('classification report')
    print(classification_report(y_test,ypred))

def randomforest(x_train,x_test,t_train,y_test):
  rf = RandomForestClassifier()
  rf.fit(x_train,y_train)
  ypred = rf.predict(x_test)
  print('***RandomForestClassifier***')
  print('confusion matrix')
  print(confusion_matrix(y_test,ypred))
  print('classification report')
  print(classification_report(y_tast,ypred))

def KNN(x_train,x_test,y_train,y_test):
  knn = KNeighborsClassifier()
  knn.fit(x_train,y_train)
  ypred = knn.predict(x_test)
  print('(***KNeighborsClassifier***')
  print('confudion matrix')
  print('classification report')
  print(classification_report(y_test,ypred))

def xgboost(x_train,x_test,y_train,y_test):
  xg = GradientBoostingClassifier()
  xg.fit(x_train,y_train)
  ypred = xg.predict(x_test)
  print('***GrandientBoostingClassifier***')
  print('confusion matrix')
  print(confusion_matrix(y_test,ypred))
  print('classification report')
  print(classification_report(y_tast,ypred))

# impoeting the keras libraries and packages
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units=100,activation='relu',input_dim=11))

# Addin the second hidden layer
classifier.add(Dense(units=50,activation='relu'))

# Adding the output layer
classifier.add(Dense(units=1,activation='sigmoid'))

# Compiling the ANN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# Fitting the ANN to the training set
model_history = classifier.fit(x_train, y_train, batch_size=100, validation_split=0.2, epochs=100)

#Gender Married Dependents Education Self_Employed ApplicatIncome coapplicantIncome Loan_Amount_Term Credit_History property_Area
dtr.predict([[ 1, 1, 0, 1, 1, 4276, 1542, 145, 240, 0, 1]])

#Gender Married Dependents Education Self_Employed ApplicatIncome CoapplicantIncome  Loan_Amount_Term Credit_History property_Area
rfr.predict([[1,1,0,1,1,4276,1542,145,240,0,1]])

#Gender Married Dependents Education Self_Employed ApplicatIncome CoapplicantIncome  Loan_Amount_Term Credit_History property_Area
knn.predict([[1,1,0,1,4276,1542,145,240,0,1]])

#Gender Married Dependents Education Self_Employed ApplicatIncome CoapplicantIncome  Loan_Amount_Term Credit_History property_Area
xgb.predict([[1,1,0,1,1,4276,1542,145,240,0,1]])

classifier.save("loan.h5")

#predicting the Test set results
y_pred = classifier.predict(x_test)

[237] y_pred

[238] y_pred = (y_pred > 0.5)
      y_pred

def predict_exit(sample_value):

  # convert list to numby array 
  sample_value = np.array(sample_value)

  # Reshap because sample_value contains only 1 record
  sample_value = sample_value.reshape(1,-1)

  #Feature scaling 
  sample_value = sc.transform(sample_value)

  return classifier.predict(sample_value)

# prediction 
# value order 'creditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary',France',Germany','spain',Female',Male'.
sample_value = [[1,1,0,1,1,4276,1542,145,240,0,1]]
if predict_exit(sample_value)>0.5:
    print('prediction: High chance of Loan Approval!')
else:
    print('prediction:Low chance Loan Approval.')

# Predictions
# Value order 'creditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary',France',Germany','spain',Female',Male'.
sample_value = [[1,0,1,1,1,45,14,45,240,1,1]]
if predict_exit(sample_value)>0.5:
  print('prediction: High chance of Loan Approval!')
else:
   print('prediction:Low chance Loan Approval.')

"""TASK 4 (MODEL BUILDING)"""

def compareModel(x_train,x_test,y_train,y_test):
  decisionTree(x_train,x_test,y_train,y_test)
  print('-'*100)
  RandomForest(x_train,x_test,y_train,y_test)
  print('-'*100)
  XGB(x_train,x_test,y_train,y_test)
  print('-'*100)
  KNN(x_train,x_test,y_train,y_test)
  print('-'*100)

compareModel(x_train,x_test,y_train,y_test)

ypred = classifier.predict(x_test)
print(accuracy_score(y_pred,y_test))
print("ANN Model")
print("Confusion_Matrix")
print(confusion_matrix(y_test,y_pred))
print("Classification Report")
print(classification_report(y_test,y_pred))

from sklearn.model_selection import cross_val_score

#Random forest model is selected

rf = RandomForestClassifier()
rf.fit(x_train,y_train)
ypred = rf.predict(x_test)

f1_score(yPred,y_test,average='weighted')

cv = cross_val_score(rf,x,y,cv=5)

np.mean(cv)

""" TASK 4 (PERFORMANCE TESTING & HYPERPARAMETER TUNING)"""

pickle.dump(model,open('rdf.pkl','wb'))

from flask import Flask,render_template,request
import pickle

app = Flask(_name_)
model = pickle.load(open(r'rdf.pkl', 'rb'))
scale = pickle.load(open(r'scale1.pkl', 'rb'))

@app.route('/') # rendering the html template
def home():
  return render_template('home.html')

@app.route('/submit',methods=["POST","GET"])# route to show the predictions in a web UI
def submit():
  # reading the inputs given by the user 
  input_feature=[int(x) for x in request.form.values() ]
  #input_feature= np.transpose(input_feature)
  input_feature=[np.array(input_feature)]
  print(input_feature)
  name = ['Gender','Married','Dependents','Education','self_Employed','ApplicatIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']
  data = pandas.DataFrame(input_featuer,columns=names)
  print(data)
  

  #data_scale = scale.fit_transform(data)
  #data = pandas.DataFrame(,columns=name)

# prediction using the loaded model file
 prediction = model.predict(data)
 print(prediction)
 prediction = int(prediction)
 print(type(prediction))

 if (prediction == 0):
    return render_template("output.html",result ="Loan will Not be Approved")
 else:
    return render_template("output.html",result = "Loan will be Approved")
    # showing the prediction results in a UI
 if __name__=="__main__":

  # app.run(host='0.0.0.0', port=8000,debug=true)       #running the app
  port=int(os.environ.get('PORT',5000))
  app.run(debug=False)



