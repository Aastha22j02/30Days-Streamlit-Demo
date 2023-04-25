import streamlit as st

st.title('st.secrets')

st.write(st.secrets['demo']['public_gsheets_url'])