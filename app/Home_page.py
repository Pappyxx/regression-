import streamlit as st

def home_page():
    st.title("Welcome to the House Price Prediction App")
    
    st.image("C:\Users\hp\Desktop\Houseregression\app\images.jpg", caption="House Image", width=500)
    
    st.markdown("""
                predicting house privescan be challenging but wirh the power of machine learning,
                we make it simple and efficient!. This app is designed to help uzers estimate house prices based on a variety of features like location,age,rooms and more""")
    
    st.markdown("""
                 ### How it works: 
                 1. Input the features of the houses such as longitude, latitude,tools rooms, households, and ocean proximity.
                 2. our Machinelearning model, trained on historical data, will predict the median house values for your inputs.
                 3. Explore feature insights and visualize dada trends using our interactive dashboard.
                 """)
    
    st.markdown("""
    ### About this project:
    """)
    st.info("""
            thios project uses a dataset that contains house pricing data from california, including features like location, number of rooms,
            and proximity to the ocean. With this app, you can explore how different features influence house prices and MAKE YOUR OWN PREDICTIONS!""")