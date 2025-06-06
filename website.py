import streamlit as st
import base64

# --- Page config ---
st.set_page_config(page_title="Jabbar Jatoi Portfolio", layout="wide")

# --- Set custom background and fully control style ---
def set_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <style>
        /* REMOVE TOP BLACK LAYER */
        header {{ visibility: hidden; }}

        /* Set full page background image */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white !important;
        }}

        /* Override font colors globally */
        html, body, [class*="st-"], .markdown-text-container {{
            color: white !important;
        }}

        .content-box {{
            background-color: rgba(0, 0, 0, 0.75);
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
            max-width: 1000px;
            margin: 3rem auto;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: #ffffff !important;
        }}

        a {{
            color: #66ccff !important;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- Apply background image ---
set_bg_image("background.jpg")

# --- Main content container ---
st.markdown('<div class="content-box">', unsafe_allow_html=True)

# Profile section
col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=150)
with col2:
    st.markdown("## Jabbar Jatoi")
    st.markdown("#### 🤖 Building intelligent AI agents to automate the future")

# About Me
st.markdown("### 🧑‍💼 About Me")
st.markdown("""
I'm a Python Backend Developer specialized in building AI-powered tools and intelligent agents using OpenAI SDKs, Chainlit, and Streamlit.  
I love crafting systems that think, learn, and solve real-world problems.
""")

# Skills
st.markdown("### 🛠️ Skills")
st.markdown("""
- 🐍 **Python** – Logic, scripting, backend systems  
- 🔗 **Chainlit** – Fast UI for LLM agents  
- 🤖 **OpenAI Agents SDK** – Autonomous decision-making systems  
- 🌐 **Streamlit** – Interactive web apps with Python  
""")

# Projects
st.markdown("### 📂 Projects")
st.markdown("""
- 🤖 **Chatbot** – AI chatbot using OpenAI & Chainlit  
- 🚦 **Traffic Signal Simulation** – Logic-driven Python simulation  
- 📈 **Nexa** – Data-driven analytics project (details TBD)  
""")

# Contact
st.markdown("### 📬 Contact")
st.markdown("""
- ✉️ **Email:** [jabbar.jatoi99@gmail.com](mailto:jabbar.jatoi99@gmail.com)  
- 🐙 **GitHub:** [github.com/iam-jatoi](https://github.com/iam-jatoi)  
- 🔗 **LinkedIn:** [linkedin.com/in/jabbar-jatoi-621510bb](https://www.linkedin.com/in/jabbar-jatoi-621510bb/)  
""")

st.markdown('</div>', unsafe_allow_html=True)
