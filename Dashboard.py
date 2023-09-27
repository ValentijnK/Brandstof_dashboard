import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title='Dashboard'
)

# Load dataset
df = pd.read_csv('data.csv', delimiter=';')

# Rename Columns
column_names = ['motorbrandstof', 'perioden', 'gemiddelde_pompprijs', 'prijs_snelweg_bemand',
                'prijs_niet_snelweg_bemand', 'prijs_niet_snelweg_onbemand']
df.columns = column_names
st.dataframe(df)
# Prices > floats
df['gemiddelde_pompprijs'] = df['gemiddelde_pompprijs'].str.replace(',', '.')
df['gemiddelde_pompprijs'] = df['gemiddelde_pompprijs'].astype(float)
df['prijs_snelweg_bemand'] = df['prijs_snelweg_bemand'].str.replace(',', '.')
df['prijs_snelweg_bemand'] = df['prijs_snelweg_bemand'].astype(float)
df['prijs_niet_snelweg_bemand'] = df['prijs_niet_snelweg_bemand'].str.replace(',', '.')
df['prijs_niet_snelweg_bemand'] = df['prijs_niet_snelweg_bemand'].astype(float)
df['prijs_niet_snelweg_onbemand'] = df['prijs_niet_snelweg_onbemand'].str.replace(',', '.')
df['prijs_niet_snelweg_onbemand'] = df['prijs_niet_snelweg_onbemand'].astype(float)

# Drop rows with the average price
df = df.drop(df[df['perioden'].isin(['2022', '2023'])].index)

# Convert months to decimal values
df['perioden'] = df['perioden'].str.replace(' ', '')
df['perioden'] = df['perioden'].str.replace('januari', '-01')
df['perioden'] = df['perioden'].str.replace('februari', '-02')
df['perioden'] = df['perioden'].str.replace('maart', '-03')
df['perioden'] = df['perioden'].str.replace('april', '-04')
df['perioden'] = df['perioden'].str.replace('mei', '-05')
df['perioden'] = df['perioden'].str.replace('juni', '-06')
df['perioden'] = df['perioden'].str.replace('juli', '-07')
df['perioden'] = df['perioden'].str.replace('augustus', '-08')
df['perioden'] = df['perioden'].str.replace('september', '-09')
df['perioden'] = df['perioden'].str.replace('oktober', '-10')
df['perioden'] = df['perioden'].str.replace('november', '-11')
df['perioden'] = df['perioden'].str.replace('december', '-12')

# Convert string > datetime datatype
df['perioden'] = pd.to_datetime(df['perioden'], format='%Y-%m')

# Subset the dataframe to split fuels
df_benzine = df[df['motorbrandstof'] == 'Benzine Euro95']
df_diesel = df[df['motorbrandstof'] == 'Diesel']
df_lpg = df[df['motorbrandstof'] == 'Lpg']

st.dataframe(df_benzine)

# st.line_chart(data=df_benzine, x='perioden', y='gemiddelde_pompprijs')
