import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TEXT
st.title('BASIC DATA ANALYSIS')
st.header("My Dashboard")
st.subheader("Dashboard 1")
st.markdown(
    """
    # My first app
    `streamlit run <file.py>`
    """
)
st.caption("Copyright (c) 2024")

st.text("Hello")

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")


df = pd.DataFrame({
    'feature':["feature","feature2","feature3"],
    'name':["a1","b1","c1"],
    'loc':["aa","bb","cc"]
})
# WRITE
st.write(df)

# Data Display
st.dataframe(data=df, width=500)

st.table(data=df)

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

st.json(df.to_json())

# Chart
x1 = np.random.normal(15, 5, 250)
x2 = np.random.normal(15, 5, 250)

fig, axs = plt.subplots(
    nrows=1,
    ncols=2,
    figsize=(13,5)
)
axs[0].hist(x=x1, bins=15)

axs[1].hist(x=x2, bins=15)

plt.suptitle("Test chart", fontsize=20)

st.pyplot(fig)