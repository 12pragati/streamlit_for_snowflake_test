import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.title("Hierarchical Data Charts")

df=pd.read_csv("data/what_if_test15.csv", header=0).convert_dtypes()
st.dataframe(df)

labels = df[df.columns[1]]
parents = df[df.columns[2]]

data = go.Treemap(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgray")
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)


data = go.Icicle(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgray")
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)


data = go.Sunburst(
    ids=labels,
    labels=labels,
    parents=parents,
    insidetextorientation='horizontal')
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)


#