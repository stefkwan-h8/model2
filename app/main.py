import streamlit as st

import pickle
model_nb = pickle.load(open("model/model_student_placement_nb.pkl", "rb"))

from utils import head, body

hasil = head()

if st.button("Submit"):
    gender, workex, nilai = hasil

    g = {"wanita":0, "pria":1}
    w = {"belum pengalaman bekerja":0, "sudah ada pengalaman bekerja":1}

    input_model = [[g[gender], w[workex], nilai]]

    hasil_prediksi = model_nb.predict(input_model)[0]
    
    h = {0:"Tidak dapat tawaran kerja, not placed", 1:"Dapat tawaran kerja, placed"}

    body("hasil prediksi:" + h[hasil_prediksi])