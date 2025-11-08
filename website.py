import streamlit as st
import base64

# Page configuration
st.set_page_config(page_title="Abdul Jabbar Portfolio", layout="wide")

def set_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
        color: #f9f9f9; /* Light text for dark overlay */
        position: relative;
    }}

    /* Dark overlay for readability */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.45);
        z-index: -1;
    }}

    /* Banner styling */
    .banner-container {{
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }}

    .main-banner {{
        display: inline-block;
        background-color: rgba(0, 0, 0, 0.65);
        padding: 1.2rem 2.5rem;
        border-radius: 14px;
        box-shadow: 0 4px 25px rgba(0,0,0,0.3);
    }}

    .main-banner h1 {{
        font-size: 3.5rem;
        font-weight: 700;
        color: #00e0ff;
        margin: 0;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }}

    /* Content box with slightly transparent dark theme */
    .content-box {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 0 25px rgba(0,0,0,0.5);
    }}

    h2, h3, h4, h5, h6 {{
        color: #00e0ff !important;
        font-weight: 600;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.6);
    }}

    p, li {{
        color: #f1f1f1 !important;
        font-size: 1.1rem;
        line-height: 1.6;
    }}

    a {{
        color: #00e0ff;
        text-decoration: none;
        font-weight: 500;
    }}
    a:hover {{
        text-decoration: underline;
    }}
    </style>

    <div class="banner-container">
        <div class="main-banner">
            <h1>Abdul Jabbar</h1>
        </div>
    </div>
    """
    st.markdown(css, unsafe_allow_html=True)

# Apply background
set_bg_image("background.jpg")

# Main content box
st.markdown('<div class="content-box">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=160)
with col2:
    st.markdown("#### 🤖 Building intelligent AI agents to automate the future")

st.markdown("### 🧑‍💼 About Me")
st.write("""
I'm a Python Backend Developer specialized in building AI-powered tools and intelligent agents using OpenAI SDKs, Chainlit, and Streamlit.  
I love crafting systems that think, learn, and solve real-world problems.
""")

st.markdown("### 🛠️ Skills")
st.markdown("""
- 🐍 *Python* – Logic, scripting, backend systems  
- 🔗 *Chainlit* – Fast UI for LLM agents  
- 🤖 *OpenAI Agents SDK* – Autonomous decision-making systems  
- 🌐 *Streamlit* – Interactive web apps with Python  
""")

st.markdown("### 📂 Projects")
st.markdown("""
- 🤖 *Chatbot* – AI chatbot using OpenAI & Chainlit  
- 🚦 *Traffic Signal Simulation* – Logic-driven Python simulation  
- 📈 *Nexa* – Data-driven analytics project (details TBD)  
""")

st.markdown("### 📬 Contact")
st.markdown("""
- ✉️ **Email:** [jabbar.jatoi99@gmail.com](mailto:jabbar.jatoi99@gmail.com)  
- 🐙 **GitHub:** [github.com/iam-jatoi](https://github.com/iam-jatoi)  
- 🔗 **LinkedIn:** [linkedin.com/in/jabbar-jatoi-621510bb](https://www.linkedin.com/in/jabbar-jatoi-621510bb/)
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
