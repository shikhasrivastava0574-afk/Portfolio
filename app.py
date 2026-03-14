import streamlit as st

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(page_title="Portfolio | Shikha Srivastava", layout="wide", page_icon="✨")

# 2. Custom CSS for Attractive Styling
st.markdown("""
<style>
    /* Styling for project and research cards */
    .custom-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 20px;
        color: white;
    }
    /* Hover effect for cards */
    .custom-card:hover {
        transform: scale(1.01);
        transition: 0.3s;
        box-shadow: 0 4px 8px 0 rgba(255, 75, 75, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# 3. Hero Section (Header)
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Shikha Srivastava [cite: 1]")
    st.subheader("Data Science & Machine Learning Specialist [cite: 4]")
    st.markdown("📍 Jaipur, Rajasthan | 📞 +91 8955230864 | ✉️ shikhasrivastava0574@gmail.com [cite: 2]")
    st.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com) [cite: 2]")

st.markdown("---")

# 4. Navigation Tabs
tab_about, tab_projects, tab_research, tab_skills = st.tabs(["👤 About Me", "🚀 Projects", "🔬 Research", "💻 Technical Skills"])

# --- TAB 1: ABOUT ME ---
with tab_about:
    st.header("Summary")
    st.write("Machine learning-focused computer science undergraduate with a strong foundation in statistical modeling, deep learning and data analytics. [cite: 4] Proficient in Python, Java, C, TensorFlow and PyTorch, with hands-on experience processing large-scale video data for real-time object detection and building interactive dashboards. [cite: 5] Skilled in data wrangling, visualization and cross-functional collaboration, seeking an AI/ML internship to apply predictive modeling at scale. [cite: 6]")
    
    st.header("Education")
    st.info("**Manipal University Jaipur** | B.Tech, Computer Science & Engineering (Specialization: Data Science) [cite: 8, 9]")
    col_edu1, col_edu2 = st.columns(2)
    with col_edu1:
        st.write("📅 **Timeline:** Jul 2023 - Jul 2027 [cite: 11]")
        st.write("🎯 **GPA:** 8.41 (till 5th semester) [cite: 10]")
    with col_edu2:
        st.write("🏆 **Achievements:** Dean's List Excellence Award (9+ GPA in 3rd & 4th semester) [cite: 12]")

# --- TAB 2: PROJECTS ---
with tab_projects:
    st.header("Featured Projects")
    
    st.markdown("""
    <div class="custom-card">
        <h3>🧠 Mental Health Wellness Chatbot</h3>
        <p><b>Tech Stack:</b> Python, Gradio, NLP | Hugging Face Spaces</p>
        <ul>
            <li>Developed an Al-powered mental wellness chatbot that provides empathetic conversations and mood support.</li>
            <li>Built an interactive web interface using Gradio Blocks and custom CSS styling.</li>
            <li>Deployed the application online using Hugging Face Spaces for public access.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True) # [cite: 27, 28, 30, 31, 33]
    
    st.markdown("""
    <div class="custom-card">
        <h3>🎬 Cinematch-AI</h3>
        <p><b>Tech Stack:</b> Python, SQL, Machine Learning pipelines, Streamlit</p>
        <ul>
            <li>CineMatch AI is a hybrid movie recommendation engine that combines collaborative filtering, content-based filtering, genre filtering, and KMeans clustering.</li>
            <li>Connected with IMDb and TMDB APIs to enhance the application with additional data.</li>
            <li>Created a streamlit application that allows customers to use the application for real-time movie recommendations.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True) # [cite: 34, 36, 38, 39]

# --- TAB 3: RESEARCH ---
with tab_research:
    st.header("Research & Publications")
    
    st.markdown("""
    <div class="custom-card">
        <h3>📹 Real-Time Suspicious Object Detection In Surveillance Footage Using AI</h3>
        <p><i>Selected in IEEE International Conference (ICDSINC) NIT RAIPUR</i></p>
        <ul>
            <li>Designed a system to process large-scale video datasets for object detection.</li>
            <li>Created structured datasets, optimized workflows, and presented performance reports (precision, recall, mAP).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True) # [cite: 15, 16, 17, 18]
    
    st.markdown("""
    <div class="custom-card">
        <h3>🔬 Early Cancer Detection Using ML and DL</h3>
        <p><i>3rd International Symposium on Data Science 2025, Manipal University Jaipur</i></p>
        <ul>
            <li>Presented a research paper reviewing and analyzing ML/DL techniques used for early cancer diagnosis.</li>
            <li>Discussed the role of Al in improving medical imaging analysis and predictive diagnostics.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True) # [cite: 20, 21, 23, 24]

# --- TAB 4: SKILLS ---
with tab_skills:
    st.header("Technical Arsenal")
    
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.subheader("Programming")
        st.write("Python, Java, C, SQL, MySQL, NoSQL [cite: 42]")
    with col_s2:
        st.subheader("ML & Data Tools")
        st.write("TensorFlow, Pytorch, Scikit Learn, Pandas, NumPy, Google BigQuery [cite: 41, 42]")
    with col_s3:
        st.subheader("Visualization")
        st.write("Power BI, Matplotlib, Seaborn, Plotly, Streamlit [cite: 41]")
