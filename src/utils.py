import os
import re
from pytube import YouTube
from moviepy.editor import *

def convert_time_to_seconds(time):
    if time is not None:
        time = time.split(':')
        if len(time) == 2:
            return int(time[0])*60 + int(time[1])
        elif len(time) == 3:
            return int(time[0])*3600 + int(time[1])*60 + int(time[2])
        else:
            return 0
    else:
        return 

def convert_filename(filename):
    s = filename.replace(' ','-').lower()
    s = re.sub(r'[^a-zA-Z0-9()-_\s]', '', s)
    s = re.sub(r'-{2,}','-',s)
    return s

def url2audio(url:str):
    yt = YouTube(url)
    name = convert_filename(yt.title) + '.wav'
    audio = yt.streams.filter(only_audio=True).first()
    return audio, name

def audio2downloads(url):
    audio, name = url2audio(url)
    # specify the download folder
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    # download the mp3 file
    temp_file = os.path.join(download_path, "temp_audio.webm")
    audio.download(download_path, filename="temp_audio.webm")
    
    # convert the downloaded file to mp3
    clip = AudioFileClip(temp_file)
    clip.write_audiofile(os.path.join(download_path, name), codec='pcm_s16le')
    
    # remove the temporary file
    os.remove(temp_file)

def get_audio_snippet(url,time_start:str,time_end:str):
    audio, name = url2audio(url)
    # specify the download folder
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    # download the mp3 file
    temp_file = os.path.join(download_path, "temp_audio.webm")
    audio.download(download_path, filename="temp_audio.webm")

    if time_start is not None and time_end is not None:
        # convert time_start and time_end to seconds
        time_start_sec = convert_time_to_seconds(time_start)
        time_end_sec = convert_time_to_seconds(time_end)
        
        # convert the downloaded file to mp3
        clip = AudioFileClip(temp_file)
        clip = clip.subclip(time_start_sec,time_end_sec)

        # save clip to output
        trimmed_name = name.split('.')[0] + f'_[{time_start}-{time_end}].mp3'.replace(':',';')
        clip.write_audiofile(os.path.join(download_path, trimmed_name))

        # specify the output file name
        out_file = os.path.join(download_path, trimmed_name)
    else:
        # convert the downloaded file to mp3
        clip = AudioFileClip(temp_file)
        full_name = name.split('.')[0] + '.mp3'
        clip.write_audiofile(os.path.join(download_path, full_name))

        # specify the output file name
        out_file = os.path.join(download_path, full_name)
    
    # remove the temporary file
    os.remove(temp_file)

    return out_file