import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("data.csv")  #Load data from csv file
X=df[['HoursStudied']]
y=df['ExamScore']
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=42)
model=LinearRegression()
model.fit(X_train, y_train)
#streamlit user interface
st.title("Exam score Predictor")
st.write("Enter hors studied to predict the exam score.")
#user input
hours=st_number_input("Hours Studied:",min_value=0.0, step=0.1)
#Predict Button
if st.button("Predict Score"):
    predicted_score=model.predict([[hours]])[0]
    st.success(f"Predicted score: {predicted_score:.2f}")
#show sample data
    st.write("###Sample Training Data")
    st.dataframe(df)
