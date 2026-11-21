import streamlit as st

import queries
from db import connect, reset

conn = connect()

st.title("Art Sales Tracker")
st.write("Pick a page in the sidebar.")
# st.caption(f"Logs with no bed: {queries.orphan_count(conn)}")

if st.button("Reset"):
    conn.close()
    reset()
    st.rerun()
