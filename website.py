import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="Jabbar Jatoi Portfolio", layout="wide")

# Background image setup with centered banner and white fonts
def set_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }}
        .content-box {{
            background-color: rgba(0, 0, 0, 0.5);
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
        h1, h2, h3, h4, h5, h6, p, li {{
            color: white !important;
        }}
        .main-banner {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 2rem;
            text-align: center;
            border-radius: 8px;
            margin-top: 1rem;
            margin-bottom: 2rem;
        }}
        .main-banner h1 {{
            font-size: 3em;
            font-weight: bold;
            color: white;
            margin: 0;
        }}
        </style>

        <div class="main-banner">
            <h1>Jabbar Jatoi</h1>
        </div>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call background setter
set_bg_image("background.jpg")

# Start content box
st.markdown('<div class="content-box">', unsafe_allow_html=True)

# Profile image and subtitle
col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=150)
with col2:
    st.markdown("#### 🤖 Building intelligent AI agents to automate the future")

# About Me
st.markdown("### 🧑‍💼 About Me")
st.write("""
I'm a Python Backend Developer specialized in building AI-powered tools and intelligent agents using OpenAI SDKs, Chainlit, and Streamlit.  
I love crafting systems that think, learn, and solve real-world problems.
""")

# Skills
st.markdown("### 🛠️ Skills")
st.markdown("""
- 🐍 *Python* – Logic, scripting, backend systems  
- 🔗 *Chainlit* – Fast UI for LLM agents  
- 🤖 *OpenAI Agents SDK* – Autonomous decision-making systems  
- 🌐 *Streamlit* – Interactive web apps with Python  
""")

# Projects
st.markdown("### 📂 Projects")
st.markdown("""
- 🤖 *Chatbot* – AI chatbot using OpenAI & Chainlit  
- 🚦 *Traffic Signal Simulation* – Logic-driven Python simulation  
- 📈 *Nexa* – Data-driven analytics project (details TBD)  
""")

# Contact
st.markdown("### 📬 Contact")
st.markdown("""
- ✉️ **Email:** [jabbar.jatoi99@gmail.com](mailto:jabbar.jatoi99@gmail.com)  
- 🐙 **GitHub:** [github.com/iam-jatoi](https://github.com/iam-jatoi)  
- 🔗 **LinkedIn:** [linkedin.com/in/jabbar-jatoi-621510bb](https://www.linkedin.com/in/jabbar-jatoi-621510bb/)
""", unsafe_allow_html=True)

# End content box
st.markdown("</div>", unsafe_allow_html=True)
