import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import collections
import streamlit as st

df = pd.read_csv('findata.csv')

arr = df.iloc[:, 2:9].to_numpy()
freq_arr = []
for item in arr:
    kek = collections.Counter(item)
    freq_arr.append(dict(kek))

for item in freq_arr:
    if 1 in item.keys():
        item['Strongly Disagree'] = item.pop(1)
    if 2 in item.keys():
        item['Disagree'] = item.pop(2)
    if 3 in item.keys():
        item['Neutral'] = item.pop(3)
    if 4 in item.keys():
        item['Agree'] = item.pop(4)
    if 5 in item.keys():
        item['Strongly Agree'] = item.pop(5)

colours = {
    'Strongly Disagree': '#F13209',
    'Disagree': '#EB8D14',
    'Neutral': '#F7FF00',
    'Agree': '#69EC57',
    'Strongly Agree': '#199A07'
}

st.title('Review Pie Visualization')

st.subheader("Raw Data")
st.write(df)

# index = int(df.index[df['Question'] == q].to_list()[0])
index = st.slider('Select the Question',
                  min_value=1, max_value=25, step=1)
st.subheader(f'Question No : {index}')

index -= 1

labels = freq_arr[index].keys()
sizes = freq_arr[index].values()
fig, ax1 = plt.subplots()
ax1 = plt.pie(sizes, labels=labels, autopct='%1.2f%%',
              colors=[colours[key] for key in labels])
# ax2 = plt.hist(sizes)
st.pyplot(fig)

st.subheader(df['Question'][index])


arr = df.iloc[:, 2:9].to_numpy()
flat_arr = arr.flatten()
gross_arr = collections.Counter(flat_arr)


gross_arr = dict(gross_arr)

if 1 in gross_arr.keys():
    gross_arr['Strongly Disagree'] = gross_arr.pop(1)
if 2 in gross_arr.keys():
    gross_arr['Disagree'] = gross_arr.pop(2)
if 3 in gross_arr.keys():
    gross_arr['Neutral'] = gross_arr.pop(3)
if 4 in gross_arr.keys():
    gross_arr['Agree'] = gross_arr.pop(4)
if 5 in gross_arr.keys():
    gross_arr['Strongly Agree'] = gross_arr.pop(5)

st.text('')
st.text('')
st.text('')
st.text('')
st.text('')
st.header('Overall Data')

labels = gross_arr.keys()
sizes = gross_arr.values()
fig2, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct='%1.2f%%',
        colors=[colours[key] for key in labels])
st.pyplot(fig2)
st.subheader('This is the Overall Data.')
