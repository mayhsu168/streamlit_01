import streamlit as st

st.title("Streamlit 小工具")
todo=st.text_input("輸入待辦事項:")

if st.button("新增")：
    st.write("新增事項:",todo)
