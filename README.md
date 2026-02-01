# 🎧 YouTube DJ Automation System

An end-to-end **AI-powered DJ automation platform** that converts multiple uploaded songs into a **smooth DJ mixtape**, automatically generates a **YouTube-ready video**, and creates an **SEO-optimized description with timestamps & hashtags** — all from a single web interface.

---

## 🚀 Features

- 🎵 Upload multiple MP3/WAV songs
- 🔊 Automatic DJ-style smooth fade mixing
- 🎬 Convert mixtape into MP4 video with DJ image
- 📝 Generate YouTube description with:
  - Tracklist with timestamps
  - Smart hashtags
  - DJ branding
- 📥 Download final MP3 & MP4
- 🌐 Web-based UI using Streamlit
- ⚡ FastAPI backend for processing

---

## 🏗️ System Architecture

```
Streamlit Frontend  
        ↓  
FastAPI Backend  
        ↓  
Audio Mixer (Pydub)  
        ↓  
Video Generator (FFmpeg)  
        ↓  
YouTube Metadata Engine  
```

---

## 📁 Folder Structure

```
Automate_youtube/
│
├── backend/
│   └── app/
│       ├── api/
│       │   └── routes.py
│       ├── services/
│       │   ├── audio_mixer.py
│       │   ├── video_generator.py
│       │   └── description.py
│       └── main.py
│
├── frontend/
│   └── app.py
│
├── data/
│   ├── songs/        ← Uploaded MP3/WAV files
│   ├── images/       ← DJ background image
│   └── output/       ← Generated MP3 & MP4
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Create Virtual Environment

```bash
python -m venv djenv
djenv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg

Download FFmpeg from:
https://ffmpeg.org/download.html  

Add FFmpeg to your system PATH.

---

## ▶️ Run Backend (FastAPI)

```bash
cd backend
uvicorn app.main:app --reload
```

Open API:
```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend (Streamlit)

```bash
cd frontend
streamlit run app.py
```

Open UI:
```
http://localhost:8501
```

---

## 🧪 How to Use

1. Upload MP3/WAV songs
2. Click **Upload Songs**
3. Click **Generate Mixtape**
4. Wait for processing
5. Preview video
6. Download MP3 & MP4
7. Copy YouTube description

---

## 📦 Output Files

Generated files are saved in:

```
data/output/
  ├── mixtape.mp3
  └── final_video.mp4
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|----------|
Frontend | Streamlit  
Backend | FastAPI  
Audio | Pydub  
Video | FFmpeg  
Metadata | Python  
Server | Uvicorn  

---

## 🧠 Future Upgrades

- YouTube Auto-Upload
- AI Thumbnail Generator
- Trending Hashtag AI
- Multi-user login
- Cloud deployment

---

## 👨‍💻 Author

**Nikhil Bobade**  
Python Developer | Data Scientist | ML Engineer | Automation Builder  

---

## ⭐ If you like this project

Please star ⭐ the repo and share it with DJ creators!

---

🔥 This project can be turned into a **paid SaaS DJ automation platform**.
