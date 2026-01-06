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


check=st.checkbox("同意")
st.write(f"狀態: {check}")
import streamlit as st

name=st.text_input("輸入名字:")
st.write("名字:",name)

check=st.checkbox("同意")
st.write("狀態:",check)

fruit=st.selectbox(
    "你喜歡的水果:",
    ["蘋果","香蕉","草莓","芒果"]
)
st.write("水果:",fruit)

gender=st.radio(
    "性別",
    ["男","女","其他"]
)
st.write("性別",gender)

message=st.text_area("請輸入意見:")
st.write("你的意見:")
st.write(message)

age=st.number_input(
    "請輸入年齡:",
    min_value=0,
    max_value=120,
    step=1
)
st.write("你的年齡:",age)

birthday=st.date_input("請選擇日期")
st.write("生日:",birthday)






