import streamlit as st

st.title("我的第一個 Streamlit 小工具")
st.write("Hello Streamlit 👋")

name = st.text_input("請輸入你的名字")

if name:
    st.success(f"你好，{name}！")
