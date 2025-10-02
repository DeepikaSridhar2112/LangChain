import streamlit as st
from utils import generate_script
# Inject CSS with targeted styling
st.markdown(
    """
    <style>
   div.stButton > button:first-child {
        background-color: black !important;
        color: white !important;
        transition: background-color 0.3s ease;
    }

   div.stButton > button:hover{
        background-color: #45a049 !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
if 'API_Key' not in st.session_state:
    st.session_state['API_Key']=''

st.sidebar.title(":smiley: :key:")
st.session_state['API_Key']=st.sidebar.text_input("Whats your API key?", type = "password")
st.sidebar.image('./logo.png', width=300, use_container_width=True)
st.divider()
st.title(":heart: Youtube Script Writing Tool")
topic = st.text_area("Please provide topic of the video")
video_length = st.text_area("Expected Video Length :time: (in minutes)")
creative_limit = st.slider("Select the level for creativity", min_value=0.0, max_value=1.0, step=0.1)
script_button = st.button("Generate script for me")
if script_button:
      if st.session_state.get('API_Key'):
              search_result, script,title= generate_script(topic,video_length,creative_limit,st.session_state['API_Key'])
              st.success("Hope you like the script")
              st.subheader(title)
              st.subheader(script)
              st.subheader("Check out DuckDuck go :search:")
              with st.expander("Show me :eyes:"):
                   st.info(search_result)
      else:
               st.error("OOPS! you didnt provide any API Key")

