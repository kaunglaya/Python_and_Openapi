import streamlit as st

st.title("次數的範例")
count = 0 #頁面上一開始會顯示0

increament = st.button("每次加1") #生成按鈕
if increament :
    count += 1

st.write("次數=",count)