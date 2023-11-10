import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Explaration Data Analysis')
#Memanggil data csv 
    df= pd.read_csv(r'wines_SPA.csv')

#menampilakn 10 data teratas
    st.table(df.head(10))


#menampilakn plotbar
    st.title('10 Produsen Wine dengan harga rata - rata tertinggi')
    image = Image.open('WINERY.png')
    st.image(image, caption='Top 10 Produsen Wine')

# #menampilkan penjelasan 
    with st.expander('Penjalasan'):
        st.caption('Dari visualisasi ini, terdapat 10 produsen wine memiliki harga rata-rata yang lebih tinggi daripada yang lain. Saya menyimpilkan bahwa produsen-produsen tersebut mungkin menghasilkan wine dengan kualitas yang lebih tinggi atau memiliki reputasi yang baik di pasar atau mungkin tergantung dari usia wine tersebut, yang memungkinkan mereka untuk menetapkan harga yang lebih tinggi.')

    st.title('10 Jenis Wine dengan harga rata - rata tertinggi')
    image = Image.open('types.png')
    st.image(image, caption='Top 10 Jenis Wine')

    with st.expander('Penjalasan'):
        st.caption('Dari visualisasi ini, kita dapat menyimpulkan bahwa ada perbedaan yang signifikan dalam harga rata-rata antara jenis wine. Beberapa jenis wine mungkin memiliki harga yang lebih tinggi daripada yang lain, dan ini bisa disebabkan oleh berbagai faktor seperti popularitas, kualitas, atau kelangkaan jenis wine tersebut.')

    st.title('Harga tertinggi berdasarkan Tahun')
    image = Image.open('year.png')
    st.image(image, caption='Tahun vs Wine')

    with st.expander('Penjelasan'):
        st.caption('Setelah dilihat, ternyata tahun pembuatan tidak begitu berpengaruh terhadap harga. Sehingga walaupun usia wine tersebut sangat tua belum tentu harganya mahal.')