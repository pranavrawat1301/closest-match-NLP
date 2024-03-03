import streamlit as st
from rapidfuzz import process

# Initial list of items
initial_items = ["US", "UK", "Canada", "Germany", "France", "Japan", "Australia", "China", "India", "Brazil"]

# Function to find the closest match using fuzzy matching
def find_closest_match(query, items, confidence_threshold):
    matches = process.extractBests(query, items, score_cutoff=confidence_threshold)
    return matches[0] if matches else ("No match", 0)

# Streamlit app
def main():
    st.title("Sophisticated Closest Match Finder")

    # User input
    user_input = st.text_input("Type a country:", "").strip()

    # Confidence threshold slider
    confidence_threshold = st.slider("Confidence Threshold", 0, 100, 80, step=1)

    # Dynamic update of items array
    st.sidebar.header("Manage Items")
    new_item = st.sidebar.text_input("Add a new item:")
    if st.sidebar.button("Add Item") and new_item:
        initial_items.append(new_item)

    # Display current items
    st.sidebar.subheader("Current Items")
    st.sidebar.write(initial_items)

    # Find the closest match
    closest_match, confidence = find_closest_match(user_input, initial_items, confidence_threshold)

    # Display result
    st.write(f"Closest match: {closest_match}")
    st.write(f"Confidence: {confidence}%")

if __name__ == "__main__":
    main()


