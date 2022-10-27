import streamlit as st
import base64


# Configure Page
st.set_page_config(page_title="Home Page",page_icon='data\icon.jpg',layout='wide')

st.title("i was created on 27/10/2022")

# Add Title
def title(url):
    st.markdown(f'<h1 style="text-align:center;background-color:#e32636;color:#a4c639;">{url}</h1>',unsafe_allow_html=True)

title("Disco Dancer")
 

"""### gif from local file"""
col1,col2,col3=st.columns(3)
file_ = open('data/jimmy.gif', "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

col2.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)



