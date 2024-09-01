import streamlit as st
# Sidebar Title
st.title("Game Rules")

# Concise Rules Content
rules = """
- **Dragon** beats **Warrior**, but **Thief** can steal from Dragon.
- **Warrior** beats **Thief**, but is no match for **Dragon**.
- **Thief** steals from **Dragon**, but loses to **Warrior**.
"""

# Display the rules in the sidebar
st.markdown(rules, unsafe_allow_html=True)
