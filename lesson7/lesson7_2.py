from tools import taipei
import streamlit as st

@st.dialog("internet incorrect")
def vote(error):
    st.write(error)

try:
    youbikes_data:list[dict] = taipei.get_youbikes()
except Exception as error:
    vote(error)
    st.write("try it again")
    st.stop()
else:
    st.write(youbikes_data)