import streamlit as st
import requests

st.set_page_config(page_title="AI PDF Chatbot", layout="centered")

st.title("📄 Chat with your PDF (AI-powered)")
st.markdown("Upload a PDF once, then ask any question based on it.")

st.divider()

# File upload
st.subheader("📤 Upload PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
upload_btn = st.button("Upload PDF")

if upload_btn and uploaded_file:
    with st.spinner("Uploading PDF..."):
        files = {'file': uploaded_file.getvalue()}
        try:
            response = requests.post("http://localhost:8000/upload/", files=files)
            if response.status_code == 200:
                st.success("✅ PDF uploaded successfully!")
            else:
                st.error("❌ Failed to upload PDF.")
        except Exception as e:
            st.error(f"🚨 Upload Error: {e}")

st.divider()

# Ask Question
st.subheader("❓ Ask a Question")
question = st.text_input("Enter your question here")
ask_btn = st.button("Ask")

if ask_btn and question:
    with st.spinner("Thinking..."):
        try:
            res = requests.post("http://localhost:8000/ask/", json={"question": question})
            if res.status_code == 200:
                data = res.json()
                st.markdown("### 💬 Response")
                response_html = data['response'].replace('\n', '<br>')
                st.markdown(
                    f"""
    <div style='background-color: #ffffff; color: #000000; padding: 15px; border-radius: 8px;'>
        {response_html}
    </div>
    """,
    unsafe_allow_html=True
                    
                )

                # Sources
                if data.get("sources"):
                    st.markdown("#### 📚 Sources")
                    for source in set(data["sources"]):
                        st.markdown(f"- `{source}`")

            else:
                st.error("❌ Failed to get a response.")
        except Exception as e:
            st.error(f"🚨 Request Error: {e}")
