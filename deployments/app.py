import streamlit as st
import eda
import prediction


page = st.sidebar.selectbox(label='Pilih Halaman:', options=['Beranda', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Beranda':
    st.header('Selamat Datang') 
    st.write('')
    st.caption('Silahkan pilih menu lain di sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Zaky Ramdhani')
    st.write('Batch     : HCK - 008')
    st.write('Tujuan Milestone    : Program ini dibuat untuk memprediksi harga sebuah wine berdasarkan rating, score body, score acidity, dan year.')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Wine dari Spanyol memiliki reputasi yang baik di pasar internasional, tetapi kualitasnya sangat bervariasi tergantung pada berbagai faktor. Para produsen wine dan pecinta wine selalu mencari cara untuk memahami faktor-faktor apa yang memengaruhi kualitas wine Spanyol. Untuk mengatasi hal ini, sebuah dataset telah dikumpulkan yang berisi informasi tentang 7500 jenis wine Spanyol yang berbeda. Dataset ini mencakup 11 fitur yang mencerminkan berbagai aspek kualitas dan karakteristik wine tersebut, termasuk harga, rating, dan deskripsi rasa. Analisis data pada dataset ini dapat memberikan wawasan berharga tentang faktor-faktor yang memengaruhi popularitas dan kualitas wine Spanyol.')

    with st.expander("Problem Statement"):
            st.caption('Dalam konteks dataset ini, beberapa permasalahan yang mungkin bisa dijelaskan melalui analisis data antara lain: Faktor-Faktor yang Mempengaruhi Kualitas Wine, Segmentasi Wine, Pengaruh Rating terhadap Harga.')

    with st.expander("Kesimpulan"):
        st.caption('Dataset ini memberikan kesempatan untuk menganalisis berbagai aspek wine Spanyol dan faktor-faktor yang memengaruhi popularitas dan kualitasnya. Dengan analisis yang tepat, kita dapat menemukan wawasan yang berharga bagi para produsen wine dan konsumen. Selain itu, kita dapat membangun model prediksi harga wine yang dapat digunakan untuk tujuan pengambilan keputusan di industri wine. Analisis data ini juga dapat membantu mempromosikan pemahaman lebih mendalam tentang wine Spanyol dan meningkatkan penghargaan terhadap kekayaan budaya dan kuliner negara ini.')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     prediction.run()