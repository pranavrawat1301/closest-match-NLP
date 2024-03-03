# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15xQ-yFMcrDpkWMOPhR177D0yftmUw8Ml
"""


import streamlit as st
from fuzzywuzzy import process

# List of items
initial_items = ["US", "UK", "Canada", "Germany", "France", "Japan", "Australia", "China", "India", "Brazil"]

# Function to find the closest match using fuzzy matching
def find_closest_match(query, items):
    matches = process.extract(query, items, limit=1)
    return matches[0] if matches and matches[0][1] >= 80 else ("No match", 0)

# Streamlit app
def main():
    st.title("Closest Match Finder")

    # User input
    user_input = st.text_input("Type a country:", "").strip()

    # Dynamic update of items array
    st.sidebar.header("Manage Items")
    new_item = st.sidebar.text_input("Add a new item:")
    if st.sidebar.button("Add Item") and new_item:
        initial_items.append(new_item)

    # Display current items
    st.sidebar.subheader("Current Items")
    st.sidebar.write(initial_items)

    # Find the closest match
    closest_match, confidence = find_closest_match(user_input, items)

    # Display result
    st.write(f"Closest match: {closest_match}")
    st.write(f"Confidence: {confidence}%")

if __name__ == "__main__":
    main()



