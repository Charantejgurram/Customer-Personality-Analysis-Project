# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:33:56 2023

@author: ajay3
"""

# importing necessary libraries
import pickle
import streamlit as st
import pandas as pd
import numpy as np

#load the model
classifier = pickle.load(open('classifier.pkl','rb'))


#page configuration
st.set_page_config(page_title = 'Customer Segmentation Web App', layout='centered')
st.title('Customer Segmentation Web App')

# customer segmentation function
def segment_customers(input_data):
    
    prediction=classifier.predict(pd.DataFrame(input_data, columns=['Income','Kidhome','Teenhome','Age','Partner','Education_Level']))
    print(prediction)
    pred_1 = 0
    if prediction == 0:
        pred_1 = 'cluster 0'

    elif prediction == 1:
            pred_1 = 'cluster 1'

    elif prediction == 2:
            pred_1 = 'cluster 2'

    elif prediction == 3:
            pred_1 = 'cluster 3'

    return pred_1

def main():
    
    Income = st.sidebar.text_input("Type In The Household Income")
    Kidhome = st.sidebar.radio ( "Select Number Of Kids In Household", ('0', '1','2') )
    Teenhome = st.sidebar.radio ( "Select Number Of Teens In Household", ('0', '1','2') )
    Age = st.sidebar.slider ( "Select Age", 18, 85 )
    Partner = st.sidebar.radio ( "Livig With Partner?", ('Yes', 'No') )
    Education_Level = st.sidebar.radio ( "Select Education", ("Undergraduate", "Graduate", "Postgraduate") )
    
    result = ""
    
    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Segment Customer"):
        result=segment_customers([[Income,Kidhome,Teenhome,Age,Partner,Education_Level]])
    
    st.success(result)
    

if __name__ == '__main__':
        main ()