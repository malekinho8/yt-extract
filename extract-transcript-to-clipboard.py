import os
import argparse
import whisper
import sys; sys.path.append(f'{os.sep}'.join(sys.path[0].split(os.sep)[0:-1]))
import pyperclip
from src.utils import *
from moviepy.editor import *

def main(url,time_start=None,time_end=None,remove_audio_file=True):
    # first obtain the an audio snippet from the url and start/end time given
    out_file = get_audio_snippet(url,time_start,time_end)

    print('Audio snippet obtained!')
    
    # initialize the whisper model
    model = whisper.load_model('base')
    
    # get the transcript
    transcript = model.transcribe(out_file) # TODO: implement a faster method to obtain the transcript

    # remove the mp3 file if desired
    if remove_audio_file:
        os.remove(out_file)

    # copy the transcript to the clipboard
    pyperclip.copy(transcript['text']) 

    print('Transcript copied to clipboard!')


if __name__=="main":
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='YouTube URL')
    parser.add_argument('time_start', help='Start time in format HH:MM:SS or MM:SS', nargs='?', default=None)
    parser.add_argument('time_end', help='End time in format HH:MM:SS or MM:SS', nargs='?', default=None)
    parser.add_argument('remove_audio_file', help='Remove the audio file after obtaining the transcript', nargs='?', default=True, type=bool)
    args = parser.parse_args()
    main(args.url, args.time_start, args.time_end)

main("https://www.youtube.com/watch?v=TmnggxyakFw")