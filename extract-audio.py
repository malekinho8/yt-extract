import os
import argparse
import sys; sys.path.append(f'{os.sep}'.join(sys.path[0].split(os.sep)[0:-1]))
from src.utils import *

def main(url, time_start=None, time_end=None):
    get_audio_snippet(url, time_start, time_end)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='YouTube URL')
    parser.add_argument('time_start', help='Start time in format HH:MM:SS or MM:SS', nargs='?', default=None)
    parser.add_argument('time_end', help='End time in format HH:MM:SS or MM:SS', nargs='?', default=None)
    args = parser.parse_args()
    main(args.url, args.time_start, args.time_end)
