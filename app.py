import streamlit as st

st.title("Streamlit 小工具(list版)")

if "todos" not in st.session_state:
    st.session_state.todos=[]
    
todo=st.text_input("輸入待辦事項:")

if st.button("新增"):
    if todo:
        st.session_state.todos.append(todo)

st.write("待辦清單:")
for i,item in enumerate(st.session_state.todos,start=1):
    st.write(f"{i}.{item}")


if "save_data" not in st.session_state:
    st.session_state.save_date=[]

aggre=st.checkbox("agree")
name=st.text_input("name")
gender=st.radio("gender",["man","feman"])
age=st.number_input("age",min_value=0,max_value=120,step=1)
birthday=st.date_input("birday")
fruit=st.selectbox("fruit",["apple","banana","orange"])
message=st.text_area("message")

if st.button("submit"):
    dic={
        "aggre":aggre,
        "name":name,
        "gender":gender,
        "age":age,
        "birthday":birthday,
        "fruit":fruit,
        "message":message
    }  
    st.session_state.save_date.append(dic)

st.write(st.session_state.save_date)




