import os
import subprocess

list1 = os.listdir("videos")

for list in list1:
    video_number = list.split(" ")[1].split(" ")[0]
    file_name = list.split(" -")[1].split(" -")[0]

    subprocess.run(["ffmpeg","-i",f"Videos/{list}",f"audios/{video_number}_{file_name}.mp3"])

    print(video_number,file_name)