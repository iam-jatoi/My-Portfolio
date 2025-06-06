import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="Jabbar Jatoi Portfolio", layout="wide")

# Background image setup
def set_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }}
        .content-box {{
            background-color: rgba(0, 0, 0, 0.5);  /* More transparent now */
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }}
        a {{
            color: #66ccff;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: white;
        }}
        .main-title {{
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            color: white;
            margin-top: 1rem;
