import streamlit as st
import streamlit.components.v1 as components

# Set Streamlit page config
st.set_page_config(page_title="Geospatial Map", layout="wide")

st.title("Interactive Geospatial Map 🌍")

# Read the HTML file
with open("map.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the HTML file in Streamlit
components.html(html_content, height=700, scrolling=True)
