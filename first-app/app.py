import webbrowser
import urllib.parse
import pandas as pd
import streamlit as st

st.title("Heirarchical Data Viewer")

df=pd.read_csv("first-app/data/what_if_test15.csv", header=0).convert_dtypes()
st.dataframe(df)

edges = ""
for _, row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'

d = f'digraph{{\n {edges}}}' 
st.graphviz_chart(d)
#url = f'https://magjac.com/graphviz-visual-editor/?dote={urllib.parse.quote(d)}'       
#webbrowser.open(url)