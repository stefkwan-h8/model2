import streamlit as st

def head():
    st.title("Latihan Streamlit")
    g = st.radio("Gender", ["wanita", "pria"])
    w = st.radio("Work Experience", ["belum pengalaman bekerja", "sudah ada pengalaman bekerja"])
    n = st.number_input("Nilai Wawancara:", 0, 100, step=1)

    return [g,w,n]
    

def body(result):
    st.text("hello, saya text di function body")
    st.text(result)


