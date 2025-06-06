import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Jabbar Jatoi Portfolio", layout="wide")

# Function to set background image
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
        }}
        .content-box {{
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
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
            color: #ffffff;
        }}
        </style>
    """, unsafe_allow_html=True)

# 👇 Change 'background.jpg' to your actual background image filename
set_bg_image("background.jpg")

# --- Main content below ---
st.markdown('<div class="content-box">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=150)  # Make sure this image also exists
with col2:
    st.title("Jabbar Jatoi")
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
- ✉️ *Email:* [jabbar.jatoi99@gmail.com](mailto:jabbar.jatoi99@gmail.com)  
- 🐙 *GitHub:* [github.com/iam-jatoi](https://github.com/iam-jatoi)  
- 🔗 *LinkedIn:* [linkedin.com/in/jabbar-jatoi-621510bb](https://www.linkedin.com/in/jabbar-jatoi-621510bb/)  
""")

st.markdown('</div>', unsafe_allow_html=True)
