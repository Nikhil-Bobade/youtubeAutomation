import os 
from mutagen.mp3 import MP3
from datetime import timedelta


def format_time(seconds):
    return str(timedelta(seconds=int(seconds)))


def generate_youtube_description(folder,dj_name,mix_title,genre):
    files=sorted([f for f in os.listdir(folder) if f.endswith("MP3")])
    total_seconds=0

    lines=[

        f"🎧 {mix_title}",
        f"🔥 Mixed by {dj_name}",
        f"🎶 Genre: {genre}",
        "",
        "📌 Tracklist:"
    ]


    for file in files:
        audio=MP3(os.path.join(folder,file))
        lines.append(f"{format_time(total_seconds)}-{file.replace('.mp3','')}")
        total_seconds+=audio.info.length


    lines.append("")
    lines.append("#DJMix #NonStopDJ #EDMMix #BollywoodDJ")   
    
    
    return "\n".join(lines) 

