




import streamlit as st

st.title("jaseem's Portfolio")

st.header("About Us")
st.write("""
I am a BCA student interested in AI, data analytics, and web development.
I enjoy learning new technologies and building creative projects.
""")


st.header("Skills",divider="green" )

st.markdown("- python\n- pandas \n-tablueau \n- sql \n- html \n- css \n- js")

st.header("code",divider="green")
st.caption("source: jaseem_w1d1.csv")
st.code("df=pd.read_csv('data/jaseem_w1d1.csv')",language="python")
st.header("result",divider="green")
st.latex(r'\text{jaseem}=\frac{\text{jaseem}}{\text{jaseem}}')