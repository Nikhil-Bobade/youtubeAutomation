from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.audio_mixer import smooth_fade_mixtape
from app.services.description import generate_youtube_description
from app.services.video_generator import make_video
import os
import shutil
from fastapi import UploadFile ,File


router = APIRouter()

# Get project root (Automate_youtube)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

DATA_DIR = os.path.join(BASE_DIR, "data")
SONGS_DIR = os.path.join(DATA_DIR, "songs")
IMAGES_DIR = os.path.join(DATA_DIR, "images")
OUTPUT_DIR = os.path.join(DATA_DIR, "output")

@router.post("/upload")
def upload_songs(files:list[UploadFile]=File(...)):
    os.makedirs(SONGS_DIR,exist_ok=True)

    saved=[]

    for file in files:
        path=os.path.join(SONGS_DIR,file.filename)
        with open (path,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
            saved.append(file.filename)


    return {"Uploaded ": saved}        



@router.post("/generate")
def generate():
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        audio_path = os.path.join(OUTPUT_DIR, "mixtape.mp3")
        video_path = os.path.join(OUTPUT_DIR, "final_video.mp4")

        audio = smooth_fade_mixtape(SONGS_DIR, audio_path)

        description = generate_youtube_description(
            SONGS_DIR,
            "DJ Nikhil",
            "Non Stop Party Mix 2026",
            "Bollywood x EDM"
        )

        video = make_video(
            os.path.join(IMAGES_DIR, "dj-image.jpg"),
            audio_path,
            video_path
        )

        return {
            "status": "completed",
            "audio": audio_path,
            "video": video_path,
            "description": description
        }

    except Exception as e:
        return {"status": "failed", "error": str(e)}


