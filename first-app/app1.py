import streamlit as st

st.title("Hierarchical Data viewer")
st.header("this is a header")
st.subheader("subheader")
st.caption("caption")


st.write("this is write")
st.text("this is fixed text")
st.code("v = variable()\nanother_call()", "python")
st.markdown("**bold**")
st.divider()

st.latex("...")

st.error("this is an error")
st.info("this is an error")
st.warning("this is a Warning")
st.success("this is an success")

st.balloons()
st.snow()