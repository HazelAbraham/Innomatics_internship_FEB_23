import streamlit as st
from matplotlib import image
import plotly.express as px
import pandas as pd
import os


#Absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

# Absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR,os.pardir)

# Absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR,"Resources")

IMAGE_PATH = os.path.join(dir_of_interest,"images","iris.jpeg")
DATA_PATH = os.path.join(dir_of_interest,"data","iris.csv")

st.title("Iris Dashboard")



# Displaying image
img = image.imread(IMAGE_PATH)
st.image(img)

# Displaying the Dataframe
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the species", df["Species"].unique())
col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df["Species"] == species] , x = "SepalLengthCm")
col1.plotly_chart(fig_1,use_container_width=True)

fig_2 = px.box(df[df["Species"]==species] , y = "SepalLengthCm")
col2.plotly_chart(fig_2,use_container_width=True)

