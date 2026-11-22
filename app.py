import streamlit as st

import queries
from db import connect, reset

conn = connect()

st.title("Art Sales Tracker")
st.write("Pick a page in the sidebar.")

st.dataframe(queries.show_inventory(conn))

if st.button("Reset"):
    conn.close()
    reset()
    st.rerun()
