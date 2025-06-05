import streamlit as st

# Page configuration
st.set_page_config(page_title="Jabbar Jatoi Portfolio", layout="wide")

# Header Section
col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=150)  # Picture must be in same folder on GitHub
with col2:
    st.title("👋 Assalamualaikum, I'm Jabbar Jatoi")
    st.subheader("💻 Python Backend Developer | AI & LLM Enthusiast")

# About Section
st.markdown("### 🧑‍💼 About Me")
st.write("""
I'm a Python Backend Developer skilled in building AI-powered tools using OpenAI, Chainlit, and Streamlit. 
I enjoy solving real-world problems with automation and intelligent agents.
""")

# Skills Section
st.markdown("### 🛠️ Skills")
st.write("""
- ✅ Python  
- ✅ Chainlit  
- ✅ OpenAI Agents SDK  
- ✅ Streamlit  
""")

# Projects Section
st.markdown("### 📂 Projects")
st.write("""
- 🤖 *Chatbot* – Built with Chainlit & OpenAI for interactive conversations  
- 🚦 *Traffic Signal Simulation* – Python-based simulation for smart traffic management  
- 📈 *Nexa* – Data-driven project (details can be added)  
""")

# Contact Section
st.markdown("### 📬 Contact")
st.write("📧 Email: jabbar.jatoi99@gmail.com")
st.write("🔗 GitHub: [github.com/iam-jatoi](https://github.com/iam-jatoi)")
st.write("🌐 LinkedIn: [linkedin.com/in/jabbar-jatoi-621510bb](https://www.linkedin.com/in/jabbar-jatoi-621510bb/)")

# Optional: Resume download button (if you add 'resume.pdf' to your repo)
# with open("resume.pdf", "rb") as file:
#     st.download_button(
#         label="📥 Download Resume",
#         data=file,
#         file_name="Jabbar_Jatoi_Resume.pdf",
#         mime="application/pdf"
#     )