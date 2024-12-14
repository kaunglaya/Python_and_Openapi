import streamlit as st

st.title("次數的範例")
if 'count' not in st.session_state: #儲存在餅乾裡，第二次的時候就不會返回到這個程式
    st.session_state['count'] = 0  

increament = st.button("每次加1") #生成按鈕
if increament :
    st.session_state['count'] += 1

increament = st.button("每次加10")
if increament:
    st.session_state["count"] += 10

increament = st.button("歸0")
if increament:
    st.session_state["count"] = 0

st.write("次數=",st.session_state['count'])

