import streamlit as st
import pandas as pd

st.title('Simple data dashboard')

uploaded_file=st.file_uploader('Upload a csv file',type='csv')
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write('File uploaded..')
    
    st.subheader('Data preview')
    st.write(df.head())
    
    st.subheader('Data summary')
    st.write(df.describe())
    
    st.subheader('Filter data')
    columns=df.columns.to_list()
    selected_column=st.selectbox("Choose the column to filter by",columns)
    unique_values=df[selected_column].unique()
    selected_value=st.selectbox("Choose the column to filter by",unique_values)
    filtered_df=df[df[selected_column]==selected_value] #Filters the dataframe to show only rows where the selected column matches the selected value.
    st.write(filtered_df)
    
    st.subheader('Plot data')
    x_columns=st.selectbox("Select the x-axis column",columns)
    y_columns=st.selectbox("Select the y-axis column",columns)
    if st.button("Generate Chart"):
        st.line_chart(filtered_df.set_index(x_columns)[y_columns])
        
else:
    st.write("Waiting for file upload")