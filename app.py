import streamlit as st
from src.recommender import recommend

st.title("Smart Product Recommendation System")

product = st.text_input("Enter product name:")

if st.button("Get Recommendations"):
    if product:
        result = recommend(product)
        if result:
            st.success("Recommended Products:")
            for r in result:
                st.write(r)
        else:
            st.warning("No positive recommendations found")
    else:
        st.error("Please enter a product name")
