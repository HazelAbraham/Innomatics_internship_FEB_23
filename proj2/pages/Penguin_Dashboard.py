import streamlit as st
import pandas as pd
from matplotlib import image
import plotly.express as px
import os

# Absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

# Absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR,os.pardir)

# Absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR,"Resources")

IMAGE_PATH = os.path.join(dir_of_interest,"Image","Penguin.jpeg")
DATA_PATH = os.path.join(dir_of_interest,"Data","Penguin.csv")

st.title("_Penguins_")

# Displaying image
img = image.imread(IMAGE_PATH)
st.image(img)

# Displaying the Dataframe
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the species of penguin", df["Species"].unique())
col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df["Species"] == species] , x = "Culmen Length (mm)")
col1.plotly_chart(fig_1,use_container_width=True)

fig_2 = px.box(df[df["Species"]==species] , y = "Culmen Length (mm)")
col2.plotly_chart(fig_2,use_container_width=True)

fig_3 = px.histogram(df[df["Species"]==species] , x = "Flipper Length (mm)")
col1.plotly_chart(fig_3,use_container_width=True)

fig_4 = px.box(df[df["Species"]==species] , y = "Flipper Length (mm)")
col2.plotly_chart(fig_4,use_container_width=True)


