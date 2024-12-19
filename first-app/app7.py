import urllib.parse
import pandas as pd
import streamlit as st
from io import StringIO

def getGraph(df):
    edges = ""
    for _, row in df.iterrows():
        if not pd.isna(row.iloc[1]):
           edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'
    return f'digraph{{\n{edges}}}'

def OnShowList(filename):
    if "names" in st.session_state:
        filenames = st.session_state["names"]
        if filename in filenames:
            st.error("Critical file found!")
            st.stop()


@st.cache_data
def loadFile(filename):
    return pd.read_csv("first-app/data/what_if_test15.csv", header=0).convert_dtypes()
st.title("Heirarchical Data Viewer")

if "names" in st.session_state:
    filenames = st.session_state["names"]
else:
    filenames = ["what_if_test15.csv"]
    st.session_state["names"] = filenames

filename = "data/what_if_test15.csv"
uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file" , type=["csv"], accept_multiple_files=False)
if uploaded_file is not None:
    filename = StringIO(uploaded_file.getvalue().decode("utf-8"))
    file =uploaded_file.name
    if file not in filenames:
        filenames.append(file)

btn = st.sidebar.button("Show List",
     on_click = OnShowList, args=("portfolio.csv"))
if btn:
   for f in filenames:
       st.sidebar.write(f)

df_orig=loadFile(filename)
cols= list(df_orig.columns)

with st.sidebar:
     child = st.selectbox("Child Column Name", cols, index=0)
     parent = st.selectbox("parent column Nmae", cols, index=1)
     df = df_orig[[child, parent]]
        

tabs = st.tabs(["Source", "Graph", "Dot Code"])

tabs[0].dataframe(df, use_container_width=True, hide_index=True)

chart= getGraph(df)
tabs[1].graphviz_chart(chart, use_container_width=True)

url = f'https://magjac.com/graphviz-visual-editor/?dote={urllib.parse.quote(chart)}'       
tabs[2].link_button("visualize Online", url)
tabs[2].code(chart)