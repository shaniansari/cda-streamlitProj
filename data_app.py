# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
import pandas as pd
import matplotlib

    

path = 'C:\\Karachi AI\\Class 2 - 14Jan2023\\Data Manipulation\\'

filename = 'Billionaire.csv'
complete_filepath = path + filename 

df = pd.read_csv(filename)

bill_count=df.groupby("Country")['Name'].count().sort_values(ascending=False).head(10)
print(bill_count)
st.bar_chart(bill_count)
st.dataframe(bill_count)

## Source of income

group_by_source = df.groupby('Source')
source_count = group_by_source['Name'].count()
print(source_count.sort_values(ascending=False))


## interactivity


## Fixation of data
def fix_networth(value):
    subset = value[1:-2]
    converted = float(subset)
    return converted

df['NetWorth'] = df['NetWorth'].apply(fix_networth)

## Cummlative wealth of USA

cum_wealth = df[df['Country']=="United States"]['NetWorth'].sum()
print(cum_wealth)



col1, col2=st.columns(2)


countries=df['Country'].unique()
selection=col1.selectbox("SELEC COUNTIRES", countries)
subset=df[df['Country']==selection]

sources=sorted(subset['Source'].unique())
selection2=col1.multiselect("SELEC SOURCES", sources)
subset2=subset[subset['Source'].isin(selection2)]


#header_str=slection+" - Billionaiers" 
header_str="{} - Billionaires".format(selection)

col2.header(header_str)
col2.dataframe(subset)
col2.header("Source-wise info")
col2.dataframe(subset2)


