import os,subprocess
from PIL import Image

def make_video(image_path,audio_path,output):
    os.makedirs(os.path.dirname(output),exist_ok=True)


    temp_img="temp.jpg"
    Image.open(image_path).resize((1280,720)).save(temp_img)

    cmd=[

         "ffmpeg", "-y",
        "-loop", "1",
        "-i", temp_img,
        "-i", audio_path,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-shortest",
        output
    ]

    subprocess.run(cmd, check=True)
    os.remove(temp_img)
    return output

