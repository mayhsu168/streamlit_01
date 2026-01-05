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

