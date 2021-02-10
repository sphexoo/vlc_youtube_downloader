# vlc_yt_downloader
Download audio from any youtube video using a python script. 
The app uses VLC media players functionality for downloading audio from youtube.

usage: python downloader.py [-h] [--out <FILENAME>] [-verbose] url

positional arguments:
  url               Specify youtube url to download audio from.

optional arguments:
  -h, --help        show this help message and exit
  --out <FILENAME>  Specify name of output file.
  -verbose          Show VLC media player GUI when downloading audio.
