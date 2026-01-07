import streamlit as st

st.title("資料送出清空")

if "save_data" not in st.session_state:
    st.session_state.save_data=[]

if "name" not in st.session_state:
    st.session_state.name=""
    st.session_state.grender="man"
    st.session_state.age=0
    st.session_state.birthday=None
    st.session_state.fruit="apple"
    st.session_state.message=""
    st.session_state.aggre=False

st.text_input("name",key="name")
st.radio("grender",["man","feman"],key="grender")
st.number_input("age",min_value=0,max_value=120,step=1,key="age")
st.date_input("birthday",key="birthday")
st.selectbox("fruit",["apple","banana","orange"],key="fruit")
st.text_area("message",key="message")
st.checkbox("agree",key="agree")

if st.button("submit"):
    dic={
        "name":st.session_state.name,
        "gender":st.session_state.grender,
        "age":st.session_state.age,
        "birthday":st.session_state.birthday,
        "fruit":st.session_state.fruit,
        "message":st.session_state.message,
        "agree":st.session_state.agree
    }

    st.session_state.save_data.append(dic)

    st.session_state.name=""
    st.session_state.grender="man"
    st.session_state.age=0
    st.session_state.birthday=None
    st.session_state.fruit="apple"
    st.session_state.message=""
    st.session_state.aggre=False

st.write(st.session_state.save_data)
   
