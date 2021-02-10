import argparse
import subprocess
import os
import re

def cmdcall(command):
    process = subprocess.Popen(command)
    process.communicate()

def trimUrl(url):
    trimmed_url = re.search(r'[^&]+', url).group()
    print("[INFO]: Input URL trimmed to: {}".format(trimmed_url))
    return trimmed_url

def isValidUrl(url):
    if re.match(r'(https?://)?(www.)?youtube.com/watch\?v=[a-zA-Z0-9]+', url):
        return True
    print("[ERROR]: Invalid URL. Specify a valid URL or pass -no_url_check to skip URL check.")
    return False

def main(args):
    url = trimUrl(args.url)
    if not args.no_url_check and not isValidUrl(url):
        return -1
    tmp = 'tmp.ogg'
    dst = args.out + ".mp3"
    
    command_tmp = 'vlc ' + url + ' --sout=#transcode{acodec="opus",ab="128","channels=2",samplerate="44100"}:standard{access=file,mux=ogg,dst=' + tmp +'} vlc://quit'
    command_out = 'vlc ' + tmp + ' --sout=#transcode{acodec="mp3",ab="128","channels=2",samplerate="44100"}:standard{access=file{no-overwrite},mux=dummy,dst="' + dst + '"} vlc://quit'

    if not args.verbose:
        command_tmp += " --qt-notification=0 --qt-start-minimized"
        command_out += " --qt-notification=0 --qt-start-minimized"

    print("[INFO]: Downloading audio")
    cmdcall(command_tmp)
    print("[INFO]: Downloading audio finished")
    print("[INFO]: Converting to .mp3")
    cmdcall(command_out)
    print("[INFO]: Converting to .mp3 finished")
    print("[INFO]: Cleanup")
    os.remove(tmp)
    print("[INFO]: Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Specify youtube url to download audio from.")
    parser.add_argument("--out", default="out", metavar="<FILENAME>", help="Specify name of output file.")
    parser.add_argument("-verbose", action="store_true", help="Show VLC media player GUI when downloading audio.")
    parser.add_argument("-no_url_check", action="store_true", help="Disables url regex check. May result in unexpected behavior for invalid links.")
    args = parser.parse_args()
    main(args)

    