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
column_names = ['Motorbrandstof', 'Perioden', 'gemiddelde_pompprijs', 'prijs_snelweg_bemand',
                'prijs_niet_snelweg_bemand', 'prijs_niet_snelweg_onbemand']
df.columns = column_names

# Prices > floats
df['gemiddelde_pompprijs'] = df['gemiddelde_pompprijs'].str.replace(',', '.')
df['gemiddelde_pompprijs'] = df['gemiddelde_pompprijs'].astype(float)
df['prijs_snelweg_bemand'] = df['prijs_snelweg_bemand'].str.replace(',', '.')
df['prijs_snelweg_bemand'] = df['prijs_snelweg_bemand'].astype(float)
df['prijs_niet_snelweg_bemand'] = df['prijs_niet_snelweg_bemand'].str.replace(',', '.')
df['prijs_niet_snelweg_bemand'] = df['prijs_niet_snelweg_bemand'].astype(float)
df['prijs_niet_snelweg_onbemand'] = df['prijs_niet_snelweg_onbemand'].str.replace(',', '.')
df['prijs_niet_snelweg_onbemand'] = df['prijs_niet_snelweg_onbemand'].astype(float)

# Convert months to decimal values
df['Perioden'] = df['Perioden'].str.replace(' ', '')
df['Perioden'] = df['Perioden'].str.replace('januari', '-01')
df['Perioden'] = df['Perioden'].str.replace('februari', '-02')
df['Perioden'] = df['Perioden'].str.replace('maart', '-03')
df['Perioden'] = df['Perioden'].str.replace('april', '-04')
df['Perioden'] = df['Perioden'].str.replace('mei', '-05')
df['Perioden'] = df['Perioden'].str.replace('juni', '-06')
df['Perioden'] = df['Perioden'].str.replace('juli', '-07')
df['Perioden'] = df['Perioden'].str.replace('augustus', '-08')
df['Perioden'] = df['Perioden'].str.replace('september', '-09')
df['Perioden'] = df['Perioden'].str.replace('oktober', '-10')
df['Perioden'] = df['Perioden'].str.replace('november', '-11')
df['Perioden'] = df['Perioden'].str.replace('december', '-12')

# Convert string > datetime datatype
df['Perioden'] = pd.to_datetime(df['Perioden'], format='%Y-%m')

# Subset the dataframe to split fuels
df_benzine = df[df['Motorbrandstof'] == 'Benzine Euro95']
df_diesel = df[df['Motorbrandstof'] == 'Diesel']
df_lpg = df[df['Motorbrandstof'] == 'Lpg']


# st.line_chart(data=df_benzine, x='Perioden', y='gemiddelde_pompprijs')