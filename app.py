import streamlit as st

st.title("資料送出後清空資料")

if "save_data" not in st.session_state:
    st.session_state.save_data=[]

with st.form("aform",clear_on_submit=True):
    name=st.text_input("name")
    grender=st.radio("grender",["man","feman"])
    age=st.number_input("age",min_value=0,max_value=120,step=1)
    birthday=st.date_input("birthday")
    fruit=st.selectbox("fruit",["apple","banana","orange"])
    agree=st.checkbox("agree",value=False)
    message=st.text_area("message")
    sub=st.form_submit_button("submit")

if sub:
    dic={
        "name":name,
        "grender":grender,
        "age":age,
        "birthday":birthday,
        "fruit":fruit,
        "message":message,
        "agree":agree
    }

    st.session_state.save_data.append(dic)

st.write(st.session_state.save_data)
