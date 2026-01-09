import streamlit as st
import os
import json


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

    st.session_state.save_data.insert(0,dic)

display_data=[]
for i,item in enumerate(st.session_state.save_data,start=1):
    row=item.copy()
    row["編號"]=i
    display_data.append(row)
st.dataframe(display_data)

st.subheader("資料列表")

for i,item in enumerate(st.session_state.save_data):
    c1,c2,c3=st.columns([1,5,1])

    with c1:
        st.write(i+1)

    with c2:
        st.write(item)

    with c3:
        if st.button("刪除",key=f"del_{i}"):
            st.session_state.save_data.pop(i)
            st.rerun()


def save_to_file():
    with open("data.json","w",encoding="utf-8") as f:
        json.dump(st.session_state.save_data,f,ensure_ascii=False,indent=2)

if st.button("save"):
    save_to_file()

def show_file():
    if os.path.exists("data.json"):   
        with open("data.json","r",encoding="utf-8") as f:
            return json.load(f)
    return []

if st.button("show"):
    st.write(show_file())


        
