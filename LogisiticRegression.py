import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

pickle_in = open("logistic.pkl","wb")

def prediction(PassengerId,Pclass,Sex,Age,SibSp,Parch,Fare,Cabin,Embarked):
    prediction = classifier.predict([PassengerId,Pclass,Sex,Age,SibSp,Parch,Fare,Cabin,Embarked])
    print(prediction)
    return prediction

def main():
    st.title("Logistic Regression model")
    html_temp = "<div style="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1> 
    </div> ""   
    st.markdown(html_temp,unsafe_allow_html=True)
    PassengerId = st.text_input("Passenger ID", "Type Here")
    Pclass = st.text_input("Pclass", "Type Here")
    Sex = st.text_input("Sex", "Type Here")
    Age = st.text_input("Age", "Type Here")
    SibSp = st.text_input("SibSp", "Type Here")
    Parch = st.text_input("Parch", "Type Here")
    Fare = st.text_input("Fare,", "Type Here")
    Cabin = st.text_input("Cabin", "Type Here")
    Embarked = st.text_input("Embarked ", "Type Here")

    if st.button("Predict"):
        result = prediction(PassengerId,Pclass,Sex,Age,SibSp,Parch,Fare,Cabin,Embarked)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()



