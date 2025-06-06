import streamlit as st
import base64


st.set_page_config(page_title="Jabbar Jatoi Portfolio", layout="wide")


def set_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <style>
        /* Hide top menu and watermark */
        header {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}

        /* Full background image */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Make all fonts white */
        html, body, [class*="st-"] {{
            color: white !important;
        }}

        /* Centered title above everything */
        .main-title {{
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 9999;
            font-size: 48px;
            font-weight: bold;
            color: white;
            background-color: rgba(0, 0, 0, 0.6);
            padding: 10px 30px;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
        }}

        .content-box {{
            background-color: rgba(0, 0, 0, 0.75);
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
            max-width: 1000px;
            margin: 5rem auto 2rem auto;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: white !important;
        }}

        a {{
            color: #66ccff !important;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}
        </style>

        <div class="main-title">Jabbar Jatoi</div>
    """, unsafe_allow_html=True)

set_bg_image("background.jpg")


st.markdown('<div class="content-box">', unsafe_allow_html=True)


col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=150)
with col2:
    st.markdown("#### 🤖 Building intelligent AI agents to automate the future")


st.markdown("### 🧑‍💼 About Me")
st.markdown("""
I'm a Python Backend Developer specialized in building AI-powered tools and intelligent agent
