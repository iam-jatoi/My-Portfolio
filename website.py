import streamlit as st


st.set_page_config(page_title="Jabbar Jatoi Portfolio", layout="wide")


col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=150)
with col2:
    st.title("Jabbar Jatoi")
    st.markdown("#### 🤖 Building intelligent AI agents to automate the future") 


st.markdown("### 🧑‍💼 About Me")
st.write("""
I'm a Python Backend Developer skilled in building AI-powered tools using OpenAI, Chainlit, and Streamlit. 
I enjoy solving real-world problems with automation and intelligent agents.
""")


st.markdown("### 🛠️ Skills")
st.write("""
- ✅ Python  
- ✅ Chainlit  
- ✅ OpenAI Agents SDK  
- ✅ Streamlit  
""")


st.markdown("### 📂 Projects")
st.write("""
- 🤖 *Chatbot* – Built with Chainlit & OpenAI for interactive conversations  
- 🚦 *Traffic Signal Simulation* – Python-based simulation for smart traffic management  
- 📈 *Nexa* – Data-driven project (details can be added)  
""")


st.markdown("### 📬 Contact")
st.write("📧 Email: jabbar.jatoi99@gmail.com")
st.write("🔗 GitHub: [github.com/iam-jatoi](https://github.com/iam-jatoi)")
st.write("🌐 LinkedIn: [linkedin.com/in/jabbar-jatoi-621510bb](https://www.linkedin.com/in/jabbar-jatoi-621510bb/)")
