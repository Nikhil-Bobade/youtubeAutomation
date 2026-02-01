import streamlit as st
import requests
import time

st.title("🎧 YouTube DJ Automation")

uploaded = st.file_uploader(
    "Upload your songs (MP3/WAV)",
    type=["mp3", "wav"],
    accept_multiple_files=True
)

if uploaded:
    if st.button("Upload Songs"):
        files = [("files", (f.name, f, "audio/mpeg")) for f in uploaded]
        r = requests.post("http://127.0.0.1:8000/upload", files=files)

        if r.status_code == 200:
            st.success("Songs uploaded!")
        else:
            st.error("Upload failed")

if st.button("Generate Mixtape"):
    status = st.empty()
    progress = st.progress(0)

    status.info("Mixing audio...")
    progress.progress(25)
    time.sleep(1)

    res = requests.post("http://127.0.0.1:8000/generate", timeout=600)

    progress.progress(75)
    status.info("Rendering video...")

    data = res.json()
    progress.progress(100)

    if data["status"] == "completed":
        status.success("Mix & Video created!")

        st.subheader("🎥 Final Video")
        st.video(data["video"])

        st.subheader("📄 YouTube Description")
        st.text_area("Copy this", data["description"], height=300)

        st.download_button("Download MP3", open(data["audio"], "rb"), "mixtape.mp3")
        st.download_button("Download Video", open(data["video"], "rb"), "final_video.mp4")

    else:
        status.error(data["error"])
