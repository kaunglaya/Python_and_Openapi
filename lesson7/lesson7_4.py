import streamlit as st

st.title("次數的範例")
if 'count' not in st.session_state: #儲存在餅乾裡，第二次的時候就不會返回到這個程式
    st.session_state['count'] = 0  

increament = st.button("功德加1") #生成按鈕
if increament :
    st.session_state['count'] += 1

increament = st.button("功德加10")
if increament:
    st.session_state["count"] += 10

increament = st.button("回歸原功德")
if increament:
    st.session_state["count"] = 0

st.write("功德=",st.session_state['count'])

