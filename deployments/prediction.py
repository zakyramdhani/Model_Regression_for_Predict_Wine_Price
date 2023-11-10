import streamlit as st
import pandas as pd
import pickle

def run():
# Load All Files

    with open('fix_model.pkl', 'rb') as file:
        best_model = pickle.load(file)


    rating = st.selectbox(label='Silahkan pilih Rating disini',options=['4.0', '4.1', '4.2', '4.3', '4.5', '4.6', '4.7', '4.6', '4.7', '4.8', '4.9', '5.0'])
    body = st.selectbox(label='Silahkan pilih Body Score[1-5]',options=['1.0', '2.0', '3.0', '4.0', '5.0'])
    acidity = st.selectbox(label='Silahkan pilih Acidity Score[1-5]',options=['1.0', '2.0', '3.0' , '4.0', '5.0'])
    year = st.number_input(label='Silahkan pilih Year disini, mulai dari 1900 - 2020',min_value=1900,max_value=2020)
    
    st.write('Dibawah ini merupakan data yang sudah anda input : ')
    
    data_inf = pd.DataFrame({
         'rating' : rating,
        'body' : body,
        'acidity' : acidity ,
        'year' : year,
        }, index=[0])

    st.table(data_inf)


    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        pred_inf = best_model.predict(data_inf)

        
        st.metric(label="Hasil dari Prediksi harga wine anda: ", value = pred_inf[0])