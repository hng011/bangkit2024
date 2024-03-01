import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

_options = ("Sidebar","Column1","Column2","Tabs","Container","Expander")
layout = st.radio(
    label="Layout type",
    options=_options
)

# Sidebar
if layout == _options[0]:
    st.title('HI There')
 
    with st.sidebar:
        
        st.text('Using Sidebar')
        
        values = st.slider(
            label='Select a range of values',
            min_value=0, max_value=100, value=(0, 100)
        )
        st.write('Values:', values)

# Column1
if layout == _options[1]:
    st.title('Using column')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("Col 1")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    
    with col2:
        st.header("Col 2")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    
    with col3:
        st.header("Col 3")
        st.image("https://static.streamlit.io/examples/owl.jpg")

# Column2
if layout == _options[2]:
    st.header("Columns with predefined ratio")
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.header("col 1")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    
    with col2:
        st.header("col 2")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    
    with col3:
        st.header("col 3")
        st.image("https://static.streamlit.io/examples/owl.jpg")

# Tabs
if layout == _options[3]:
    st.header("Dashboard")
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
    with tab1:
        st.header("Tab 1")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    
    with tab2:
        st.header("Tab 2")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    
    with tab3:
        st.header("Tab 3")
        st.image("https://static.streamlit.io/examples/owl.jpg")

# Container
if layout == _options[4]:
    with st.container():
        st.write("Inside the container")
        
        x = np.random.normal(15, 5, 250)
    
        fig, ax = plt.subplots()
        ax.hist(x=x, bins=15)
        st.pyplot(fig) 
 
    st.write("Outside the container")  

# Expander
if layout == _options[5]:
    x = np.random.normal(15, 5, 250)
    
    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig) 
    
    with st.expander("See explanation"):
        st.write(
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
            in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
            nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
            sunt in culpa qui officia deserunt mollit anim id est laborum.
            """
        )
